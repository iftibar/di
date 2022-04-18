// 1.
let head = document.getElementById('heading');
console.log(head.textContent);
// 2.????

let art = document.getElementsByTagName('article')[0]
let par = document.getElementsByTagName('p');
par[3].remove()
art.removeChild(par[par.length-1]);
let lastP = art.lastElementChild;
// document.removeLastChild(art);

// 3.

let h2 = document.getElementById('head2')
function color() {
    h2.style.background = 'red';
}
h2.addEventListener("click", color);

// 4:

let h3 = document.querySelector('h3');
h3.addEventListener("click", goAway);
function goAway() {
    h3.style.display = 'none';
   }

  
// 5:
let btn = document.getElementById('btn');
btn.addEventListener ("click", goBold);

function goBold() {
    for (let index = 0; index < par.length; index++) {
        par[index].style.fontweight = '1900'
        par[index].style.color = 'green';
    }
}
// bonous 1:
let size;

function randomHead() {
    console.log('lo')
    head.style.fontSize = `${Math.floor(Math.random() * 100)}px`;
}


head.addEventListener("mouseover", randomHead);


