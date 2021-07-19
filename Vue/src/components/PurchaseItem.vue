<template>
    <div class="card-wrapper">
        <img :src="item.thumbnail" :alt="item.name" />
        <i class="fas fa-trash" @click="removeItem"></i>
        <div class="info">
            <h3 class="title">{{ item.name }}</h3>
            <p>Color: {{ item.color }}</p>
            <p>Size: {{ item.size }}</p>
            <div class="quantity">
                <input
                    type="number"
                    name="quantity"
                    v-model="quantity"
                    min="1"
                />
                <p>{{ $filters.formatMoneyToVND(price) }}.000 VND</p>
            </div>
        </div>
    </div>
</template>

<script>
import axios from "axios";
import { mapMutations } from "vuex";

export default {
    name: "PurchaseCard",
    props: {
        item: Object,
    },
    data() {
        return {
            shoe: {},
            quantity: null,
        };
    },
    computed: {
        price() {
            const originalPrice = this.item.price;

            return originalPrice * this.quantity;
        },
    },
    watch: {
        quantity(newVal, oldVal) {
            if (!oldVal) return;

            const newValue = {
                id: this.item.id,
                quantity: newVal,
            };

            this.quantityUpdate(newValue);
        },
    },
    methods: {
        ...mapMutations(["quantityUpdate", "removeItemInCart"]),
        removeItem() {
            if (confirm("Removing this item from your cart?")) {
                this.removeItemInCart(this.item.id);
            }
        },
    },
    mounted() {
        this.quantity = this.item.quantity;
    },
};
</script>

<style lang="scss" scoped>
.card-wrapper {
    min-width: 250px;
    max-width: 250px;
    min-height: 450px;
    max-height: 450px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: space-between;
    padding: 1rem;
    margin: 1rem 2rem;
    box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;
    position: relative;

    i {
        font-size: 1.8rem;
        color: rgb(107, 107, 107);
        position: absolute;
        top: 5px;
        right: 5px;
        // opacity: 0.7;
    }

    img {
        width: 90%;
        aspect-ratio: 1 / 1;
        margin: 0.5rem;
    }

    .info {
        margin-top: 1rem;
        width: 90%;

        .title {
            margin-bottom: 2rem;
        }
    }

    .quantity {
        display: flex;
        padding: 1rem 0;
        align-items: center;
        justify-content: space-between;
        gap: 20px;

        input {
            width: 25%;
            text-align: center;
        }
    }

    @media screen and (min-width: 1200px) {
        i {
            cursor: pointer;
            transition: all 0.3s ease;
            &:hover {
                color: rgb(218, 45, 45);
                transform: rotate(5deg);
            }
        }

        .info {
            h3 {
                font-size: 2rem;
            }
            p {
                font-size: 1.5rem;
            }
        }
    }
}
</style>
