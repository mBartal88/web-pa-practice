let items = document.querySelectorAll(".item")
let rt = []
items.forEach((element)=> {
    element.addEventListener ( "click", changeBackground )
})

function changeBackground() {
    let item = this
    let cont = document.querySelector("h1")
    cont.innerText = "Years"
    let msg = document.createElement("p")
    if (item.classList.contains("item2")) {
        items.forEach((element)=> {
        element.classList.remove("item2")
            rt = []
        })
    } else {
        item.classList.add ( "item2" )
        rt.push(item.id)
        let sum = 0
        for (let i of rt) {
            sum += Number(i)
        }
        msg.innerText = String(sum / rt.length)
        cont.appendChild(msg)

    }
}

