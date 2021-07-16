<template>
    <footer>
        <!-- Footer main -->
        <section class="ft-main">
            <div class="ft-main-item">
                <h2 class="ft-title">About</h2>
                <ul>
                    <li><a href="#">Services</a></li>
                    <li><a href="#">Portfolio</a></li>
                    <li><a href="#">Pricing</a></li>
                </ul>
            </div>
            <div class="ft-main-item">
                <h2 class="ft-title">Contact</h2>
                <ul class="social">
                    <li>
                        <a href="#"><i class="fab fa-facebook"></i></a>
                    </li>
                    <li>
                        <a href="#"><i class="fab fa-instagram"></i></a>
                    </li>
                    <li>
                        <a href="#"><i class="fab fa-github"></i></a>
                    </li>
                </ul>
            </div>
            <div class="ft-main-item">
                <h2 class="ft-title">Stay Updated</h2>
                <p>Subscribe to our newsletter to get our latest news.</p>
                <form>
                    <input
                        type="email"
                        name="email"
                        placeholder="Enter email address"
                    />
                    <input type="submit" value="Subscribe" />
                </form>
            </div>
        </section>
    </footer>
</template>

<script>
export default {
    name: "Footer",
};
</script>

<style scoped>
ul {
    list-style: none;
    padding-left: 0;
}
footer {
    background-color: black;
    color: #bbb;
    line-height: 1.5;
}
footer a {
    text-decoration: none;
    color: #eee;

    transition: all 0.2s ease;
}
a:hover {
    text-decoration: underline;
    color: var(--primary-color) !important;
}
.ft-title {
    color: var(--primary-color) !important;
    font-size: 1.5rem;
    padding-bottom: 0.625rem;
}
.ft-main {
    padding: 1.25rem 1.875rem;
    display: flex;
    flex-wrap: wrap;
}
.ft-main-item {
    padding: 1.25rem;
    min-width: 12.5rem /*200px*/;
}

.ft-main-item li {
    font-size: 1.25rem;
}

.social {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin: 1.2rem 0;
}

.social li {
    font-size: 2rem;
}

@media only screen and (min-width: 29.8125rem /*477px*/) {
    .ft-main {
        justify-content: space-around;
    }
}
@media only screen and (min-width: 77.5rem /*1240px*/) {
    .ft-main {
        justify-content: space-evenly;
    }
}
form {
    display: flex;
    flex-wrap: wrap;
}
input[type="email"] {
    border: 0;
    padding: 0.625rem;
    margin-top: 0.3125rem;
}
input[type="submit"] {
    background-color: var(--primary-color);
    color: #fff;
    cursor: pointer;
    border: 0;
    padding: 0.625rem 0.9375rem;
    margin-top: 0.3125rem;
}
</style>








