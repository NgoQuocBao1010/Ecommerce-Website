<template>
    <div class="card" ref="card">
        <img
            :src="shoe.thumbnail"
            alt="shoe.name"
            style="width: 100%; aspect-ratio: 1/1;"
            ref="thumbnail"
        />
        <div class="info">
            <h1>{{ shoe.name }}</h1>
            <p class="price">{{ shoe.price }}.000 VND</p>
            <p>
                <router-link
                    :to="{ name: 'ProductDetail', params: { id: shoe.id } }"
                >
                    View Detail
                </router-link>
            </p>
        </div>
    </div>
</template>

<script>
export default {
    name: "Card",
    props: {
        shoe: Object,
        gap: {
            type: Number,
            required: false,
        },
    },
    watch: {
        gap(newVal, oldVal) {
            this.move(newVal);
        },
    },
    methods: {
        move(gap) {
            gap = -gap;
            this.$refs.card.style = `transform: translateX(${gap}px);`;
            // console.log("Move right");
        },
    },
};
</script>

<style scoped>
.card {
    box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
    max-width: 300px;
    min-width: 300px;
    height: 420px;
    margin-bottom: 20px;

    display: flex;
    flex-direction: column;
    justify-content: space-between;

    transition: all 0.5s ease;
}

.card * {
    font-family: "Poppins", sans-serif;
}

.info {
    display: flex;
    flex-direction: column;
    justify-content: space-between;

    text-align: center;
}

.info h1 {
    font-size: 20px;
}

.price {
    color: grey;
    font-size: 16px;
}

/* button {
    border: none;
    outline: 0;
    padding: 12px;
    background-color: black;
    text-align: center;
    cursor: pointer;
    width: 100%;
    font-size: 18px;

    transition: all 0.3s ease;
} */

a {
    display: block;
    text-decoration: none;
    color: var(--primary-color);
    background-color: black;
    width: 100%;
    font-size: 18px;
    padding: 1rem 0.2rem;
    transition: all 0.3s ease;
}

a:hover {
    background-color: var(--primary-color);
    color: black;
}
</style>
