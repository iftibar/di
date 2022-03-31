let age = prompt('how old are you?');
if (age==18) {
    alert( 'Congratulations on your first year of driving. Enjoy the ride!')
    } else if (age>18) { alert('Powering On. Enjoy the ride!')
}    else { alert ('Sorry, you are too young to drive this car. Powering off')}

let object = {
    username: 'iftach',
    password: '12345'
}

let database = [object]
let person = {
    username: 'naama',
    timeline: 'abc'
    }
let person2 = {
    username: 'mishu',
    timeline: 'cde'
}
let person3 = {
    username: 'ishEhed',
    timeline: 'fgh'
}
let newsfeed = [person, person2, person3];
console.log(newsfeed, database)
