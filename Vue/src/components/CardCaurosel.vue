<template>
    <div class="wrapper">
        <div class="caurosel-wrapper" ref="caurosel">
            <div class="nav-button prev" @click="prev">
                <i class="fas fa-arrow-right"></i>
            </div>
            <Card
                v-for="shoe in shoes"
                :key="shoe.id"
                :shoe="shoe"
                :gap="gap"
            />
            <div class="nav-button for" @click="forward">
                <i class="fas fa-arrow-right"></i>
            </div>
        </div>
    </div>
</template>

<script>
import { mapState } from "vuex";
import axios from "axios";

import Card from "./Card.vue";

export default {
    name: "CardCaurosel",
    components: {
        Card,
    },
    data() {
        return {
            // carausel attributes
            width: null,
            gap: 0,
            moveLength: 330,
            moveForward: true,
            autoPlay: null,

            shoes: [],
        };
    },
    props: {
        brandName: String,
    },
    computed: {
        maxLength() {
            const itemsWidth = this.shoes.length * this.moveLength;
            return itemsWidth;
        },
        currentRouteName() {
            return this.$route.name;
        },
    },
    watch: {
        currentRouteName(newVal, oldVal) {
            if (newVal !== "Home") {
                clearInterval(this.autoPlay);
                window.removeEventListener("resize", this.resetCaurosel);
            }
        },
    },
    methods: {
        getShoes() {
            axios
                .get(`http://127.0.0.1:8000/shoes/${this.brandName}`)
                .then((response) => {
                    this.shoes = response.data;
                })
                .catch((error) => console.log(error));
        },
        // Carausel methods
        forward() {
            this.width = this.$refs.caurosel.offsetWidth;
            const remainder =
                (this.maxLength - this.width - this.gap) / this.moveLength;

            if (remainder >= 1) {
                this.gap = this.gap + this.moveLength;
            } else {
                const leftOver =
                    (this.maxLength - this.width - this.gap) % this.moveLength;

                if (leftOver > 0) this.gap = this.gap + leftOver;
                else {
                    this.moveForward = false;
                }
            }
        },
        prev() {
            if (this.gap - this.moveLength <= 0) {
                this.gap = 0;
                this.moveForward = true;
                return;
            }
            this.gap = this.gap - this.moveLength;
        },
        resetCaurosel() {
            this.width = this.$refs.caurosel.offsetWidth;
            this.gap = 0;
        },
    },
    mounted() {
        this.width = this.$refs.caurosel.offsetWidth;

        window.addEventListener("resize", this.resetCaurosel);

        this.autoPlay = setInterval(() => {
            if (this.moveForward) this.forward();
            else this.prev();
        }, 3000);
    },
    created() {
        this.getShoes();
    },
};
</script>

<style scoped>
.wrapper {
    position: relative;
    max-width: 100%;

    display: flex;
    justify-content: center;
    align-items: center;
}

.caurosel-wrapper {
    max-width: 90%;
    padding: 1rem 2rem;

    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 30px;

    overflow: hidden;
}

.nav-button {
    position: absolute;

    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    z-index: 999;
}

.nav-button i {
    font-size: 2rem;
    color: var(--secondary-color);
}

.prev {
    left: 2%;
    transform: translateX(-50%);
}

.prev i {
    transform: rotate(180deg);
}

.for {
    right: 2%;
    transform: translateX(50%);
}

@media only screen and (min-width: 820px) {
    .wrapper {
        max-width: 90%;
        padding: 1rem 5rem;
    }
    .nav-button i {
        font-size: 3rem;
    }
}

@media only screen and (min-width: 1740px) {
    .caurosel-wrapper {
        max-width: 1500px;
    }
}
</style>
