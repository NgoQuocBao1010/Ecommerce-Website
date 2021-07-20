<template>
    <div class="account-container">
        <div class="account">
            <h1 v-if="!authenticated">
                <router-link :to="{ name: 'Login' }">Login</router-link>
                to your account for better experience
            </h1>

            <div v-if="authenticated" class="account-container">
                <div class="header">
                    <h2 class="title">Account Settings</h2>

                    <div class="buttons">
                        <button @click="toggleEdit" class="btn">
                            <i class="fas fa-pen"></i>
                        </button>
                        <button class="btn logout" @click="logout">
                            <i class="fas fa-sign-out-alt"></i>
                        </button>
                    </div>
                </div>

                <form @submit.prevent="">
                    <div class="input">
                        <label for="full-name">Full name</label>
                        <input
                            spellcheck="false"
                            type="text"
                            name="full-name"
                            :class="{ active: !nonEdit }"
                            v-model="fullName"
                            :readonly="nonEdit"
                            ref="firstEdit"
                        />
                    </div>
                    <div class="gender">
                        <p>Gender</p>

                        <div class="option-wrapper">
                            <div class="option">
                                <input
                                    type="radio"
                                    value="male"
                                    v-model="gender"
                                    :readonly="nonEdit"
                                />
                                <label for="one">Male</label>
                            </div>

                            <div class="option">
                                <input
                                    type="radio"
                                    value="female"
                                    v-model="gender"
                                    :readonly="nonEdit"
                                />
                                <label for="two">Female</label>
                            </div>
                        </div>
                    </div>
                    <div class="input">
                        <label for="email">Email</label>
                        <input
                            spellcheck="false"
                            type="email"
                            name="email"
                            v-model="email"
                            readonly
                        />
                    </div>
                    <div class="input">
                        <label for="phone">Phone</label>
                        <input
                            type="text"
                            spellcheck="false"
                            name="phone"
                            :class="{ active: !nonEdit }"
                            v-model="phone"
                            :readonly="nonEdit"
                        />
                    </div>
                    <div class="input">
                        <label for="address">Address</label>
                        <input
                            spellcheck="false"
                            type="text"
                            name="address"
                            :class="{ active: !nonEdit }"
                            v-model="address"
                            :readonly="nonEdit"
                        />
                    </div>
                    <div class="input">
                        <label for="dob">Date of birth</label>
                        <input
                            type="date"
                            name="dob"
                            v-model="dateOfBirth"
                            :class="{ active: !nonEdit }"
                            :readonly="nonEdit"
                        />
                    </div>
                </form>

                <button
                    type="submit"
                    class="btn save"
                    v-show="!nonEdit"
                    @click="saveInfo"
                >
                    Save
                </button>
            </div>
        </div>

        <div class="order-container" v-if="authenticated && orders">
            <h1 class="title">Your Orders, ({{ orders.length }} order)</h1>
            <div class="orders">
                <p v-if="orders.length === 0">
                    No order yet!!
                    <router-link :to="{ name: 'Product' }">
                        Go shopping now
                    </router-link>
                </p>
                <OrderCard
                    v-for="(order, index) in orders"
                    :key="index"
                    :order="order"
                />
            </div>
        </div>
    </div>
</template>

<script>
import axios from "axios";
import { mapState, mapMutations } from "vuex";

import OrderCard from "../components/OrderCard.vue";

export default {
    name: "Account",
    components: {
        OrderCard,
    },
    data() {
        return {
            nonEdit: true,
            fullName: "",
            gender: "",
            email: "",
            phone: "",
            address: "",
            dateOfBirth: "",

            orders: null,
        };
    },
    computed: {
        ...mapState(["user", "authenticated"]),
    },
    watch: {
        nonEdit(newVal) {
            if (!newVal) this.$refs.firstEdit.focus();
        },
        user(newVal, oldVal) {
            if (newVal) {
                this.getOrders();
                ({
                    email: this.email,
                    fullName: this.fullName,
                    gender: this.gender,
                    phone: this.phone,
                    address: this.address,
                    dateOfBirth: this.dateOfBirth,
                } = this.user);
            }
        },
    },
    methods: {
        ...mapMutations(["logout", "getUserProfile"]),
        getOrders() {
            axios
                .get("http://127.0.0.1:8000/my-orders/")
                .then((response) => {
                    console.log(response.data);
                    this.orders = response.data;
                })
                .catch((error) => {
                    console.log(error);
                });
        },
        toggleEdit() {
            if (this.nonEdit) this.nonEdit = false;
        },
        saveInfo() {
            const data = {
                email: this.email,
                fullName: this.fullName,
                gender: this.gender,
                phone: this.phone,
                address: this.address,
                dateOfBirth: this.dateOfBirth,
            };

            axios
                .post("http://127.0.0.1:8000/api/update-profile", data)
                .then((response) => {
                    if (response.status === 200) this.getUserProfile(data);
                })
                .catch((error) => {
                    console.log(error);
                });

            this.nonEdit = true;
        },
    },
    mounted() {
        if (this.user) {
            this.getOrders();
            ({
                email: this.email,
                fullName: this.fullName,
                gender: this.gender,
                phone: this.phone,
                address: this.address,
                dateOfBirth: this.dateOfBirth,
            } = this.user);
        }
    },
};
</script>

