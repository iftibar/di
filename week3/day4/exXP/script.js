let lang = prompt('what language do you speak?');
langLower = lang.toLowerCase();
switch (langLower) {
    case 'english':
        alert('Hello');
        break;
    case 'french':
        alert('bonjour');
        break;
    case 'hebrew':
        alert('shalom');
        break;
    default:
        alert('01110011 01101111 01110010 01110010 01111001')
}

let grade = prompt('what is your grade?');
let gradeLet;

if (grade > 90) {
    gradeLet = 'A'
} else if (grade>80 && grade<=90) {
    gradeLet = 'B'
} else if (grade>=70 && grade<=80){
    gradeLet = 'C'
} else if (grade<70) {
    gradeLet = 'D'
} else {gradeLet = 'error';
}

switch(gradeLet) {
    case 'A':
        console.log('A');
        break;
    case 'B':
        console.log('B');
        break;
    case 'C':
        console.log('C');
        break;
    case 'D':
        console.log('D');
        break;
    default:
        console.log('errrror');
}

let verb = prompt('what is the word?');
let newVerb;
let result = Text.endswith('ing');
if (verb.length>3 && result = true ) {
    newVerb = verb+'ly'; 
}
else if (verb.length>3) {
    newVerb = verb + 'ing';
}

else {
    newverb=verb;
}
alert (newVerb);



