<template>
    <header class="header">
        <nav class="navbar">
            <router-link class="nav-logo" :to="{ name: 'Home' }">
                footco
            </router-link>
            <ul class="nav-menu" :class="navMobile ? 'active' : ''">
                <li
                    v-for="(link, index) in menuLinks"
                    :key="index"
                    class="nav-item"
                    :class="link === currentRouteName ? 'active' : ''"
                >
                    <router-link class="nav-link" :to="{ name: link }">
                        {{ link }}
                    </router-link>
                </li>
            </ul>

            <!-- Search bar -->
            <div class="search-bar">
                <form onsubmit="event.preventDefault();" role="search">
                    <label for="search">Search for stuff</label>
                    <input
                        id="search"
                        type="search"
                        placeholder="Search..."
                        autofocus
                        required
                    />
                    <button type="submit">Go</button>
                </form>
                <i class="fas fa-shopping-cart" @click="goToCart">
                    <span>{{ orders }}</span>
                </i>
            </div>

            <!-- Menu Phone Icon -->
            <div
                class="hamburger"
                :class="navMobile ? 'active' : ''"
                @click="navMobile = !navMobile"
            >
                <span class="bar"></span>
                <span class="bar"></span>
                <span class="bar"></span>
            </div>
        </nav>
    </header>
</template>

<script>
export default {
    name: "Navigation",
    data() {
        return {
            navMobile: false,
            currentRoute: null,
            menuLinks: ["Home", "Product", "Account", "Contact"],
        };
    },
    computed: {
        currentRouteName() {
            return this.$route.name;
        },
        orders() {
            return this.$store.getters.getCartLength;
        },
    },
    watch: {
        currentRouteName(newVal, oldVal) {
            this.navMobile = false;
        },
    },
    methods: {
        goToCart() {
            this.$router.push({ name: "Purchase" });
        },
    },
};
</script>

<style lang="scss" scoped>
.header {
    background-color: black;
    border-bottom: 1px solid #171718;
    position: fixed;
    z-index: 1000;
    width: 100%;
}

.navbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 1rem 4rem;
}

.hamburger {
    display: none;
}

.bar {
    display: block;
    width: 25px;
    height: 3px;
    margin: 5px auto;
    -webkit-transition: all 0.3s ease-in-out;
    transition: all 0.3s ease-in-out;
    background-color: #fff;
}

.nav-menu {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.nav-item {
    margin-left: 5rem;
}

.nav-item.active a {
    color: var(--primary-color);
}

.nav-link {
    font-size: 1.6rem;
    font-weight: 400;
    color: #fff;
}

.nav-link:hover {
    color: var(--primary-color);
}

.nav-logo {
    font-family: "Comfortaa", cursive;
    font-size: 3.1rem;
    font-weight: bold;
    letter-spacing: 7px;
    color: var(--primary-color);
}

// SEARCH BAR
.search-bar {
    --rad: 0.7rem;
    --dur: 0.3s;
    --color-dark: #2f2f2f;
    --color-light: #fff;
    --height: 4rem;
    --btn-width: 6rem;
    --bez: cubic-bezier(0, 0, 0.43, 1.49);
    display: flex;
    flex-direction: row;
    align-items: center;
}

// Cart
.search-bar i {
    position: relative;
    color: white;
    font-size: 20px;
    margin-left: 2rem;
    cursor: pointer;
}

.search-bar i span {
    position: absolute;
    font-family: "Poppins", sans-serif;
    font-size: 1.2rem;
    font-weight: bold;
    top: 0;
    right: -15px;
    color: var(--primary-color);
}

// Search form
form {
    position: relative;
    width: 30rem;
    background: var(--primary-color);
    border-radius: var(--rad);
}
input,
button {
    height: var(--height);
    font-family: "Poppins", sans-serif;
    border: 0;
    color: var(--color-dark);
    font-size: 1.5rem;
}
input[type="search"] {
    outline: 0;
    width: 100%;
    background: var(--color-light);
    padding: 0 1.6rem;
    border-radius: var(--rad);
    appearance: none;
    transition: all var(--dur) var(--bez);
    transition-property: width, border-radius;
    z-index: 1;
    position: relative;
}
button {
    display: none;
    position: absolute;
    top: 0;
    right: 0;
    width: var(--btn-width);
    font-weight: bold;
    background: var(--primary-color);
    border-radius: 0 var(--rad) var(--rad) 0;
    cursor: pointer;
}
input:not(:placeholder-shown) {
    border-radius: var(--rad) 0 0 var(--rad);
    width: calc(100% - var(--btn-width));
    + button {
        display: block;
    }
}
label {
    position: absolute;
    clip: rect(1px, 1px, 1px, 1px);
    padding: 0;
    border: 0;
    height: 1px;
    width: 1px;
    overflow: hidden;
}

@media only screen and (max-width: 1200px) {
    .search-bar form {
        width: 15rem;
    }

    .search-bar i {
        display: none;
    }
}

@media only screen and (max-width: 768px) {
    .nav-menu {
        position: fixed;
        left: -100%;
        top: 5rem;
        flex-direction: column;
        background-color: black;
        width: 100%;
        border-radius: 10px;
        text-align: center;
        transition: 0.3s;
        box-shadow: 0 10px 27px rgba(0, 0, 0, 0.05);
    }
    .nav-logo {
        font-size: 2rem;
    }

    .nav-menu.active {
        left: 0;
    }

    .nav-item {
        margin: 2.5rem 0;
    }

    .hamburger {
        display: block;
        cursor: pointer;
    }

    .hamburger.active .bar:nth-child(2) {
        opacity: 0;
    }

    .hamburger.active .bar:nth-child(1) {
        transform: translateY(8px) rotate(45deg);
    }

    .hamburger.active .bar:nth-child(3) {
        transform: translateY(-8px) rotate(-45deg);
    }
    form {
        display: none;
    }
}
</style>
