function init () {
    let shows = document.querySelectorAll ( ".shows td" )
    let actors = document.querySelectorAll ( ".actors td" )

    shows.forEach ( ( element ) => {
        element.addEventListener ( "mouseover", actorHighlight )
        element.addEventListener ( "mouseleave", removeHighlight )
    } )

    actors.forEach ( ( element ) => {
        element.addEventListener ( "mouseover", showHighlight )
        element.addEventListener ( "mouseleave", removeHighlight )
    } )

    function actorHighlight () {
        let title = this
        actors.forEach ( ( element ) => {
            if ( element.id === title.innerText ) {
                element.classList.add ( "highligth" )
            }
        } )
    }

    function showHighlight () {
        let actor = this
        shows.forEach ( ( element ) => {
            if ( element.innerText === actor.id ) {
                element.classList.add ( "highligth" )
            }
        } )
    }

    function removeHighlight () {
        actors.forEach ( ( element ) => {
            element.classList.remove ( "highligth" )
        } )

        shows.forEach ( ( element ) => {
            element.classList.remove ( "highligth" )
        } )
    }
}

init ()