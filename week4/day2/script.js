// ex1:
// part 1
function infoAboutMe () {
    console.log("my name is iftach, 41 years old and i like to play drum & bass")

}
infoAboutMe();

// part 2
  function infoAboutPerson(personName, personAge, personColor) {
      console.log("person name is", personName, "he is", personAge,"years old and favorite color is", personColor);

  }
  infoAboutPerson("David", 45, "blue")
  infoAboutPerson("Josh", 12, "yellow")

// ex2:
function caculateTip () {
    bill = prompt("what is the bill?");
    let Bill = Number.parseInt(bill);
    if (Bill < 50)  {
        tip = Bill*20 / 100;
    } else if (Bill>=50 && Bill<300) {
        tip = Bill * 15 / 100    
    }
      
    else {tip = Bill * 10 / 100;    
        
    }
    total = Bill + tip;
    console.log(total);
}
// caculateTip()

// ex3:
let sum=0;
let div;
function isDivisble(div) {
    for (let i=0; i < 500; i++) {
    if (i%div)
    continue;
    else {
        console.log(i);
        sum += i;
    }

}
}
// div = prompt("what to divide?")
// isDivisble(div)
// console.log(sum)

// ex4:
let stock = { 
    "banana": 6, 
    "apple": 0,
    "pear": 12,
    "orange": 32,
    "blueberry":1
}  

let prices = {    
    "banana": 4, 
    "apple": 2, 
    "pear": 1,
    "orange": 1.5,
    "blueberry":10
}
let bill2 = 0; 
let shopingList = ['banana', 'orange', 'apple'];
function myBill() {
for (let item of shopingList) {
                if (stock[item]>0) {
                bill2 += prices[item];
                stock[item]--;
                console.log(item)
            }
            }    
        }
myBill()
console.log(bill2)

// ex4:
let totalSum = 0;
function changeEnough(itemPrice, amountOfChange) {
 for (let sum of amountOfChange) {
 switch (sum) {
     case amountOfChange[0]:
         totalSum += amountOfChange[0] * 0.25;  
         break;
         case amountOfChange[1]:
         totalSum+=amountOfChange[1] * 0.10;       
         break;
         case amountOfChange[2]:
         totalSum+=amountOfChange[2] * 0.05;         
         break;
         case amountOfChange[3]:
         totalSum+=amountOfChange[3] * 0.01;         
         break;
 }
}
if (totalSum>=itemPrice){
return true}
else {return false}
}
console.log(changeEnough(14.11, [2,100,0,0]))

// ex5:
let hotelNights = 0;
function hotelCost(hotelNights) {
    let sumNights = hotelNights*140;
   return sumNights;
}
let destin = ""
let planePrice = 0;
function planeRideCost (destin) {
    if (destin = "london") {
        console.log(planePrice)
        return planePrice = 183;
    }
    else if (destin = "paris") {
        console.log(planePrice)
        return planePrice = 220;
    }
    else {
        console.log(planePrice)
        return planePrice = 300;
    }
}
let carSum = 0;
let days = 0;
function rentalCarCost (days) {
    carSum = days * 40;
    if (days>=10) {
        carSum = carSum * 0.95;
    } 
    console.log(carSum)
    return carSum;
}
 function totalVacationCost () {
     hotelNights = prompt("how many nights in hotel?")
     while (isNaN(hotelNights)) {
        hotelNights = prompt("sorry didnt get it, how many nights in hotel?")
             }
             hotelNights = Number(hotelNights);
             
    destin = prompt("what is your destination?")
        if (!isNaN(destin)) {
            prompt("sorry didnt get it, what is your destination?")
            }             
            
    days = prompt("how many days do you want to rent a car?")        
    if (isNaN(days)) {
        prompt("sorry didnt get it, how many days to rent?")
    }
    days = Number(days);
    return hotelCost(hotelNights) +  planeRideCost(destin) +  rentalCarCost(days);

 }

 console.log(totalVacationCost())

 



    



























