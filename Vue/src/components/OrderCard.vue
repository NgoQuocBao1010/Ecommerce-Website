<template>
    <div class="order-wrapper">
        <div class="header">
            <div class="code">
                #{{ order.id }}
                <span class="date">{{ order.dateCreated }}</span>
            </div>
            <div class="status" :class="order.status">{{ order.status }}</div>
        </div>

        <div class="orders">
            <div class="item" v-for="item in order.cart" :key="item.id">
                <img
                    :src="`${order.domain}${item.thumbnail}`"
                    :alt="item.name"
                />
                <div class="info">
                    <p class="name">{{ item.name }}</p>
                    <p>Color: {{ item.color }}</p>
                    <p>Size: {{ item.size }}</p>
                    <p>
                        Quantity: {{ item.quantity }} X
                        {{ $filters.formatMoneyToVND(item.price) }}.000 VND
                    </p>
                </div>
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
    created() {
        console.log(this.order);
    },
};
</script>

<style lang="scss" scoped>
.order-wrapper {
    width: 90%;
    border-radius: 8px;
    padding: 2rem;
    margin: 3rem auto;
    box-shadow: rgba(0, 0, 0, 0.12) 0px 1px 3px, rgba(0, 0, 0, 0.24) 0px 1px 2px;

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

        .date {
            color: grey;
            font-weight: 500;
            font-size: 1rem;
            padding-left: 1rem;
        }

        .status {
            padding: 0.2rem 1rem;
            display: flex;
            align-items: center;
            justify-content: center;
            border-radius: 1000px;
        }

        .pending {
            color: white;
            background: orange;
        }

        .delivering {
            color: black;
            background: lightgreen;
        }

        .delivered {
            color: white;
            background: grey;
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

        .info {
            p {
                text-transform: capitalize;
                &.name {
                    font-weight: bold;
                }
            }
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

    @media screen and (min-width: 768px) {
        .header {
            .code {
                font-size: 2rem;
            }

            .date {
                font-size: 1.8rem;
            }

            .status {
                font-size: 1.5rem;
            }
        }

        .item {
            .info {
                p {
                    font-size: 2rem;
                    padding: 1rem;
                    &.name {
                        font-weight: bold;
                    }
                }
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
