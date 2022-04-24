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

    // create icon for website:
    // web = document.getElementById('website').value;
    // // web.setAttribute("href", "web")
    // document.getElementById('inputWebsite') = web;
    // document.getElementById('inputWebsite').innerHTML = web;
    






    document.getElementById("card").style.display = "flex";
    document.getElementById("userDesign").style.display = "inline-block";

    //  inputWebsite.href =  document.getElementById('website').value;



}
let color1 = document.querySelector('.color1');
let color2 = document.querySelector('.color2');
let card = document.getElementById('card');

function setColor() {
    card.style.background = "linear-gradient(to right,  "
        + color1.value
        + ", "
        + color2.value
        + ")";
}
color1.addEventListener('input', setColor)

color2.addEventListener('input', setColor)








