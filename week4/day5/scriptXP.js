// let elem = document.getElementById('navBar');
// elem.setAttribute('navBar', 'socialNetworkNavigation');
// let newLi = document.createElement('li');
// let newText = document.createTextNode('Logout');
// newLi.appendChild(newText);
// document.getElementById('navBar').appendChild(newLi);

// let pare = document.getElementsByClassName('list')

// for (let index = 0; index < pare.length; index++) {
//     let chil = document.createElement('li');
//     let line = document.createTextNode('Hey students!'); 
//     chil.appendChild(line);
//     pare[index].appendChild(chil);
    
// }
// document.getElementsByClassName('list')[1].removeChild(document.getElementsByClassName('list')[1].children[1])

// for (let index = 0; index < pare.length; index++) {
//     document.getElementsByClassName('list')[index].setAttribute('class', 'student_list')

// }

document.querySelector('div').style.backgroundColor ='lightblue';
document.querySelector('div').style.padding ='20px';
// let line = document.querySelector('ul').firstElementChild;
// line.style.display = 'none';
// let line2 = document.querySelector('ul').lastElementChild;
// line2.style.border = '10px solid'

let list = document.getElementById('list');
let first = list.childNodes[1];
let second = first.nextSibling;
second.style.display = 'none';






