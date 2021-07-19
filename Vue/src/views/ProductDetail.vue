<template>
    <div class="card-wrapper">
        <div class="card" v-if="exist">
            <!-- card left -->
            <div class="product-imgs">
                <div class="img-display">
                    <div class="img-showcase">
                        <img
                            :src="product.pictures ? product.pictures[0] : '#'"
                            alt="shoe image"
                        />
                    </div>
                </div>
                <div
                    class="img-select"
                    v-show="product.pictures && product.pictures.length > 1"
                >
                    <div
                        class="img-item"
                        v-for="(pic, index) in product.pictures"
                        :key="index"
                        :src="pic"
                    >
                        <a href="#" data-id="1">
                            <img :src="pic" alt="shoe image" />
                        </a>
                    </div>
                </div>
            </div>
            <!-- card right -->
            <div class="product-content">
                <h2 class="product-title">{{ product.name }}</h2>
                <router-link :to="{ name: 'Home' }" class="product-link">
                    visit nike store
                </router-link>
                <div class="product-rating">
                    <i class="fas fa-star"></i>
                    <i class="fas fa-star"></i>
                    <i class="fas fa-star"></i>
                    <i class="fas fa-star"></i>
                    <i class="fas fa-star-half-alt"></i>
                    <span>4.7(21)</span>
                </div>

                <div class="product-price">
                    <p class="last-price">
                        Old Price: <span>1.000.000.000 VND</span>
                    </p>
                    <p class="new-price">
                        New Price: <span>{{ product.price }}.000 VND</span>
                    </p>
                </div>

                <div class="product-detail">
                    <h2>about this item:</h2>
                    <p>
                        Lorem ipsum dolor sit amet consectetur adipisicing elit.
                        Illo eveniet veniam tempora fuga tenetur placeat
                        sapiente architecto illum soluta consequuntur,
                        aspernatur quidem at sequi ipsa!
                    </p>
                    <p>
                        Lorem ipsum dolor sit amet consectetur adipisicing elit.
                        Consequatur, perferendis eius. Dignissimos, labore
                        suscipit. Unde.
                    </p>
                    <ul>
                        <li>
                            Color:
                            <span
                                class="options"
                                :class="chosenColor === color ? 'active' : ''"
                                v-for="(color, index) in colors"
                                :key="index"
                                @click="chosenColor = color"
                            >
                                {{ color }}
                                <i class="fas fa-check"></i>
                            </span>
                        </li>
                        <span
                            v-show="emptyColor"
                            class="errors"
                            style="color: red"
                        >
                            Please pick a color before add to cart
                        </span>

                        <li>
                            Size:
                            <span
                                class="options"
                                :class="chosenSize === size ? 'active' : ''"
                                v-for="(size, index) in sizes"
                                :key="index"
                                @click="chosenSize = size"
                            >
                                {{ size }}
                                <i class="fas fa-check"></i>
                            </span>
                        </li>
                        <span
                            v-show="emptySize"
                            class="errors"
                            style="color: red"
                        >
                            Please pick a size before add to cart
                        </span>
                    </ul>
                </div>

                <div class="purchase-info">
                    <input type="number" min="1" max="5" v-model="quantity" />
                    <button type="button" class="btn" @click="addToCart">
                        Add to Cart <i class="fas fa-shopping-cart"></i>
                    </button>
                </div>

                <div class="social-links">
                    <p>Share At:</p>
                    <a href="#">
                        <i class="fab fa-facebook-f"></i>
                    </a>
                    <a href="#">
                        <i class="fab fa-twitter"></i>
                    </a>
                    <a href="#">
                        <i class="fab fa-instagram"></i>
                    </a>
                    <a href="#">
                        <i class="fab fa-whatsapp"></i>
                    </a>
                    <a href="#">
                        <i class="fab fa-pinterest"></i>
                    </a>
                </div>
            </div>
        </div>
        <h1 v-else>Product does not exist</h1>
    </div>
</template>

<script>
import axios from "axios";
import { mapMutations } from "vuex";

import { createToast } from "mosha-vue-toastify";

export default {
    name: "ProductDetail",
    props: {
        id: String,
    },
    data() {
        return {
            exist: true,
            product: {},
            sizes: [],
            colors: [],

            // Size and color validation
            chosenSize: null,
            chosenColor: null,
            emptySize: false,
            emptyColor: false,

            quantity: 1,
        };
    },
    watch: {
        chosenSize() {
            this.emptySize = false;
        },
        chosenColor() {
            this.emptyColor = false;
        },
    },
    methods: {
        ...mapMutations(["cartUpdate"]),
        getShoeDetail() {
            // http://127.0.0.1:8000/shoe-detail/16
            axios
                .get(`http://127.0.0.1:8000/shoe-detail/${this.id}`)
                .then((response) => {
                    this.product = response.data;
                    console.log(response.data);

                    this.product.items.forEach((item) => {
                        this.colors = [...this.colors, item.itemColor];
                        this.sizes = [...this.sizes, item.itemSize];
                    });

                    this.colors = [...new Set(this.colors)];
                    this.sizes = [...new Set(this.sizes)];

                    this.exist = true;
                })
                .catch((error) => {
                    console.log(error);
                    if (error.response.status === 404) this.exist = false;
                });
        },

        addToCart() {
            this.emptySize = !this.chosenSize ? true : false;
            this.emptyColor = !this.chosenColor ? true : false;

            if (this.emptySize || this.emptyColor) return;

            const itemId = this.product.items.find(
                (item) =>
                    item.itemColor === this.chosenColor &&
                    item.itemSize === this.chosenSize
            ).id;

            const item = {
                id: itemId,
                productId: this.id,
                name: this.product.name,
                size: this.chosenSize,
                color: this.chosenColor,
                thumbnail: this.product.thumbnail,
                price: this.product.price,
                quantity: parseInt(this.quantity),
            };

            this.cartUpdate(item);
            this.$router.push({ name: "Home" });

            createToast("New product is added to cart!", {
                type: "success",
                timeout: 2500,
                position: "bottom-right",
                transition: "bounce",
                hideProgressBar: true,
                showIcon: true,
            });
        },
    },
    mounted() {
        this.getShoeDetail();
    },
};
</script>

