<template>
    <div class="order-wrapper">
        <div class="header">
            <div class="code">#{{ order.id }}</div>
            <div class="status delivered">{{ order.status }}</div>
        </div>

        <div class="orders">
            <div class="item" v-for="item in order.cart" :key="item.id">
                <img
                    :src="`${order.domain}${item.thumbnail}`"
                    :alt="item.name"
                />
                <p>
                    {{ item.name }}, {{ item.color }}, {{ item.size }},
                    <strong>X{{ item.quantity }}</strong>
                </p>
            </div>
        </div>

        <div class="footer">
            <h4>Total Price</h4>
            <h4 class="price">
                {{ $filters.formatMoneyToVND(order.totalPrice) }}.000 VND
            </h4>
        </div>
    </div>
</template>

<script>
import PurchaseItem from "./PurchaseItem.vue";

export default {
    name: "OrderCard",
    components: {
        PurchaseItem,
    },
    props: {
        order: Object,
    },
};
</script>

<style lang="scss" scoped>
.order-wrapper {
    width: 100%;
    max-width: 800px;
    border: 1px solid black;
    border-radius: 8px;
    padding: 0.5rem 1rem;
    margin: 1rem auto;

    .header {
        display: flex;
        justify-content: space-between;
        padding-bottom: 0.2rem;
        border-bottom: 1px solid rgb(0, 0, 0, 0.2);

        .code {
            font-size: 1.2rem;
            font-weight: bold;
            color: var(--primary-color);
        }

        .status {
            padding: 0.2rem 1rem;
            display: flex;
            align-items: center;
            justify-content: center;
            border-radius: 1000px;
        }

        .delivered {
            color: black;
            background: lightgreen;
        }
    }

    .item {
        width: 100%;
        padding: 1rem 0;
        display: flex;
        align-items: center;
        gap: 20px;

        img {
            width: 30%;
            aspect-ratio: 1 / 1;
        }

        p {
            font-size: 1.2rem;
            text-align: center;
        }
    }

    .footer {
        display: flex;
        justify-content: space-between;
        padding: 1rem 0;

        h4 {
            font-size: 1.2rem;
        }
    }

    @media screen and (min-width: 1200px) {
        .header {
            .code {
                font-size: 2rem;
            }

            .status {
                font-size: 1.5rem;
            }
        }

        .item {
            p {
                font-size: 1.8rem;
            }
        }

        .footer {
            h4 {
                font-size: 1.8rem;
            }
        }
    }
}
</style>
