
let color1 = document.querySelector('.color1');
let color2 = document.querySelector('.color2');
let card = document.getElementById('card');

function setBackgroundColor() {
    card.style.background = "linear-gradient(to right,  "
        + color1.value
        + ", "
        + color2.value
        + ")";
}
color1.addEventListener('input', setBackgroundColor);

color2.addEventListener('input', setBackgroundColor);


let color3 = document.querySelector('.color3');
let color4 = document.querySelector('.color4');
let left = document.getElementById("left");
let right = document.getElementById("right");

function setTextColor() {
    left.style.color = color3.value;
    right.style.color = color4.value;
}
color3.addEventListener("input", setTextColor);
color4.addEventListener("input", setTextColor);

let fontBtn = document.getElementById('fontBtn');
let fonts = [ 'Cambria', 'Cochin', 'Georgia', 'Times', 'monospace', 'Franklin Gothic Medium', 'Arial Narrow', 'Arial', 'Lucida Sans', 'Lucida Grande', 'Lucida Sans Unicode', 'Verdana', 'sans-serif',  'Impact', 'Arial Narrow Bold'];
let i = 0;
function changeFont() {
    console.log(fonts[i])
    left.style.fontFamily = fonts[i]
    right.style.fontFamily = fonts[i]
    if (i < fonts.length -1){
    i++;
    }
    else { i=0 }
}
fontBtn.addEventListener('click', changeFont)
