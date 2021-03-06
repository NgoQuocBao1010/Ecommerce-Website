<template>
    <div class="product">
        <div class="filter-container">
            <h1>Products</h1>
            <div class="filter">
                <select name="brands" v-model="brand">
                    <option value="">All Brands</option>
                    <option value="nike">Nike</option>
                    <option value="adidas">Adidas</option>
                    <option value="converse">Converse</option>
                    <option value="others">Others</option>
                </select>

                <select name="brands" v-model="feature">
                    <option value="">Newest</option>
                    <option value="best-seller">Best sellers</option>
                    <option value="on-sales">On sales</option>
                </select>

                <select name="brands" v-model="sort">
                    <option value="">Sort</option>
                    <option value="a-z">Letters: A to Z</option>
                    <option value="z-a">Letters: Z to A</option>
                    <option value="hight2low">Price: Highest to Lowest</option>
                    <option value="low2high">Price: Lowest to Highest</option>
                </select>
            </div>
        </div>
        <div class="tags" v-show="productName || brand || feature || sort">
            <h1>
                You are looking for
                <span v-show="productName">
                    {{ productName }}
                    <i class="fas fa-times" @click="productName = ''"></i>
                </span>
                <span v-show="brand">
                    {{ brand }}
                    <i class="fas fa-times" @click="brand = ''"></i>
                </span>
                <span v-show="feature">
                    {{ feature }}
                    <i class="fas fa-times" @click="feature = ''"></i>
                </span>
                <span v-show="sort">
                    {{ sort }}
                    <i class="fas fa-times" @click="sort = ''"></i>
                </span>
            </h1>
        </div>
        <div class="product-container">
            <Card v-for="shoe in shoes" :key="shoe.id" :shoe="shoe" />
        </div>
    </div>
</template>

<script>
import axios from "axios";
import { mapState } from "vuex";

import Card from "../components/Card.vue";

export default {
    name: "Product",
    components: {
        Card,
    },
    data() {
        return {
            shoes: [],
            brand: "",
            feature: "",
            sort: "",
            productName: "",
            value: "",
        };
    },
    watch: {
        productName() {
            this.updateQueryString();
        },
        brand() {
            this.updateQueryString();
        },
        feature() {
            this.updateQueryString();
        },
        sort() {
            this.updateQueryString();
        },
        $route(to, from) {
            if (to.name === "Product") {
                this.productName = this.$route.query.productName || "";
                this.getAllShoes();
            }
        },
    },
    methods: {
        getAllShoes() {
            this.brand = this.brand || "";
            this.feature = this.feature || "";
            this.sort = this.sort || "";

            const url = `http://127.0.0.1:8000/all-shoes/?productName=${this.productName}&brand=${this.brand}&feature=${this.feature}&sort=${this.sort}`;

            axios
                .get(url)
                .then((response) => {
                    this.shoes = response.data;
                })
                .catch((error) => console.log(error));
        },
        updateQueryString() {
            const data = {
                productName: this.productName,
                brand: this.brand,
                feature: this.feature,
                sort: this.sort,
            };
            this.$router.push({
                query: data,
            });
        },
    },
    created() {
        const queryString = this.$route.query;

        if (
            !(Object.keys(queryString).length === 0) ||
            !(queryString.constructor === Object)
        ) {
            ({
                productName: this.productName,
                brand: this.brand,
                feature: this.feature,
                sort: this.sort,
            } = this.$route.query);
        }
        this.getAllShoes();
    },
};
</script>

<style scoped>
.product {
    --select-border: #777;
    --select-focus: blue;
    --select-arrow: var(--select-border);
    width: 100%;
}

.filter-container {
    box-shadow: rgba(0, 0, 0, 0.35) 0px 5px 15px;
}

.filter-container * {
    margin: 0;
    padding: 0;
}

.filter-container h1,
.filter-container .filter {
    width: 100%;
    text-align: center;
    padding: 0.5rem;
    font-size: 4rem;
}

.filter {
    display: flex;
    flex-direction: column;
    align-items: center;
}

.filter > * {
    margin-bottom: 10px;
}

select {
    min-width: 15ch;
    max-width: 30ch;
    border: 1px solid var(--select-border);
    border-radius: 0.25em;
    padding: 0.5em 0.5em !important;
    font-size: 1.5rem;
    cursor: pointer;
    line-height: 1.4;
    background-color: #fff;
    background-image: linear-gradient(to top, #f9f9f9, #fff 33%);
}

select::-ms-expand {
    display: none;
}

select option {
    font-size: 1.5rem;
    max-width: 100px !important;
    min-height: 20px !important;
    max-height: 20px !important;
    padding: 1rem !important;
    margin: 0 !important;
}

.tags {
    width: 100%;
    padding: 2rem;
    margin-top: 2rem;
    line-height: 2;

    font-size: 0.8rem;

    display: flex;
    justify-content: center;
    align-items: center;
}

.tags h1 {
    width: 80%;
    font-weight: 500;
}

.tags i {
    color: #fff;
    font-weight: bold;
    cursor: pointer;
}

.tags span {
    margin-left: 1rem;
    padding: 0.5rem;
    background: var(--primary-color);
}

.tags-enter-active,
.tags-leave-active {
    transition: all 0.2s ease;
}
.tags-enter-from,
.tags-leave-to {
    opacity: 0;
    transform: translateY(30px);
}

.product-container {
    padding: 2rem;
    margin: 2rem auto;
    display: flex;
    justify-content: center;
    align-items: center;
    flex-wrap: wrap;
    gap: 4rem;
}

@media only screen and (min-width: 768px) {
    .filter {
        display: flex;
        flex-direction: row;
        justify-content: space-around;
        padding: 2rem !important;
        gap: 2rem;
    }

    .tags {
        font-size: 1rem;
    }

    .product-container {
        max-width: 1410px;
    }
}
</style>
