<template>
    <header class="header">
        <nav>
            <router-link class="nav-logo" :to="{ name: 'Home' }">
                footco
            </router-link>

            <ul class="nav-menu" v-show="!mobile">
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

            <div class="search-bar" v-show="!mobile">
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
                <router-link :to="{ name: 'Account' }">
                    <i class="fas fa-user"></i>
                </router-link>
                <i class="fas fa-shopping-cart" @click="goToCart">
                    <span>{{ orders }}</span>
                </i>
            </div>

            <!-- Mobile Nav -->
            <div class="utils" v-show="mobile">
                <router-link :to="{ name: 'Account' }">
                    <i class="fas fa-user"></i>
                </router-link>
                <div
                    class="hamburger"
                    :class="{ active: mobileNav }"
                    @click="toggleMobileNav"
                >
                    <div class="bar"></div>
                    <div class="bar"></div>
                    <div class="bar"></div>
                </div>
            </div>

            <transition name="mobile-nav">
                <ul class="dropdown-nav" v-show="mobileNav">
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
                    <li
                        class="nav-item"
                        :class="currentRouteName === 'Purchase' ? 'active' : ''"
                    >
                        <router-link
                            class="nav-link"
                            :to="{ name: 'Purchase' }"
                        >
                            Shopping Cart
                        </router-link>
                    </li>
                </ul>
            </transition>
        </nav>
    </header>
</template>

<script>
export default {
    name: "ResponsiveNav",
    data() {
        return {
            currentRoute: null,
            menuLinks: ["Home", "Product", "Contact"],

            scrollPosition: null,
            mobile: true,
            mobileNav: null,
            windowWidth: null,
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
            this.mobileNav = false;
        },
    },
    methods: {
        toggleMobileNav() {
            this.mobileNav = !this.mobileNav;
        },
        goToCart() {
            this.$router.push({ name: "Purchase" });
        },
        checkScreen() {
            this.windowWidth = window.innerWidth;

            if (this.windowWidth < 750) {
                this.mobile = true;
                return;
            }

            this.mobile = false;
            this.mobileNav = false;
            return;
        },
    },
    created() {
        window.addEventListener("resize", this.checkScreen);
        this.checkScreen();
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

    nav {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 2rem;

        .nav-logo {
            font-family: "Comfortaa", cursive;
            font-size: 3rem;
            font-weight: bold;
            letter-spacing: 7px;
            color: var(--primary-color);
        }

        .nav-menu {
            display: flex;
            justify-content: space-between;
            align-items: center;

            .nav-item {
                margin-left: 4rem;
            }
        }

        .nav-item.active a {
            color: var(--primary-color);
        }

        .nav-link {
            font-size: 1.6rem;
            font-weight: 400;
            color: #fff;
        }

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

            form {
                display: none;
            }

            i {
                position: relative;
                color: white;
                font-size: 20px;
                margin-left: 2rem;
                cursor: pointer;

                span {
                    position: absolute;
                    font-family: "Poppins", sans-serif;
                    font-size: 1.2rem;
                    font-weight: bold;
                    top: 0;
                    right: -1.2rem;
                    color: var(--primary-color);
                }
            }

            @media only screen and (min-width: 1200px) {
                form {
                    display: initial;
                    position: relative;
                    width: 20rem;
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
            }
        }

        .utils {
            display: flex;
            align-items: center;
            gap: 3rem;

            .hamburger {
                .bar {
                    display: block;
                    width: 25px;
                    height: 3px;
                    margin: 5px auto;
                    -webkit-transition: all 0.3s ease-in-out;
                    transition: all 0.4s ease-in-out;
                    background-color: #fff;
                }
                &.active .bar:nth-child(2) {
                    opacity: 0;
                }

                &.active .bar:nth-child(1) {
                    transform: translateY(8px) rotate(45deg);
                }

                &.active .bar:nth-child(3) {
                    transform: translateY(-8px) rotate(-45deg);
                }
            }

            i.fa-user {
                font-size: 2rem;
                color: white;
            }
        }

        .dropdown-nav {
            display: flex;
            flex-direction: column;
            position: fixed;
            width: 100%;
            max-width: 250px;
            height: 100%;
            padding-top: 2rem;
            background-color: black;
            top: 0;
            left: 0;

            .nav-item {
                padding: 1rem 2rem;

                .nav-link {
                    padding: 0 3rem;
                }
            }
        }

        .mobile-nav-enter-active,
        .mobile-nav-leave-active {
            transition: all 0.5s ease;
        }

        .mobile-nav-enter-from,
        .mobile-nav-leave-to {
            transform: translateX(-250px);
        }

        .mobile-nav-enter-to {
            transform: translateX(0);
        }
    }

    @media only screen and (min-width: 768px) {
        nav {
            padding: 2rem 4rem !important;

            .nav-logo {
                font-size: 4rem !important;
            }
        }
    }
}
</style>
