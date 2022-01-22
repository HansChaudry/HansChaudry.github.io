let rep =10;
var number = Math.ceil(Math.random() * 100);
let ul = document.getElementById("history");

function verify() {
    var guess = Number(this.elements.guess.value),
        output = document.getElementById('output');
    var score=0;
    var counter = document.getElementById("Counter");

    if (isNaN(guess)) {
        output.innerHTML = 'Enter a number.';
    } else if (number === guess) {
        score++;
        counter.innerHTML="Your Score increased by"+score+"game";
        output.innerHTML = 'You guessed right!';
    } else if (guess > 100) {
        output.innerHTML = 'Your guess is out of the 1 to 100 range.';
    } else if (guess > number) {
        output.innerHTML = 'You\'re getting warmer.';
    } else if (guess < number) {
        output.innerHTML = 'You\'re getting cold.';
    }
    return false;
}

document.getElementById('guessNumber').onsubmit = verify;

location.reload();
/*while (rep <13){
  console.log('still positive! current number:${rep}')
  rep++
}

let diceVal= math.random()*10;
console.log(diceVal);*/

function addHistory(num){
    let li = document.createElement("li");
    li.appendChild(document.createTextNode(num));
    ul.appendChild(li);
}

function clearHistory(){
    ul.innerHTML = '';
}
