import { createStore } from "vuex";

export default createStore({
    state: {
        user: null,
        authenticated: true,
        shoes: [
            {
                id: 1,
                name: "Adizero Boston 10",
                brand: "Adidas",
                price: 200,
                thumbnail: require("../assets/shoes/shoes-1.jpg"),
                dateAdded: new Date("July 08, 2021 12:00:00"),
            },
            {
                id: 2,
                name: "Futurecraft 3D shoes",
                brand: "Adidas",
                price: 800,
                thumbnail: require("../assets/shoes/shoes-2.jpg"),
                dateAdded: new Date("July 07, 2021 12:00:00"),
            },
            {
                id: 3,
                name: "ZK 2K Boost 2.0",
                brand: "Adidas",
                price: 400,
                thumbnail: require("../assets/shoes/shoes-3.jpg"),
                dateAdded: new Date("May 09, 2021 12:00:00"),
            },
            {
                id: 4,
                name: "Male Multi Court Tennis",
                brand: "Adidas",
                price: 500,
                thumbnail: require("../assets/shoes/shoes-4.jpg"),
                dateAdded: new Date("July 05, 2021 12:00:00"),
            },
            {
                id: 5,
                name: "Converse Classic",
                brand: "Converse",
                price: 500,
                thumbnail: require("../assets/shoes/converse-1.jpg"),
                dateAdded: new Date("July 09, 2019 12:00:00"),
            },
            {
                id: 6,
                name: "Converse 70s",
                brand: "Converse",
                price: 200,
                thumbnail: require("../assets/shoes/converse-2.jpg"),
                dateAdded: new Date("December 09, 2020 12:00:00"),
            },
            {
                id: 7,
                name: "Fear of Gods",
                brand: "Converse",
                price: 1500,
                thumbnail: require("../assets/shoes/converse-3.jpg"),
                dateAdded: new Date("November 01, 2020 12:00:00"),
            },
            {
                id: 8,
                name: "Chuck Taylor",
                brand: "Converse",
                price: 2500,
                thumbnail: require("../assets/shoes/converse-4.jpg"),
                dateAdded: new Date("June 09, 2021 12:00:00"),
            },
            {
                id: 9,
                name: "One star",
                brand: "Converse",
                price: 100,
                thumbnail: require("../assets/shoes/converse-5.jpg"),
                dateAdded: new Date("July 08, 2021 03:00:00"),
            },
        ],
        productDropdown: "",
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
        authenticate(state, loginInfo) {
            const { username, password } = loginInfo;
            console.log(`Logging in ${username}, ${password}`);

            state.user = loginInfo;
            state.authenticated = true;
        },
        logout(state) {
            state.user = null;
            state.authenticated = false;
        },
        dropdownToggle(state, status) {
            state.productDropdown = status;
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
        getShoeByID: (state) => (id) => {
            return state.shoes.find((song) => song.id === id);
        },
        getCartLength: (state) => {
            let numOfItems = 0;
            state.cart.forEach((order) => {
                numOfItems += order.quantity;
            });

            return numOfItems;
        },
    },
    actions: {},
    modules: {},
});
