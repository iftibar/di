// ex1:
function isblank(str) {
if (str == '') {
return true;
}
else {return false};
}
console.log(isblank(prompt("enter string")))

// ex2:


function abbrevName(nameFrom) {
  let ind = nameFrom.indexOf(' ')
  let lname = nameFrom.substring(ind+1, ind+2);
  console.log(lname);
  let abb =  lname.toUpperCase() + '.';
  console.log(abb);
  let Fname = nameFrom.substring(0, ind)
  return (Fname + ' ' + abb);  
}
let nameFrom = prompt("what is your full name?")
console.log(abbrevName(nameFrom));

// ex3 swapCase:
let newstr = "";
function swapCase (string) {
  for (let char of string) {
   if (char == char.toUpperCase()) {
       newstr += char.toLowerCase()
   }
   else {
     newstr += char.toUpperCase()
   }
  }
  console.log(newstr)
}
swapCase(prompt("another string please"))

// ex4 omnipresent
let counter;
let x = 0;
function isOmnipresent(array, checknum) {
  for (let x of array) {
    for (let a of x) {
      if (a == checknum) {
        counter = true;
      }
      else {
        counter = false;
      }
    }
}
}
isOmnipresent([[1, 1], [1, 3], [5, 1], [6, 1]], 6)
console.log(counter)