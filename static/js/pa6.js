function main () {
    let ratings = document.querySelectorAll (".rating")
    ratings.forEach ((element) => {
        element.addEventListener ("click", increaseRating)

        element.addEventListener ('contextmenu', function (event){
            event.preventDefault ();
            decreaseRating (element)
        });
    })

    function increaseRating () {
        this.innerText = (Number (this.innerText) + 0.1).toFixed (1)
    }

    function decreaseRating (element) {
        element.innerText = (Number (element.innerText) - 0.1).toFixed (1)
    }
}

main ()