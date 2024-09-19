const body = document.querySelector("body");
const modeToggle = document.querySelector(".mode-toggle");

function toggleMode() {
    body.classList.toggle("light-mode");

    if (body.classList.contains("light-mode")) {
        modeToggle.innerText = "Dark Mode";
    } else {
        modeToggle.innerText = "Light Mode";
    }
}

modeToggle.addEventListener("click", toggleMode);