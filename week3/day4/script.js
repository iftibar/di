let num1 = 5
let num2 = 6
if (num1>num2) {
    prompt(num1, ' is the biggest number')
}
else {
    prompt(num2, ' is the biggest number')
}

let newDog = 'chihuahua'
console.log(newDog.length);
console.log(newDog.toUpperCase());
console.log(newDog.toLowerCase());
if (newDog=='chihuahua') {
    prompt('I love Chihuahuas, it’s my favorite dog breed');    
}
else {
    console.log('i dont care, i prefer cats');
}

let x = prompt('give me a number')
let y = x%=2
if (y == 0) {
    prompt(x, ' is even number'); 
}
else {
    prompt(x,' is odd number')
}
let rest;
let users = ['lea123', 'princess45', 'cat&dogLovers', 'helooo@00'];
if (users.length==0) {
   console.log('no one is online');  
}
else if (users.length==1) {
    console.log(users[0], ' is online');
}
else if (users.length==2) {
    console.log(users[0], 'and', users[1], ' are online');
}
else {
    let rest = users.length-2;
    console.log (users[0], users[1], 'and', rest , ' more is online');
}    
