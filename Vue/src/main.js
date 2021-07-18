import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";

const app = createApp(App);
app.config.globalProperties.$filters = {
    formatMoneyToVND(value) {
        return value.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ".");
    },
};

app.use(store)
    .use(router)
    .mount("#app");
