async function fetchData (genre) {
    const response = await fetch(`/genres/${genre}`)
    let data = await response.json()
    return data
}

async function showData (genre) {
    let data = await fetchData(genre)
    let showDiv = document.querySelector(".show-div")
    let table = document.createElement("table")
    let headerTitle = document.createElement("th")
    let headerYear = document.createElement("th")
    let headerRow = document.createElement("tr")
    headerTitle.innerText = "Title"
    headerYear.innerText = "30 Year Anniversary"
    headerRow.appendChild(headerTitle)
    headerRow.appendChild(headerYear)
    table.appendChild(headerRow)
    showDiv.innerHTML = ""
    for (let show of data) {
        let row = document.createElement("tr")
        let td = document.createElement("td")
        let td2 = document.createElement("td")
        td.innerText = show.title
        td2.innerText = show.year+30
        row.appendChild(td)
        row.appendChild(td2)
        table.appendChild(row)
        showDiv.appendChild(table)
    }
}

function buttons () {
    let buttons = document.querySelectorAll(".buttons")
    buttons.forEach((element)=>{
        element.addEventListener("click", ()=> {
            let id = element.id
            showData(id)
        })
    })
}

buttons()