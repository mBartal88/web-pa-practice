function main() {
    let input = document.getElementById ("search")
    input.addEventListener ("keyup", submit)

    function submit () {
        createLists (this.value)
    }

    async function getFetch (phrase) {
        const response = await fetch (`/pa9/${phrase}`)
        return await response.json ()
    }

    async function createLists (phrase) {
        let characters = await getFetch (phrase)

        let list = document.getElementById ("character-list")
        list.innerHTML = ""

        for (let character of characters) {
            let element = document.createElement ("li")
            let searched = document.createElement ("span")
            let title = document.createElement ("span")

            searched.innerText = character.character
            searched.classList.add ("result")
            element.innerText = `${character.name} played `
            title.innerText = ` in ${character.title}`
            element.appendChild (searched)
            element.appendChild (title)
            element.classList.add ("list-item")

            list.appendChild (element)
        }
    }
}

main()





