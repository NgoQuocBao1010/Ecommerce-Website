<template>
    <div class="modal-container" v-if="visible">
        <div class="modal">
            <div class="modal__title">
                <h2 class="logo">footco</h2>
            </div>
            <div class="modal__info">
                <p>You need to login to view this page</p>
                <a href="#">Login</a>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "LoginModal",
    data() {
        return {
            visible: false,
        };
    },
};
</script>

<style lang="scss" scoped>
.modal-container {
    position: fixed;
    z-index: 9998;
    top: 0;
    left: 0;
    width: 100%;
    min-height: 100vh;
    max-height: 100vh;
    background-color: rgba(0, 0, 0, 0.4);
    display: flex;
    justify-content: center;
    align-items: center;
    transition: opacity 0.3s ease;

    .modal {
        padding: 2rem;
        width: 80%;
        min-width: 250px;
        max-width: 400px;
        border-radius: 30px;
        aspect-ratio: 1 / 1;
        background: black;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        align-items: center;

        * {
            color: white;
        }

        &__title {
            width: 100%;
            text-align: center;

            h2 {
                color: var(--primary-color);
                font-size: 5rem;
            }
        }

        &__info {
            text-align: center;
            min-height: 70%;
            margin-top: 2rem;
            padding: 2rem;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            align-items: center;

            p {
                font-size: 1.5rem;
            }

            a {
                color: var(--primary-color);
                background-color: black;
                padding: 0.5rem 2rem;
                border: 2px solid var(--primary-color);
                border-radius: 1000px;
                font-size: 1.8rem;
                font-weight: 500;
                cursor: pointer;
                text-decoration: none;
            }
        }
    }

    @media only screen and (min-width: 1200px) {
        .modal a {
            transition: all 0.2s ease-in;
        }

        .modal a:hover {
            background-color: var(--primary-color);
            color: black;
        }
    }
}
</style>
