const body = document.querySelector('body'),
    sidebar = body.querySelector('nav'),
    toggle = body.querySelector(".toggle"),
    searchaBtn = body.querySelector(".search-box"),
    modeSwitch = body.querySelector(".toggle-swictch"),
    modeText = body.querySelector("mode-text");

toggle.addEventListener("click", () => {
    sidebar.classList.toggle("close");
})

searchaBtn.addEventListener("click", () => { 
    sidebar.classList.remove("close");
})

modeSwitch.addEventListener("click", () => {

    body.classList.toggle("dark");
    if (body.classList.contains("dark")) {
        modeText.innerText = "Linght mode"
    }else {
        modeText.innerText = "Dark mode"
    }

})