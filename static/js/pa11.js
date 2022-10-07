function main () {
    let tbody = document.getElementById ("show-container")
    let table = document.getElementById ("table")
    init ()

    async function fetchShows ( genre ) {
        const response = await fetch (`/pa11/${genre}`)
        return await response.json ()
    }

    async function createTable ( genre ) {
        let data = await fetchShows (genre)
        let tbody = document.getElementById ("show-container")
        tbody.innerHTML = ""

        for (let show of data) {
            let showRow = document.createElement ("tr")
            let showData = document.createElement ("td")

            showData.innerText = show.title

            showRow.appendChild (showData)
            tbody.appendChild (showRow)
        }
        checkBody ()
    }

    function selector () {
        let genreSelector = document.getElementById ("genre-selector")
        let genre = genreSelector.value
        createTable (genre)
    }

    function checkBody () {
        if (tbody.innerText === "") {
            table.classList.add ("hidd")
        } else {
            table.classList.remove ("hidd")
        }
    }

    function init () {
        checkBody ()
        let button = document.getElementById ("submit")
        button.addEventListener ("click", () => {
            selector ()
        })
    }
}

main ()



