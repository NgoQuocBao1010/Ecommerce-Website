import { createRouter, createWebHistory } from "vue-router";
import Home from "../views/Home.vue";
import Product from "../views/Product.vue";
import ProductDetail from "../views/ProductDetail.vue";
import Purchase from "../views/Purchase.vue";
import Account from "../views/Account.vue";
import Login from "../views/Login.vue";
import Register from "../views/Register.vue";
import Contact from "../views/Contact.vue";

const routes = [
    {
        path: "/",
        name: "Home",
        component: Home,
        meta: {
            title: "Home",
        },
    },
    {
        path: "/product",
        name: "Product",
        component: Product,
        meta: {
            title: "Product",
        },
    },
    {
        path: "/product/:id",
        name: "ProductDetail",
        component: ProductDetail,
        props: true,
        meta: {
            title: "Product Detail",
        },
    },
    {
        path: "/purchase",
        name: "Purchase",
        component: Purchase,
        meta: {
            title: "Purchase",
        },
    },
    {
        path: "/account",
        name: "Account",
        component: Account,
        meta: {
            title: "Account",
        },
    },
    {
        path: "/login",
        name: "Login",
        component: Login,
        meta: {
            title: "Login",
        },
    },
    {
        path: "/register",
        name: "Register",
        component: Register,
        meta: {
            title: "Register",
        },
    },
    {
        path: "/contact-us",
        name: "Contact",
        component: Contact,
        meta: {
            title: "Contact",
        },
    },
];

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes,
});

router.beforeEach((to, from, next) => {
    document.title = `${to.meta.title} | Footco`;
    next();
});

export default router;
