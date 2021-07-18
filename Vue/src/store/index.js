import { createStore } from "vuex";

import axios from "axios";

export default createStore({
    state: {
        user: null,
        token: null,
        authenticated: false,
        cart: [],
        orders: [
            {
                address: "đường B19, KDC Hưng Phú 1, Cái Răng",
                name: "Ngô Hồng Quốc Bảo",
                note: "",
                phone: "0939983979",
                cart: [
                    {
                        id: "1-35-orange",
                        productId: 1,
                        name: "Adizero Boston 10",
                        thumbnail: require("../assets/shoes/shoes-1.jpg"),
                        size: 35,
                        color: "orange",
                        quantity: 1,
                    },
                    {
                        id: "7-35-white",
                        productId: 7,
                        name: "Fear of Gods",
                        thumbnail: require("../assets/shoes/converse-3.jpg"),
                        size: 35,
                        color: "white",
                        quantity: 3,
                    },
                ],
                price: 5400,
            },
            {
                address: "đường B19, KDC Hưng Phú 1, Cái Răng",
                name: "Ngô Hồng Quốc Bảo",
                note: "",
                phone: "0939983979",
                cart: [
                    {
                        id: "1-35-orange",
                        productId: 1,
                        name: "Adizero Boston 10",
                        thumbnail: require("../assets/shoes/shoes-1.jpg"),
                        size: 35,
                        color: "orange",
                        quantity: 1,
                    },
                ],
                price: 1400,
            },
        ],
    },
    mutations: {
        authenticate(state, token) {
            state.token = token;
            state.authenticated = true;
            axios.defaults.headers.common["Authorization"] = `Token ${token}`;
            localStorage.setItem("authToken", token);

            console.log("Authenticated!!!!!");
        },
        getUserProfile(state, profile) {
            state.user = profile;
        },
        logout(state) {
            state.user = null;
            state.token = null;
            state.authenticated = false;
            axios.defaults.headers.common["Authorization"] = "";
            localStorage.setItem("authToken", "");
        },
        cartUpdate(state, newItem) {
            const existItem = state.cart.find((item) => item.id === newItem.id);

            if (existItem) existItem.quantity += parseInt(newItem.quantity);
            else state.cart = [newItem, ...state.cart];

            localStorage.setItem("cart", JSON.stringify(state.cart));
        },
        quantityUpdate(state, newValue) {
            const { id, quantity } = newValue;

            const updateItem = state.cart.find((item) => item.id === id);

            updateItem.quantity = parseInt(quantity);
        },
        removeItemInCart(state, deleteItemId) {
            state.cart = state.cart.filter((item) => item.id !== deleteItemId);
            localStorage.setItem("cart", JSON.stringify(state.cart));
        },
        clearCart(state) {
            state.cart = [];
            localStorage.clear();
        },
    },
    getters: {
        getCartLength: (state) => {
            let numOfItems = 0;
            state.cart.forEach((order) => {
                numOfItems += order.quantity;
            });

            return numOfItems;
        },
    },
    actions: {
        logginIn(context, token) {
            context.commit("authenticate", token);

            axios
                .get("http://127.0.0.1:8000/api/profile")
                .then((response) => {
                    context.commit("getUserProfile", response.data);
                })
                .catch((error) => {
                    if (error.response.status === 401)
                        console.log(
                            "You are not allowed to view this information"
                        );
                });
        },
    },
    modules: {},
});
