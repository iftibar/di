//for (let i = 0; i<=15; i++) {
 //   if (i % 2) {
 //       console.log(i, 'is odd number');
//            }
//   else {
//        console.log(i, 'is even number');
//    }       


//ex2
let name;
let charecter = '';
let upperName;
let names = ["john", "sarah", 23, "Rudolf", 34];
for (let i of names) {
    console.log(i)

        let name = names[i]
        console.log(name);
        if (isNaN(name))  {
                charecter = name.charAt(0)
                if (charecter === charecter.toUpperCase()) {
                    console.log(name);
                }
                else {
                    upperName = names.rePlaceAt(0, charecter.toUpperCase());
                    console.log(upperName);
                    }    
                }           
        else {
        console.log(names[i]);
        }
        
    }


