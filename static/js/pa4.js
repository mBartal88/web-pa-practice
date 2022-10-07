function main() {
    let input = document.getElementById ("input-field")
    drawTable ("%")
    startSearch ()

    async function fetchResults (search) {
        const response = await fetch (`/pa4/${search}`)
        return await response.json ()
    }

    async function drawTable (search) {
        let data = await fetchResults (search)
        let table = document.getElementById ("shows-table")

        table.innerHTML = ""
        for (let row of data) {
            let tableRow = document.createElement ("tr")
            let tableTitle = document.createElement ("td")
            let tableRating = document.createElement ("td")
            let tableYear = document.createElement ("td")
            let tableTrailer = document.createElement ("td")
            let tableButton = document.createElement ("button")

            tableTitle.innerText = row.title
            tableRating.innerText = row.rating
            tableYear.innerText = row.year
            tableTrailer.innerText = row.trailer

            tableButton.innerText = "Watch trailer"
            tableButton.addEventListener ("click", () => {
                openModal (row.trailer)
            })

            tableRow.appendChild (tableTitle)
            tableRow.appendChild (tableRating)
            tableRow.appendChild (tableYear)
            if (tableTrailer.innerText !== "") {
                tableRow.appendChild (tableButton)
            }
            table.appendChild (tableRow)
        }
    }

    function startSearch() {
        input.addEventListener ("keyup", () => {
            let phrase = input.value
            if (input.value === "") {
                drawTable ("%")
            } else {
                drawTable (phrase)
            }
        })
    }

    function openModal (trailer) {
        let code = trailer.split ("=")
        let index_of_code = 1
        let link = `https://youtube.com/embed/${code[ index_of_code ]}`
        let c = document.getElementById ("content")
        c.innerHTML = `<iframe width='640' height='390' src=${link} allowFullScreen></iframe>`

        let modal = document.getElementById ("myModal");
        let span = document.getElementsByClassName ("close")[ 0 ];

        modal.style.display = "block";

        span.onclick = function () {
            modal.style.display = "none";
        }

        window.onclick = function (event) {
            if (event.target === modal) {
                modal.style.display = "none";
            }
        }
    }
}

main()