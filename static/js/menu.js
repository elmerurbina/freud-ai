const body = document.querySelector('body'),
    sidebar = body.querySelector('nav'),
    toggle = body.querySelector(".toggle"),
    modeSwitch = body.querySelector(".toggle-swictch"),
    modeText = body.querySelector("mode-text");

toggle.addEventListener("click", () => {
    sidebar.classList.toggle("close");
})