<style lang="scss" scoped>
.account-container {
    width: 100%;
    position: relative;

    > * {
        width: 100%;
        max-width: 1000px;
        margin: 3rem auto;
        padding: 1rem 3rem;
    }

    .title {
        font-size: 2rem;
        text-transform: uppercase;
        padding: 0;
    }

    .account {
        h1 {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            font-size: 3rem;
        }

        .btn {
            width: 3rem;
            aspect-ratio: 1 / 1;
            padding: 0.2rem 0;
            margin-left: 0.7rem;

            border: none;
            border-radius: 50%;
            background: var(--primary-color);
        }

        .account-container {
            width: 100%;
            padding: 2rem 0;
            box-shadow: rgba(0, 0, 0, 0.15) 1.95px 1.95px 2.6px;

            .header {
                // background: lightblue;
                padding: 1rem 0;
                display: flex;
                align-items: center;
                justify-content: space-between;

                .buttons {
                    padding: 0 1.2rem;

                    .btn {
                        span {
                            display: none;
                        }
                    }

                    .logout {
                        color: white;
                        background: hsl(0, 85%, 55%);
                    }
                }
            }

            form {
                width: 100%;
                display: flex;
                flex-wrap: wrap;
                gap: 1rem;

                > * {
                    flex: 1 1 45%;
                    margin-bottom: 2rem;
                }

                .input {
                    width: 100%;
                    min-width: 250px;
                    display: flex;
                    flex-direction: column;
                    font-size: 1.5rem;

                    input {
                        width: 100%;
                        font-size: 1.8rem;
                        line-height: 2;
                        padding: 0.5rem;
                    }
                }

                input[type="text"],
                input[type="date"],
                input[type="email"] {
                    border: none;
                    border-bottom: 1px solid black;
                    transition: border 0.2s ease-in-out;
                }

                input[type="text"]:focus,
                input[type="date"]:focus,
                input[type="email"]:focus {
                    border: none;
                    outline: none;
                    border-bottom: 1px solid black;
                }

                input[type="text"].active,
                input[type="date"].active {
                    border: 1px solid black;
                }

                input[type="text"].active:focus,
                input[type="date"].active:focus {
                    outline: none;
                    border: none;
                    outline: 2px solid var(--primary-color);
                }

                .gender {
                    width: 100%;
                    display: flex;
                    flex-direction: column;
                    justify-content: space-between;

                    p {
                        font-size: 1.5rem;
                    }

                    .option-wrapper {
                        width: 100%;
                        height: 50%;
                        display: flex;
                        align-items: center;
                        justify-content: space-around;
                        .option {
                            label {
                                font-size: 1.5rem;
                                margin-left: 1.5rem;
                            }
                        }
                    }
                }
            }

            .save {
                padding: 1rem 4rem;
                margin: 0 auto;
                aspect-ratio: initial;
                display: flex;
                justify-content: center;
                align-items: center;
                border-radius: 10px;
                font-size: 1.6rem;
            }
        }
    }

    .order-container {
        max-width: 1000px;

        .orders {
            outline: 1px solid rgb(0, 0, 0, 0.4);
            margin: 2rem auto;
            padding: 1rem 4rem;

            p {
                text-align: center;
                font-size: 1.2rem;
            }
        }
    }

    @media only screen and (min-width: 768px) {
        .account-container {
            .header {
                .btn {
                    width: 3.5rem !important;
                    margin-left: 2rem;
                    cursor: pointer;
                    transition: all 0.2s ease;
                }

                .btn:hover {
                    transform: scale(1.2);
                }
            }

            .save {
                border-radius: 20px !important;
                border: 2px solid black;
                background: #fff;
                color: black;
                cursor: pointer;
                transition: all 0.2s ease;
            }

            .save:hover {
                color: var(--primary-color);
                background: black;
            }
        }
    }
}
</style>
