

//model



let datas = JSON.parse(localStorage.getItem("data")) === null
  ? []
  : JSON.parse(localStorage.getItem("data"))



let newRow = (first,
  last,
  handle) => {
  return {
    first: first,
    last: last,
    handle: handle
  }
}
let pushIndata = (object) => {
  datas.push(object)
  localStorage.setItem("data", JSON.stringify(datas))
}

let removeInData = (index) => {
  datas.splice(index, 1)
  localStorage.setItem("data", JSON.stringify(datas))
}

//vue

let createArow = (index, first,
  last,
  handle) => {
  let tr = document.createElement("tr")
  let idCell = document.createElement("td")
  idCell.textContent = index + 1
  let firstCell = document.createElement("td")
  firstCell.textContent = first
  let lastCell = document.createElement("td")
  lastCell.textContent = last
  let handleCell = document.createElement("td")
  handleCell.textContent = handle
  let deletteCell = document.createElement("td")
  let deleteButton = document.createElement("button")
  deleteButton.classList.add("btn", "btn-danger")
  deleteButton.id = `row_${index}`
  deleteButton.textContent = "delete"
  deletteCell.append(deleteButton)
  tr.append(idCell)
  tr.append(firstCell)
  tr.append(lastCell)
  tr.append(handleCell)
  tr.append(deletteCell)
  return tr
}

let fromFormToData = (form) => {
  let inputs = [...form.querySelectorAll("input")]
  return inputs.filter(input => input.type !== "submit")
    .reduce((prev, current) => {
      prev[current.name] = current.value
      return prev
    }, {})

}

let emptyInputs = (form) => [...form.querySelectorAll("input")]
  .filter(input => input.type !== "submit")
  .forEach(input => input.value = '')

let deletArow = (event) => table.querySelectorAll("tbody tr")[Number(event.target.id.substring(4))].remove()


//controller

let table = document.querySelector("table")

let form = document.querySelector("form")

let feedTheTable = (event) => {
  event.preventDefault()
  let datasFrom = fromFormToData(form)
  pushIndata(datasFrom)
  emptyInputs(form)
  emptyAndFuFill()
}


let emptyAndFuFill = () => {
  table.querySelector("tbody").innerHTML = ""
  datas.forEach((data, index) => {
    let row = createArow(index, data.first, data.last, data.handle)
    table.querySelector("tbody").append(row)
    createdeleteEvenetListner(row.querySelector(".btn-danger"))
  })
}

let deletRowProces = (e) => {
  deletArow(e)
  removeInData(e.target.id.substring(4))
  emptyAndFuFill()

}

let createdeleteEvenetListner = (btn) => { btn.addEventListener("click", deletRowProces) }


form.addEventListener("submit", feedTheTable)


emptyAndFuFill()