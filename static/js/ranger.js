function changeVal (){
    let p = document.getElementById("val")
    let range = document.getElementById("inputs")
    p.textContent = range.value
    range.onchange = changeVal
    showHide(range.value)

}

function showHide(n){
    let s = document.querySelectorAll(".shows")
    s.forEach((element) => {
        if (Number(element.id) < n)
            element.classList.add("hidd")
        if (Number(element.id) >= n)
            element.classList.remove("hidd")
    })
    }

changeVal()

