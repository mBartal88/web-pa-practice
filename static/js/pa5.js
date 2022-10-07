function main() {
    let cards = document.querySelectorAll ( ".flex-cards" )
    cards.forEach ( ( element ) => {
        element.addEventListener ( "click", chBackground )
    } )

    function chBackground () {
        if ( this.id === "None" ) {
            this.classList.add ( "alive" )
        } else {
            this.classList.add ( "dead" )
        }
    }
}

main()