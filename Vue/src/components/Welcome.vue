<template>
    <section class="welcome">
        <h3>Welcom to</h3>

        <div>
            <span style="--i: 1">f</span>
            <span style="--i: 2">o</span>
            <span style="--i: 3">o</span>
            <span style="--i: 4">t</span>
            <span style="--i: 5">c</span>
            <span style="--i: 6">o</span>
        </div>
    </section>
</template>

<script>
export default {
    name: "Welcome",
};
</script>

<style scoped>
section {
    width: 100%;
    height: 25vh;
    background-image: url("../assets/background3.jpg");
    background-size: cover;
    background-position: 0 -15%;

    display: flex;
    align-items: center;
    justify-content: center;
}

h3 {
    transform: translateY(70%);
    font-size: 2rem;
    font-weight: bold;
    color: #fff;
}

div {
    transform: translateY(60%);
}

span {
    font-family: "Comfortaa", cursive;
    font-size: 3.1rem;
    font-weight: bold;
    letter-spacing: 7px;
    color: var(--primary-color);

    display: inline-block;
    /* text-transform: uppercase; */
    animation: flip 2s infinite;
    animation-delay: calc(0.2s * var(--i));
}

span:nth-child(1) {
    margin-left: 20px;
}

@keyframes flip {
    0%,
    80% {
        transform: rotateY(360deg);
    }
}

@media only screen and (min-width: 420px) {
    section {
        height: 60vh;
        background-position: 0 -15%;

        flex-direction: column;
    }

    h3 {
        font-size: 4rem;
        margin-bottom: 2rem;
    }

    span {
        font-size: 8rem;
    }
}

@media only screen and (min-width: 700px) {
    section {
        height: 60vh;
        background-size: cover;
        background-position: center;

        flex-direction: column;
    }

    h3 {
        font-size: 5rem;
        margin-bottom: 3rem;
    }

    span {
        font-size: 10rem;
    }

    div {
        transform: translateY(30%);
    }
}
</style>
