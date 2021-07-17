<template>
    <section>
        <!-- Addidas -->
        <h2 class="title">Adidas</h2>
        <CardCaurosel brandName="adidas" />

        <!-- Nike -->
        <h2 class="title">Nike</h2>
        <CardCaurosel brandName="nike" />
    </section>
</template>

<script>
import axios from "axios";
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
        return {
            nikeShoes: [],
            adidasShoes: [],
        };
    },
    methods: {
        getShoesByBrand(brand) {
            let data = [];
            axios
                .get(`http://127.0.0.1:8000/shoes/${brand}`)
                .then((response) => {
                    console.log(response.data);
                    data = response.data;
                })
                .catch((error) => console.log(error));

            return data;
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
