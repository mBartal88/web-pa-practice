function main() {
    let cards = document.querySelectorAll(".flex-card1")
    cards.forEach((element)=> {
        element.addEventListener("dblclick", changeBack)
    })

    function changeBack() {
        if (this.id % 2 === 0) {
            this.classList.toggle("even")
        } else {
            this.classList.toggle("odd")
        }
    }

}

main()