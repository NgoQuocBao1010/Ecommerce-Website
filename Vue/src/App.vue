<template>
    <div class="app">
        <LoginModal v-show="showNav" />
        <ResponsiveNav v-show="showNav" />
        <Welcome v-show="$route.name === 'Home'" />
        <div class="container">
            <router-view v-slot="{ Component }">
                <transition
                    :name="
                        $route.name === 'Login' || $route.name === 'Register'
                            ? ''
                            : 'fade'
                    "
                    mode="out-in"
                >
                    <component :is="Component" />
                </transition>
            </router-view>
        </div>
        <Footer v-show="showNav" />
    </div>
</template>

<script>
import Navigation from "./components/Navigation.vue";
import ResponsiveNav from "./components/ResponsiveNav.vue";
import Footer from "./components/Footer.vue";
import Welcome from "./components/Welcome.vue";
import LoginModal from "./components/LoginModal.vue";

import "mosha-vue-toastify/dist/style.css";

export default {
    components: {
        Navigation,
        ResponsiveNav,
        Footer,
        Welcome,
        LoginModal,
    },
    data() {
        return {
            showNav: true,
        };
    },
    watch: {
        $route(to, from) {
            if ((to.name === "Login") | (to.name === "Register"))
                this.showNav = false;
            else this.showNav = true;
        },
    },
    created() {
        // localStorage.clear();
        this.showNav =
            (this.showNav.name === "Login") | (this.showNav.name === "Register")
                ? (this.showNav = false)
                : (this.showNav = true);

        const cart = JSON.parse(localStorage.getItem("cart"));
        const token = localStorage.getItem("authToken");

        if (cart) {
            cart.forEach((order) => {
                this.$store.commit("cartUpdate", order);
            });
        }

        if (token) {
            this.$store.dispatch("logginIn", token);
        }
    },
};
</script>

<style lang="scss">
@import url("https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;800&display=swap");
@import url("https://fonts.googleapis.com/css2?family=Comfortaa:wght@400;500;700&display=swap");

:root {
    --primary-color: #f8b2cd;
    --secondary-color: #b6c9f0;
    --dark-color: #362222;
    --white: #ffffff;
}

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: "Poppins", sans-serif;
}

html {
    font-size: 62.5%;
}

li {
    list-style: none;
}

a {
    text-decoration: none;
}

.app {
    display: flex;
    min-height: 100vh;
    flex-direction: column;
}
.container {
    margin-top: 84px;
    flex: 1;
    display: flex;
}
.fade-enter-active,
.fade-leave-active {
    transition: opacity 0.2s ease;
}

.fade-enter-from,
.fade-leave-to {
    opacity: 0;
}

.logo {
    font-family: "Comfortaa", cursive;
    font-size: 3.1rem;
    font-weight: bold;
    letter-spacing: 7px;
    color: var(--primary-color);
}

// Notifications
.mosha__toast__content {
    font-family: "Poppins", sans-serif !important;
}
.mosha__toast__content__text {
    font-weight: 400 !important;
}
.mosha__toast.success {
    background-color: var(--primary-color);
}
.mosha__toast.success .mosha__toast__content__text {
    color: black !important;
}
</style>
