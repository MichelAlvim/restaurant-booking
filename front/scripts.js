document.addEventListener("DOMContentLoaded", function() {
    const showRegisterLink = document.getElementById("show-register");
    const showLoginLink = document.getElementById("show-login");
    const loginCard = document.querySelector(".card");
    const registerCard = document.getElementById("register-card");

    showRegisterLink.addEventListener("click", function(event) {
        event.preventDefault();
        loginCard.classList.add("d-none");
        registerCard.classList.remove("d-none");
    });

    showLoginLink.addEventListener("click", function(event) {
        event.preventDefault();
        registerCard.classList.add("d-none");
        loginCard.classList.remove("d-none");
    });
});
