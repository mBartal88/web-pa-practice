async function fetchData(genre){
    const response = await fetch(`/stars/${genre}`)
    let data = await response.json()
    return data
}

async function showData(genre){
    let data = await fetchData(genre)
    let container = document.getElementById("item-container")

    container.innerHTML = ""
    for (let shows of data) {
        let item = document.createElement("li")
        let rating = Math.round(shows.rating)
        let score = ""
        for (let i = 0; i < rating; i++){
            score += `<span class="fa fa-star"></span>`
        }
        for (let i = 0; i < 10-rating; i++){
            score += `<span class="fa fa-star-o"></span>`
        }

        item.innerHTML = `${shows.title} | ${shows.year} | ${shows.rating} <p>${score}</p>`
        container.appendChild(item)
    }
    init()

}
let g = ""

function sortByGenre(){
    let input = document.getElementById("selector")
    let button = document.getElementById("button")

    button.addEventListener("click", ()=> {

        let genre = input.value
        g = genre

        if (genre !== "") {
            showData (genre)
        }
    })
}

function init() {
    let stars = document.querySelectorAll(".fa-star, .fa-star-o");

    stars.forEach((star) => {
        star.addEventListener("mouseover", hover)
    })
}

function hover() {
    let star = this
    let stars_p = star.parentElement

    stars_p.addEventListener("mouseleave", reset)



    let stars = stars_p.querySelectorAll(".fa-star, .fa-star-o");

    for (let i = 0; i < stars.length; i++) {
        let id = i.toString()
        stars[i].setAttribute('id', id)
    }
    let star_id = star.id
    stars.forEach((s) => {

            if (s.id <= star_id) { //current target id-nál kisebb vagy nagyobb id csillagoknál
                s.className = "fa fa-star"
            }
            else {
                s.className = "fa fa-star-o"
            }
        })
}

function reset() {
    showData (g)

}

sortByGenre()
