function main () {
    let wasOlder = document.querySelectorAll ( "span" )
    let listItems = document.querySelectorAll ( "li" )

    wasOlder.forEach ( ( element ) => {
        if ( element.id === "True" ) {
            element.classList.add ( "highligth" )
        }
    } )

    listItems.forEach ( ( element ) => {
        element.addEventListener ( "click", showAge )
    } )

    function showAge () {
        let ageActorThen = this.children[1].textContent
        let showsAge = this.children[2].textContent
        alert ( `Age of the actor at show release: ${ageActorThen}\n\nShows current age ${showsAge}` )
    }
}

main()