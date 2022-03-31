let addressNumber = 6;
let addressStreet = 'noga ';
let country = ' Israel ';
globalAddress =  addressStreet + addressNumber + country
console.log( 'i live in: ', globalAddress)

let bYear = 1980
let fYear = 2468
age = fYear - bYear
console.log('i will be', age, 'in the year', fYear) 

let pets = ['cat', 'dog', 'fish', 'rabbit', 'cow' ]
let dog = pets[1]
console.log(dog)
pets.splice (3,1, 'horse')
console.log (pets.length, pets)
let age2= prompt ('how old are you?', 20)

let food = 'pizza'
let meal = 'dinner'
console.log ('i eat', food, 'at every', meal);

let myWatchedSeries = ["black miror", "money heist", "big bang theory"];
let myWatchedSeriesLength = 3
let myWatchedSeriesSentence = ["darken future", "stilling gold", "didnt see"];
console.log ('i watched', myWatchedSeriesLength, 'series:', myWatchedSeries);
let bgtplace = indexof ('the big bang theory')
myWatchedSeries.splice(bgtplace, 1, "friends")
myWatchedSeries.push ('seinfled')
myWatchedSeries.unshift ('someone somwhere');
myWatchedSeries.splice (1,1)
console.log (myWatchedSeries[1[2]]);

let temp = 30;
farTemp = temp / 5 * 9 + 32;
console.log(temp, 'C is', farTemp);

let c;
let a = 34;
let b = 21;

console.log(a+b) //first expression
    // Prediction:55
    // Actual:55

a = 2;

console.log(a+b) //second expression
    // Prediction:23
    // Actual:23
console.log(3 + 4 + '5');

typeof(15)
// Prediction:number
// Actual:number

typeof(5.5)
// Prediction:number
// Actual:number

typeof(NaN)
// Prediction:undefined
// Actual:number???

typeof("hello")
// Prediction:string
// Actual:string

typeof(true)
// Prediction: boolean
// Actual:boolean

typeof(1 != 2)
// Prediction:boolean
// Actual:boolean

"hamburger" + "s"
// Prediction:hamburgers
// Actual:hamburgers

"hamburgers" - "s"
// Prediction:undfined
// Actual:nan

"1" + "3"
// Prediction:13
// Actual:13

"1" - "3"
// Prediction:syntax error
// Actual:-2

"johnny" + 5
// Prediction:syntax error
// Actual:johnny5


"johnny" - 5
// Prediction:syntax error
// Actual:nan

99 * "hello"
// Prediction: hellohellohello (99)
// Actual:nan

1 != 1
// Prediction:false
// Actual:false

1 == "1"
// Prediction:true
// Actual:true

1 === "1"
// Prediction:false
// Actual:false

5 + "34"
// Prediction: 534
// Actual:534

5 - "4"
// Prediction:nan
// Actual:1

10 % 5
// Prediction:nan
// Actual:0

5 % 10
// Prediction:nan
// Actual:5

"Java" + "Script"
// Prediction:javascript
// Actual:javascript

" " + " "
// Prediction:   
// Actual:' '

" " + 0
// Prediction:0
// Actual:' 0'

true + true
// Prediction:nan
// Actual:

true + false
// Prediction:nan
// Actual:2

false + true
// Prediction:nan
// Actual:1

false - true
// Prediction:nan
// Actual:-1

!true
// Prediction:boolean
// Actual:flase

3 - 4
// Prediction:-1
// Actual:-1

"Bob" - "bill"
// Prediction:nan
// Actual:nan





