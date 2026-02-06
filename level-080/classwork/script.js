// promt  იგივე input
let input =prompt("enter your name")  
console.log(input)

// იგივე ბულიანი
//  === მკაცრი ტოლობა 
console.log(5>10)
console.log("5" > "True")
console.log(5 == "5")//true
console.log(5 === "5")//false
// and == da . or --an
// && = ან 
// || da
// !  წინ გადაყავს საპირისპირო მნიშვნელობაში

// if else syntax
if (15 > 21){
    consloe.log("15>21")
} else{
    console.log("15<21")
}

// ternari operato syntax
15>21 ? console.log("15>21"):console.log("15<21")

let age =21

age > 18 ? console.log("user is adult"): console.log("user is tanger")


// swich

let day = "monday"
switch(day){
   case "monday":
     console.log("today is monday")
     break
  case "tusday":
     console.log("today is tusday")
     break
   case "wenseday":
     console.log("today is wensday")
     break
  case "thurthday":
     console.log("today is today")
     break
   case "friday":
     console.log(friday)

     default:
    consloe.log("not a week day")
     break

}


// functions 

function greet(){
    console.log("helo world from fuction")
}
function reminder(){
    consloe.log("its time wake up!")
}
function agecheker(age){
     age > 18 ? console.log("you are adoult") : console.log("you are teen")
}
function addition(){
    console.log(a + b)
}


greet()
reminder()
agecheker(21)
addition(9,8)

// ---------------------------------------------



// hosting - მაგალითად ცვლადების და ფუნქციების დეკლარაციები კოდის შესრულებამდე იწევა ზემოთ ჰოსტით
sayHello();

function sayHello() {
  console.log("Hello!");
}


let myName = "me";
switch (myName) {
  case "me":
    console.log("gio");
    break;

  case "gio1":
    console.log("gio1");
    break;

  case "gio2":
    console.log("gio12");
    break;

  default:
    console.log("gaumarjos");
}



function greet(name) {
  return "gaumarjiiiooss " + name + "!";
}


console.log(greet("gio"));



function multiplication(a, b) {
  return a * b;
}

console.log(multiplication(5, 3)); 


function substriction(a, b) {
  return a - b;
}


console.log(substriction(10, 4));

 
function ageChecker(age) {
  if (age > 18) {
    return "srulwlovani";
  } else {
    return "mozardi";
  }
}


console.log(ageChecker(2026));
console.log(ageChecker(12));