<style scoped>
.card-wrapper {
    max-width: 1100px;
    margin: 2rem auto;
    padding: 0 2rem;
}
img {
    width: 100%;
    display: block;
}
.img-display {
    overflow: hidden;
}
.img-showcase {
    display: flex;
    width: 100%;
    transition: all 0.5s ease;
}
.img-showcase img {
    min-width: 100%;
}
.img-select {
    display: flex;
}
.img-item {
    margin: 0.3rem;
}
.img-item:nth-child(1),
.img-item:nth-child(2),
.img-item:nth-child(3) {
    margin-right: 0;
}
.img-item:hover {
    opacity: 0.8;
}

.product-imgs {
    margin-bottom: 3rem;
}

/* Right Side */
.product-content {
    padding: 0 1rem;
    margin-bottom: 2rem;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    max-height: 700px;
}

.product-title {
    font-size: 3rem;
    text-transform: capitalize;
    font-weight: 700;
    position: relative;
    color: #12263a;
    margin: 1rem 0;
}
.product-title::after {
    content: "";
    position: absolute;
    left: 0;
    bottom: 0;
    height: 4px;
    width: 80px;
    background: #12263a;
}

.product-link {
    text-decoration: none;
    text-transform: uppercase;
    font-weight: 400;
    font-size: 1rem;
    display: inline-block;
    margin-bottom: 0.5rem;
    background: #256eff;
    color: #fff;
    width: 30%;
    text-align: center;
    border-radius: 1000px;
    padding: 0.5rem;
    transition: all 0.5s ease;
}
.product-link:hover {
    opacity: 0.9;
}

.product-rating {
    color: #ffc107;
    margin: 2rem 0;
}
.product-rating i {
    font-size: 2.5rem;
}
.product-rating span {
    font-size: 2rem;
    font-weight: 600;
    color: #252525;
    margin-left: 1rem;
}

.product-price {
    margin: 1rem 0;
    font-size: 2rem;
    font-weight: 700;
}
.product-price span {
    font-weight: 400;
}
.last-price span {
    color: #f64749;
    text-decoration: line-through;
}
.new-price span {
    color: #256eff;
}

.product-detail {
    margin: 2rem 0;
}
.product-detail h2 {
    text-transform: capitalize;
    color: #12263a;
    padding-bottom: 0.6rem;
}
.product-detail p {
    font-size: 1.2rem;
    padding: 0.5rem;
    opacity: 0.8;
}
.product-detail ul {
    font-size: 0.9rem;
}
.product-detail ul li {
    margin: 1.4rem 0;
    list-style: none;
    font-size: 1.5rem;
    font-weight: 600;
    opacity: 0.9;
}
.options {
    font-weight: 400;
    margin-left: 0.5rem;
    padding: 0.5rem 0.5rem;
    background: black;
    cursor: pointer;
    color: white;
    border-radius: 10px;
    text-align: center;

    transition: all 0.2s ease;
}

.options i {
    display: none;
}

.product-detail ul li span.active {
    background: var(--primary-color);
    color: black;
}

.product-detail ul li span.active i {
    display: initial;
}

.purchase-info {
    margin: 1.5rem 0;
}
.purchase-info input,
.purchase-info .btn {
    border: 1.5px solid #ddd;
    border-radius: 25px;
    text-align: center;
    padding: 1rem 0.8rem;
    outline: 0;
    margin-right: 1rem;
    margin-bottom: 1rem;
    width: 40%;
    font-family: "Poppins", sans-serif;
}
.purchase-info input {
    width: 30%;
}
.purchase-info .btn {
    cursor: pointer;
    color: #fff;
}
.purchase-info .btn {
    color: black;
    background: var(--primary-color);
}

.purchase-info .btn:hover {
    opacity: 0.9;
}
.social-links {
    display: flex;
    align-items: center;
}
.social-links a {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 32px;
    height: 32px;
    color: #000;
    border: 1px solid #000;
    margin: 0 0.2rem;
    border-radius: 50%;
    text-decoration: none;
    font-size: 1rem;
    transition: all 0.5s ease;
    margin-left: 1rem;
}
.social-links a:hover {
    background: #000;
    border-color: transparent;
    color: #fff;
}

@media screen and (min-width: 992px) {
    .card {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        grid-gap: 5rem;
    }
    .card-wrapper {
        /* height: 100vh; */
        display: flex;
        justify-content: center;
        align-items: center;
    }
    .product-imgs {
        display: flex;
        flex-direction: column;
        justify-content: center;
    }
    .product-content {
        padding-top: 0;
    }
    .options {
        font-weight: 400;
        margin-left: 1rem;
        padding: 0.5rem 2rem;
    }
}
</style>
