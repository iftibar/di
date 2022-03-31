let sentence = ["my", "favorite", "color", "is", "blue"];
let string = sentence.join();
console.log(string);

let str1 = "endoftheroad";
let str2 = "whywhywhy";
let sliceStart1 = str1.slice(0, 2);
let sliceStart2 = str2.slice(0, 2);
let sliceend1 = str1.slice(2);
let sliceend2 = str2.slice(2)

console.log(sliceStart1+sliceend2, sliceStart2+sliceend1);

//let num1 = prompt('first number please');
//let num2 = prompt('first number please');
//console.log(parseInt(num1) + parseInt (num2));
//console.log(parseInt(num1) - parseInt (num2));
//console.log(parseInt(num1) / parseInt (num2));
//console.log(parseInt(num1) * parseInt (num2));

5 >= 1
// true
0 === 1
// false
4 <= 1
// false
1 != 1
// false
"A" > "B"
// false
"B" < "C"
//true
"a" > "A"
// true
"b" < "A"
// flase
true === false
// false
true != true
// false

let numString = prompt('enter numbers seperated by commas');
let num = number(numString);
let sum = num.reduce(function(total, num) 0 );
console.log (sum);

