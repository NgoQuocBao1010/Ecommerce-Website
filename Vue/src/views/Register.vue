<template>
    <div class="register-container">
        <div class="register-wrapper">
            <form @submit.prevent="register">
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
                            v-model="email"
                            spellcheck="false"
                            required
                        />
                        <p class="errors">{{ error.email }}</p>
                    </div>
                    <div class="input">
                        <label for="password">Password</label>
                        <input type="password" v-model="password1" required />
                        <p class="errors">{{ error.password }}</p>
                    </div>
                    <div class="input">
                        <label for="password2">Confirm Password</label>
                        <input type="password" v-model="password2" required />
                        <p class="errors">{{ error.password }}</p>
                    </div>
                </div>

                <div class="loading-animation" v-show="loadingAnimation">
                    <div class="spinner">
                        <div class="bubble-1"></div>
                        <div class="bubble-2"></div>
                    </div>
                </div>

                <div class="submit">
                    <button type="submit">Register</button>
                    <router-link :to="{ name: 'Login' }">
                        Have an account? Login here
                    </router-link>
                </div>
            </form>
        </div>
    </div>
</template>

<script>
import axios from "axios";
import { createToast } from "mosha-vue-toastify";

export default {
    name: "Register",
    data() {
        return {
            email: "",
            password1: "",
            password2: "",
            error: {
                email: "",
                password: "",
            },

            loadingAnimation: false,
        };
    },
    methods: {
        validatePassword() {
            if (this.password1 !== this.password2) {
                this.error.password =
                    "Password and confirm password do not match";

                return false;
            }

            if (this.password1.length < 5) {
                this.error.password =
                    "Password needs to be at least 5 letters-long!";

                return false;
            }

            if (
                /[a-z]/.test(this.password1) &&
                /[A-Z]/.test(this.password1) &&
                /\d/.test(this.password1)
            ) {
                this.error.password = "";
                return true;
            } else {
                this.error.password =
                    "Password needs to contain number, uppercase and lowercase letter";

                return false;
            }
        },
        register() {
            if (!this.validatePassword()) return;

            const data = {
                email: this.email,
                password: this.password1,
            };

            this.loadingAnimation = true;

            axios
                .post("http://127.0.0.1:8000/api/register", data)
                .then((response) => {
                    this.loadingAnimation = false;
                    this.$router.push({ name: "Login" });

                    createToast(`Your account is created`, {
                        type: "success",
                        timeout: 3000,
                        position: "bottom-right",
                        transition: "bounce",
                        hideProgressBar: true,
                        showIcon: true,
                    });
                })
                .catch((error) => {
                    this.loadingAnimation = false;
                    const data = error.response.data;

                    for (const key in data.errors) {
                        this.error[key] = data.errors[key][0];
                    }
                });
        },
    },
};
</script>

<style lang="scss" scoped>
.register-container {
    position: absolute;
    top: 0;
    width: 100%;
    min-height: 100vh;
    background-color: black;
    display: flex;
    align-items: center;
    justify-content: center;

    .register-wrapper {
        width: 90%;
        max-width: 900px;
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

                    .errors {
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
                margin: 2rem 0;
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
        .register-wrapper {
            display: flex;

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
