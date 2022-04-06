let people = ["Greg", "Mary", "Devon", "James"];
people.splice(0, 1);
people.splice(2, 1, "jason");
people.push("iftach")
console.log(people);
people2 = people.slice(1, 4);
delete.people2("iftach", "mary");
let str = people.slice(0, indexOf("mary"));
let str2 = people.slice()

// find the elemnt i dont want position
// get the array from o to posiotion to execlude and put into var
// get the array from the excluded position until the end
// merge
console.log(people2);
console.log(people.indexOf("foo"));
last = people.length - 1;
console.log(people[last])

for (i = 0; i < people.length; i++)
    console.log(people[i])
if (people[i] === "jason") { break; }


let colors = ["yellow", "green", "purple", "blue", "gray"];
let sufix = ["1st", "2nd", "3rd", "4th", "5th"]
for (let i = 0; i < colors.length; i++) {
    indexNumber = i + 1;
    console.log("my #", indexNumber, 'choice is', colors[i]);
    // while (i<colors.length) {
    //    console.log("my", sufix[i], "is", colors[i])
    // }  
}

// let num = number(prompt("give me a number"));
//// while (num<10) {
//     num = prompt("give me another number?")
//     }


let building = {
    numberOfFloors: 4,
    numberOfAptByFloor: {
        firstFloor: 3,
        secondFloor: 4,
        thirdFloor: 9,
        fourthFloor: 2,
    },
    nameOfTenants: ["Sarah", "Dan", "David"],
    numberOfRoomsAndRent: {
        sarah: [3, 990],
        dan: [4, 1000],
        david: [1, 500],
    },
}
// console.log(building.numberOfFloors)
// console.log(building.numberOfAptByFloor.firstFloor + building.numberOfAptByFloor.thirdFloor)
// console.log(building.nameOfTenants[1], building.numberOfRoomsAndRent.dan[0])
// if (building.numberOfRoomsAndRent.sarah[1] + building.numberOfRoomsAndRent.david[1]>building.numberOfRoomsAndRent.dan[1]) {
//     building.numberOfRoomsAndRent.dan[1] = 1200;
// }
// console.log(building.numberOfRoomsAndRent.dan)


let family = {
    dad: 'iftach',
    mom: 'naama',
    pet: 'pike',
    kids: {
        little: 'ja',
        bigger: 'or'
    }
}
Object.values(family)


for (let i in family) {
    console.log(i);

}

let details = {
    my: 'name',
    is: 'Rudolf',
    the: 'raindeer'
}



let names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];
names.sort()
for (let i = 0; i < names.length; i++) {
    let secret = names.chartAt(0) + secret;
}
console.log(secret)




