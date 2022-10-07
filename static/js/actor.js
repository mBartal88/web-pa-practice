function add () {
    let medal = document.querySelectorAll("#rank")
    medal.forEach((element)=> {
    element.addEventListener("click", () => {
        element.classList.add("effect");
        setTimeout(()=> {remove(element)}, 500);
    })
    })
}

function remove (element) {
        element.classList.remove("effect")
}

function main () {
    add ()
}

main()
