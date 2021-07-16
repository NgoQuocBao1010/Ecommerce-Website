<template>
    <section>
        <!-- Addidas -->
        <h2 class="title">Adidas</h2>
        <CardCaurosel :shoes="addidasBrands" />

        <!-- Nike -->
        <h2 class="title">Converse</h2>
        <CardCaurosel :shoes="converseBrands" />
    </section>
</template>

<script>
import { mapState } from "vuex";

import Welcome from "../components/Welcome.vue";
import Card from "../components/Card.vue";
import CardCaurosel from "../components/CardCaurosel.vue";

export default {
    name: "Home",
    components: {
        Welcome,
        Card,
        CardCaurosel,
    },
    data() {
        return {};
    },
    computed: {
        ...mapState(["shoes"]),
        addidasBrands() {
            return this.shoes.filter((item) => {
                return item.brand === "Adidas";
            });
        },
        converseBrands() {
            return this.shoes.filter((item) => {
                return item.brand === "Converse";
            });
        },
    },
};
</script>

<style scoped>
section {
    padding: 0 20px;
    max-width: 100%;
    min-width: 100%;

    text-align: center;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
}

.title {
    font-size: 4rem;
    margin: 2rem;
}
</style>
