document.querySelectorAll(".drop-zone__input").forEach(inputElemnt => {
    const dropZoneElement = inputElemnt.closest(".drop-zone");

    dropZoneElement.addEventListener('click', e => {
        inputElemnt.click()
    });

    inputElemnt.addEventListener('change', e => {
        if (inputElemnt.files.length) {
            updateThumbnail(dropZoneElement, inputElemnt.files[0])
        }
    })

    dropZoneElement.addEventListener("dragover", e => {
        e.preventDefault()
        dropZoneElement.classList.add("drop-zone--over");
    });
    ["dragleave", "dragend"].forEach(type => {
        dropZoneElement.addEventListener(type, e => {
            dropZoneElement.classList.remove("drop-zone--over");
        });
    });
    dropZoneElement.addEventListener("drop", e => {
        e.preventDefault();

        if (e.dataTransfer.files.length) {
            inputElemnt.files = e.dataTransfer.files;
            updateThumbnail(dropZoneElement, e.dataTransfer.files[0]);
        }
        dropZoneElement.classList.remove("drop-zone--over");
    });
});
let thumbnailElement;

function updateThumbnail(dropZoneElement, file) {
    let thumbnailElement = dropZoneElement.querySelector(".drop-zone__thumb");

    if (dropZoneElement.querySelector('.drop-zone__prompt')) {
        dropZoneElement.querySelector('.drop-zone__prompt').remove();
    }

    if (!thumbnailElement) {
        thumbnailElement = document.createElement('div');
        thumbnailElement.classList.add('drop-zone__thumb');
        dropZoneElement.appendChild(thumbnailElement);
    }
    thumbnailElement.dataset.label = file.name;
    let logo;
    if (file.type.startsWith("image")) {
        const reader = new FileReader();

        reader.readAsDataURL(file);
        reader.onload = () => {
            thumbnailElement.style.backgroundImage = `url("${reader.result}")`;
            thumbnailElement.style.backgroundsize = "cover";
            thumbnailElement.style.backgroundPosition = 'center';
            thumbnailElement.style.width = '245px';
            document.getElementById("logo").src = reader.result;

        }
    }

}

let btn = document.getElementById('btn');
btn.addEventListener("click", creatCard);

// hide form and btn, then create the card and display it
function creatCard() {
    document.getElementById("col_").style.display = 'none';
    document.getElementById('inputName').textContent = document.getElementById('name').value;
    document.getElementById('inputCategory').textContent = document.getElementById('category').value;
    document.getElementById('inputPhone').textContent = document.getElementById('phone').value;
    document.getElementById('inputEmail').textContent = document.getElementById('email').value;
    document.getElementById('inputFacebook').textContent = document.getElementById('facebook').value;
    document.getElementById('inputAddress').textContent = document.getElementById('address').value;
    document.getElementById('inputSentence').textContent = '"' + document.getElementById('sentence').value + '"';
    document.getElementById('inputWebsite').textContent= document.getElementById('website').value;
    
    // create icon for website:
    // web = document.getElementById('website').value;
    // let a = document.createElement('a')
    // a.setAttribute("href", web);
    // document.getElementById('inputWebsite').appendChild(a);
    // // document.card.appendChild(a);
    






    document.getElementById("card").style.display = "flex";
    document.getElementById("userDesign").style.display = "inline-block";

    //  inputWebsite.href =  document.getElementById('website').value;



}
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

let fontBtn = document.getElementById("fontBtn");
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








