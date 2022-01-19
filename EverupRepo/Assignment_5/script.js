function convertTemp() {
    let x = document.getElementById('temp').value;
    let ans = (x * 1.8) + 32;
    document.getElementById('answer').innerHTML = `${x.toFixed(1)}°C is ${ans.toFixed(1)}°F`;
    document.getElementById('second').innerHTML = `${ans.toFixed(1)}°F is ${((ans - 32) * 5/9).toFixed(1)}°C`;
}

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

    document.getElementById('winner').innerHTML = `John's BMI ${johnBmi.toFixed(1)} is higher than Lucas’ BMI ${lucasBmi.toFixed(1)}, that is ${johnBmi > lucasBmi}!`;
}


// If user enters nothing or strings, log "Please enter a number!" to console;
// If user enter 10, log "You win 10 point" to console;
// If user typed 8, log "You win 8 points to console
// If the number is not 8 or 10, log "NOT MATCHED!!" to console
// let num = prompt("Please enter a number");

// if (num == null || typeof(num) == String) {
//   console.log("Please enter a number!");
// }
// else if(num === 10){
//     console.log("You win 10 point");
// }



// document.getElementById('temp').addEventListener('keypress', function (e) {
//     if (e.key === 'Enter') {
//       convertTemp();
//     }
// });