//Part A
function convertTemp() {
    let x = document.getElementById('temp').value;
    let ans = (x * 1.8) + 32;
    document.getElementById('answer').innerHTML = `${x}°C is ${ans.toFixed(1)}°F`;
    document.getElementById('second').innerHTML = `${ans.toFixed(1)}°F is ${((ans - 32) * 5/9).toFixed(1)}°C`;
}


//Part B
function bmiCalc(){
    let johnBmi = (document.getElementById('JohnMass').value
    /document.getElementById('JohnHeight').value **2) * 703;

    let lucasBmi = (document.getElementById('LucasMass').value
    /document.getElementById('LucasHeight').value **2) * 703;

    if(lucasBmi > johnBmi){
        console.log("Lucas'BMI is higher than John's!");
    }else{
        console.log("John's BMI is higher than Lucas'!");
    }

    document.getElementById('winner').innerHTML = `John's BMI ${johnBmi.toFixed(1)} is higher than Lucas’ BMI ${lucasBmi.toFixed(1)}, that is statement ${johnBmi > lucasBmi}!`;
}

//Part C
let num = prompt("Enter a number:");

if(num == null || isNaN(Number(num)) || num === ''){
    console.log("Please enter a number!");
}
else if(num == 10){
    console.log("You win 10 points");
}
else if(num == 8){
    console.log("You win 8 points to console");
}
else if(num != 10 || num != 8){
    console.log("NOT MATCHED!!");
}