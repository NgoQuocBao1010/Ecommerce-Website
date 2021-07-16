<template>
    <div class="dropdown-container">
        <div class="active" @click="toggleMenu">{{ value }}</div>
        <i
            class="fas fa-chevron-down"
            :class="animatedIcon ? 'animated' : ''"
            @click="toggleMenu"
            @animationend="animatedIcon = false"
        ></i>

        <ul class="items" :class="showMenu ? 'active' : ''" ref="items">
            <li
                class="item"
                v-for="(val, index) in dropdown.query"
                :key="index"
                @click="changeValue(val)"
            >
                {{ val }}
            </li>
        </ul>
    </div>
</template>

<script>
import { mapMutations, mapState } from "vuex";

export default {
    name: "Dropdown",
    data() {
        return {
            value: this.dropdown.query[0],
            showMenu: false,
            animatedIcon: false,
        };
    },
    props: {
        dropdown: Object,
    },
    watch: {
        productDropdown(newVal, oldVal) {
            if (oldVal === this.dropdown.field && newVal) this.showMenu = false;
        },
        value(newVal, oldVal) {
            this.$emit("updateValue", newVal);
        },
    },
    computed: {
        ...mapState(["productDropdown"]),
    },
    methods: {
        ...mapMutations(["dropdownToggle"]),
        toggleMenu() {
            this.animatedIcon = true;
            this.showMenu = !this.showMenu;

            if (window.innerWidth < 768) {
                let updateDropdown = this.showMenu ? this.dropdown.field : "";
                this.dropdownToggle(updateDropdown);
            }
        },
        changeValue(newValue) {
            this.value = newValue;
            this.showMenu = false;
        },
    },
};
</script>

<style scoped>
.dropdown-container {
    position: relative;

    width: 90%;
    max-width: 400px;
    min-height: 40px;
    padding: 0 2rem !important;
    border-radius: 1000px;
    background: var(--dark-color);
    display: flex;
    align-items: center;
}

.dropdown-container .active {
    color: white;
    font-size: 1.2rem;
    cursor: pointer;
}

.dropdown-container i {
    color: white;
    margin-left: auto;
    font-size: 2rem;
    cursor: pointer;
}

.dropdown-container i.animated {
    animation: spin 0.3s linear;
}

@keyframes spin {
    100% {
        -webkit-transform: rotate(360deg);
        transform: rotate(360deg);
    }
}

.items {
    position: absolute;
    top: 100%;
    left: 0;
    width: 100%;
    background: var(--dark-color);
    border-radius: 5px;
    opacity: 0;
    pointer-events: none;
    transform: translateY(-10%);
    z-index: 1;
    transition: all 0.5s ease;
}

.items.active {
    opacity: 1;
    pointer-events: all;
    transform: translateY(2%);
}

.item {
    font-size: 1.2rem;
    border: 1px sold var(--dark-color);
    color: white;
    padding: 1rem 4rem;
    cursor: pointer;
    transition: all 0.3s ease;
}

@media only screen and (min-width: 768px) {
    .dropdown-container .active {
        font-size: 2rem;
    }
    .item {
        font-size: 2rem;
        transition: all 0.3s ease;
    }

    .item:hover {
        background: white;
        color: var(--dark-color);
    }
}
</style>
