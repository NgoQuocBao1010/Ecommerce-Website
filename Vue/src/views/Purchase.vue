<template>
    <section class="purchase">
        <div class="form-wrapper">
            <h3>Purchase Information</h3>
            <form @submit.prevent="submit">
                <div class="input">
                    <label for="name">Name</label>
                    <input type="text" name="name" required v-model="name" />
                </div>

                <div class="input">
                    <label for="phone">Phone</label>
                    <input
                        type="numeric"
                        name="phone"
                        required
                        v-model="phone"
                    />
                </div>

                <div class="input" style="flex-basis: 100%">
                    <label for="address">Address</label>
                    <input
                        type="text"
                        name="address"
                        required
                        v-model="address"
                    />
                </div>

                <div class="input" style="flex-basis: 100%">
                    <label for="note">Note for your shipping</label>
                    <input type="text" name="note" v-model="note" />
                </div>

                <button style="flex-basis: 100%" type="submit">Purchase</button>

                <div class="note" style="flex-basis: 100%">
                    Lorem ipsum dolor sit amet, consectetur adipisicing elit.
                    Deserunt, placeat!
                </div>
            </form>
        </div>
        <div class="cart-wrapper">
            <h3>Your shopping cart</h3>
            <h4
                v-if="cart.length === 0"
                style="font-size: 16px; font-weight=500;"
            >
                There is no item in your cart
            </h4>
            <div v-else class="items">
                <PurchaseItem
                    v-for="item in cart"
                    :key="item.id"
                    :item="item"
                />
                <!-- {{ item.name }} {{ item.color }} {{ item.size }},
                {{ item.quantity }} -->
            </div>
            <div class="price-info">
                <div class="coupon-input">
                    <button>Coupon Code</button>
                    <input type="text" name="coupon" v-model="couponCode" />
                </div>

                <div class="price-couting">
                    <div class="field">
                        <h3>Original Price</h3>
                        <span>{{ totalPrice }}.000 VND</span>
                    </div>
                    <div class="field">
                        <h3>Coupon</h3>
                        <span>{{ couponCode }}</span>
                    </div>
                    <div class="field">
                        <h3>Other Sales</h3>
                        <span>...</span>
                    </div>
                    <div class="field total">
                        <h3>Total Price</h3>
                        <span>{{ totalPrice }}.000 VND</span>
                    </div>
                </div>
            </div>
        </div>
    </section>
</template>

<script>
import { mapState, mapMutations } from "vuex";
import { createToast } from "mosha-vue-toastify";

import PurchaseItem from "../components/PurchaseItem.vue";

