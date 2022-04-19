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
    if (file.type.startsWith("image")) {
        const reader = new FileReader();

        reader.readAsDataURL(file);
        reader.onload = () => {
            thumbnailElement.style.backgroundImage = `url("${reader.result}")`;
            thumbnailElement.style.backgroundsize = "cover";
            thumbnailElement.style.backgroundPosition =  'center';
            thumbnailElement.style.width = '100%';
            console.log("${reader.result}");
        }
    }
}

let btn = document.getElementById('btn');
btn.addEventListener("click", creatCard);

// hide form and btn, then create the card and display it
 function creatCard() {
     document.getElementById("col_").style.display='none';
     document.getElementById('inputName').textContent = document.getElementById('name').value;
     document.getElementById('inputCategory').textContent = document.getElementById('category').value;
     document.getElementById('inputPhone').textContent = document.getElementById('phone').value;
     document.getElementById('inputEmail').textContent = document.getElementById('email').value;
     document.getElementById('inputWebsite').textContent = document.getElementById('website').value;
     document.getElementById('inputFacebook').textContent = document.getElementById('facebook').value;
     document.getElementById('inputAddress').textContent = document.getElementById('address').value;
     document.getElementById('inputSentence').textContent = document.getElementById('sentence').value;
    //  document.getElementById('logo').style.backgroundImage = thumbnailElement.style.backgroundImage;
     document.getElementById("card").style.display="block"
}

// toggle - .hider





