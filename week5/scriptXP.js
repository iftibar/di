let userInput = [];

function libIt(userInput) {
    for (let index = 0; index < userInput.length; index++)
    if (checkInput(userInput[index])) {
        story += val + ' ';
        console.log(story);
        }
    }
    
function checkInput(userInput) {
    if (userInput.length > 0 && (userInput = isNaN()))
    return true;
    }
let button = document.getElementById('lib-button');
let story = document.getElementById('story');
let noun = document.getElementById('noun').value;
let adj = (document.getElementById('adjective')).value;
let person = (document.getElementById('person')).value;
let verb = (document.getElementById('verb')).value;
let place = (document.getElementById('place')).value;
userInput.push(noun, adj, person, verb, place);
console.log(userInput)

button.addEventListener("click", libIt(userInput));
   