export default {
    name: "Purchase",
    components: {
        PurchaseItem,
    },
    data() {
        return {
            name: "",
            phone: "",
            address: "",
            note: "",
            couponCode: "",
            // totalPrice: 0,
        };
    },
    computed: {
        ...mapState(["cart"]),
        totalPrice() {
            let result = 0;
            console.log(this.cart);
            this.cart.forEach((item) => {
                console.log(item);
                // const itemPrice = this.$store.getters.getShoeByID(
                //     item.productId
                // ).price;
                // const price = itemPrice * item.quantity;
                // result += price;
            });

            return result;
        },
    },
    methods: {
        ...mapMutations(["clearCart"]),
        submit() {
            if (this.cart.length === 0) {
                createToast("No items in your cart", {
                    type: "danger",
                    timeout: 3000,
                    position: "bottom-right",
                    transition: "bounce",
                    hideProgressBar: true,
                    showIcon: true,
                });
                return;
            }
            // const cartToJson = JSON.stringify(this.cart);

            const purchaseInfo = {
                name: this.name,
                phone: this.phone,
                address: this.address,
                note: this.note,
                cart: this.cart,
                price: this.totalPrice,
            };

            this.clearCart();
            console.log(purchaseInfo);
            this.$router.push({ name: "Home" });

            createToast("Purchase Successful!", {
                type: "success",
                timeout: 3000,
                position: "bottom-right",
                transition: "bounce",
                hideProgressBar: true,
                showIcon: true,
            });
        },
    },
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700&display=swap");
.purchase {
    display: flex;
    justify-content: center;
    align-items: center;
    flex-wrap: wrap;
    gap: 2rem;
    margin: 2rem auto;
    width: 90%;
    /* max-width: 1200px; */
}

.form-wrapper,
.cart-wrapper {
    width: 100%;
    padding: 1em;
    box-shadow: rgba(0, 0, 0, 0.1) 0px 4px 12px;
}

.cart-wrapper {
    order: 1;
}

.form-wrapper {
    order: 2;
}

.form-wrapper h3,
.cart-wrapper h4,
.cart-wrapper h3 {
    text-align: center;
    font-size: 2rem;
}

.form-wrapper form {
    display: flex;
    justify-content: center;
    align-items: center;
    min-width: 100%;
    flex-wrap: wrap;
    gap: 0.5rem;
    margin: 5rem 0;
}

.form-wrapper .input {
    flex: 1 1 40%;
    min-width: 100px;
    display: flex;
    flex-direction: column;
    margin-bottom: 2rem;
}

.input input,
.input label {
    font-family: "Roboto", sans-serif;
    font-weight: 400;
}

.input label {
    font-size: 12px;
}

.input input {
    border: none;
    border-bottom: 2px solid rgb(44, 44, 44);
    font-size: 14px;
    min-height: 40px;
    line-height: 2;
}

.input input:focus {
    /* border: none; */
    outline: none;
}

form button {
    min-width: 50%;
    max-width: 50%;
    font-size: 14px;
    border-radius: 15px;
    border: none;
    font-family: "Poppins", sans-serif;
    font-weight: bold;
    background: var(--primary-color);
}

.note {
    text-align: center;
    font-size: 10px;
}

.cart-wrapper h4 {
    padding: 4rem 0;
    font-weight: 400;
}

.items {
    display: flex;
    align-items: center;
    min-height: 100px;
    /* justify-content: space-around; */
    /* text-align: center; */
    overflow-x: scroll;
}

.price-info {
    margin: 1rem auto;
    padding: 1.5rem;
    max-width: 500px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    box-shadow: rgba(149, 157, 165, 0.1) 0px 8px 24px;
}

.price-couting {
    margin-top: 1.2rem;
    width: 100%;
}

.price-couting h3 {
    text-align: left;
    font-size: 1.2rem;
    font-weight: 500;
}

.price-couting .total {
    margin-top: 0.5rem;
    font-weight: bold;
}

.coupon-input {
    display: flex;
}

.coupon-input button,
.coupon-input input {
    height: 4rem;
    line-height: 2;
}

.coupon-input button {
    background: var(--primary-color);
    font-family: "Poppins", sans-serif;
    font-size: 1.4rem;
    font-weight: bold;
    padding: 0 0.5rem;
    text-align: center;
    display: inline-block;
    outline: none;
    border: none;
}

.field {
    display: flex;
    width: 100%;
    margin: 1rem 0;
}

.field span {
    margin-left: auto;
}

@media only screen and (min-width: 1200px) {
    .purchase {
        padding-top: 3rem;
        flex-wrap: nowrap;
        align-items: flex-start;
    }

    .form-wrapper,
    .cart-wrapper {
        flex-basis: 40%;
        min-width: 500px;
        max-width: 1000px;
    }

    .cart-wrapper {
        order: 2;
    }

    .form-wrapper {
        order: 1;
    }

    .form-wrapper .input {
        margin-bottom: 3rem;
    }

    .input label {
        font-size: 1.5rem;
    }

    .input input {
        font-size: 1.8rem;
    }

    form button {
        padding: 1rem 0;
        border-radius: 1000px;
        font-size: 17px;
        cursor: pointer;

        transition: all 0.3s ease;
    }

    form button:hover {
        background: black;
        color: var(--primary-color);
    }

    .price-couting {
        margin: 3rem 0;
    }

    .price-couting h3,
    .price-couting span {
        font-size: 2rem;
    }
}
</style>
