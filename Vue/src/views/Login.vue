<template>
    <div class="login-container">
        <div class="login-wrapper">
            <form @submit.prevent="login">
                <div class="animated-logo">
                    <!-- <p>Welcome</p> -->
                    <span style="--i: 1">f</span>
                    <span style="--i: 2">o</span>
                    <span style="--i: 3">o</span>
                    <span style="--i: 4">t</span>
                    <span style="--i: 5">c</span>
                    <span style="--i: 6">o</span>
                </div>
                <div class="input-container">
                    <div class="input">
                        <label for="email">Email</label>
                        <input
                            type="email"
                            name="email"
                            v-model="email"
                            spellcheck="false"
                            required
                        />
                        <p class="error">{{ error }}</p>
                    </div>
                    <div class="input">
                        <label for="password">Password</label>
                        <input type="password" v-model="password" required />
                        <p class="error">{{ error }}</p>
                    </div>
                </div>

                <div class="loading-animation" v-show="loadingAnimation">
                    <div class="spinner">
                        <div class="bubble-1"></div>
                        <div class="bubble-2"></div>
                    </div>
                </div>

                <div class="submit">
                    <button type="submit">Login</button>
                    <router-link :to="{ name: 'Register' }">
                        Create an accout
                    </router-link>
                </div>
            </form>
            <div class="introduction">
                <img src="../assets/login-thumbnail.png" alt="" />
            </div>
        </div>
    </div>
</template>

<script>
import axios from "axios";
import { mapActions } from "vuex";
import { createToast } from "mosha-vue-toastify";

export default {
    name: "Login",
    data() {
        return {
            email: "",
            password: "",
            error: "",

            loadingAnimation: false,
        };
    },
    methods: {
        ...mapActions(["logginIn"]),
        login() {
            const loginForm = {
                email: this.email,
                password: this.password,
            };

            // Start loading animation
            this.loadingAnimation = true;

            axios
                .post("http://127.0.0.1:8000/api/login", loginForm)
                .then((response) => {
                    // Get token from response
                    const token = response.data["auth_token"];

                    // End loading animation
                    this.loadingAnimation = false;

                    // loggin in globaly by using vuex
                    this.logginIn(token);

                    //  redirect to home page
                    this.$router.push({ name: "Home" });

                    // Make an notification
                    createToast(`Welcome, ${this.email}`, {
                        type: "success",
                        timeout: 3000,
                        position: "bottom-right",
                        transition: "bounce",
                        hideProgressBar: true,
                        showIcon: true,
                    });

                    this.email = "";
                    this.password = "";
                    this.error = "";
                })
                .catch((err) => {
                    console.log(err);
                    if (err.response.status === 401) {
                        this.error = err.response.data.message;

                        // End loading animation
                        this.loadingAnimation = false;
                    }
                });
        },
    },
};
</script>

<style lang="scss" scoped>
.login-container {
    position: absolute;
    top: 0;
    width: 100%;
    min-height: 100vh;
    background-color: black;
    display: flex;
    align-items: center;
    justify-content: center;

    .login-wrapper {
        width: 90%;
        max-width: 900px;
        height: 60vh;
        aspect-ratio: 7 / 4;
        padding: 3rem 0;
        box-shadow: rgb(248, 178, 205, 0.5) 0px 3px 8px;

        .introduction {
            display: none;
        }

        form {
            width: 100%;
            height: 100%;
            display: flex;
            flex-direction: column;
            justify-content: space-around;
            align-items: center;
            color: white;

            .animated-logo {
                p {
                    text-align: center;
                    font-size: 2rem;
                }
                span {
                    font-family: "Comfortaa", cursive;
                    font-size: 5rem;
                    font-weight: bold;
                    letter-spacing: 7px;
                    color: var(--primary-color);

                    display: inline-block;
                    /* text-transform: uppercase; */
                    animation: flip 2s infinite;
                    animation-delay: calc(0.2s * var(--i));
                }

                span:nth-child(1) {
                    margin-left: 20px;
                }

                @keyframes flip {
                    0%,
                    80% {
                        transform: rotateY(360deg);
                    }
                }
            }

            .input-container {
                width: 90%;
                .input {
                    display: flex;
                    flex-direction: column;
                    font-size: 2rem;
                    min-width: 100%;
                    margin: 1rem 0;

                    label {
                        color: var(--primary-color);
                    }

                    input {
                        width: 100%;
                        padding: 5px 20px;
                        font-size: 1.8rem;
                        border-radius: 5px;
                    }

                    .error {
                        color: red;
                        font-size: 1.2rem;
                    }
                }
            }

            .loading-animation {
                .spinner {
                    position: relative;
                    width: 45px;
                    height: 45px;
                    margin: 0 auto;
                    animation: loadingI 2s linear infinite;

                    .bubble-1,
                    .bubble-2 {
                        position: absolute;
                        top: 0;
                        width: 25px;
                        height: 25px;
                        border-radius: 100%;
                        background-color: var(--primary-color);
                        animation: bounce 2s ease-in-out infinite;
                    }
                    .bubble-2 {
                        top: auto;
                        bottom: 0;
                        animation-delay: -1s;
                    }

                    @keyframes loadingI {
                        100% {
                            transform: rotate(360deg);
                        }
                    }

                    @keyframes bounce {
                        0%,
                        100% {
                            transform: scale(0);
                        }
                        50% {
                            transform: scale(1);
                        }
                    }
                }
            }

            .submit {
                display: flex;
                flex-direction: column;
                align-items: center;

                button {
                    padding: 1rem 3rem;
                    font-size: 2rem;
                    cursor: pointer;
                    border: 2px solid var(--primary-color);
                    color: var(--primary-color);
                    background-color: black;

                    transition: all 0.3s ease-in-out;
                }

                a {
                    text-decoration: underline;
                    cursor: pointer;
                    font-size: 1.5rem;
                    color: var(--primary-color);
                    margin-top: 2rem;
                }
            }
        }
    }

    @media only screen and (min-width: 720px) {
        form {
            .animated-logo {
                span {
                    font-size: 6rem !important;
                }
            }

            button:hover {
                background-color: var(--primary-color) !important;
                color: black !important;
            }
        }
    }

    @media only screen and (min-width: 1140px) {
        .login-wrapper {
            display: flex;

            > * {
                flex-basis: 50%;
            }

            .introduction {
                display: flex;
                justify-content: center;
                align-items: center;
                position: relative;

                img {
                    width: 70%;
                    z-index: 1;
                }
            }

            .introduction::before {
                content: "";
                position: absolute;
                top: 50%;
                left: 50%;
                transform: translate(-60%, -110%);
                min-width: 150px;
                min-height: 150px;
                border-radius: 50%;
                background-color: var(--primary-color);
            }
        }
    }
}
</style>
