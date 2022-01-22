let ul = document.getElementById("history");
let rep = 10;
let number = Math.ceil(Math.random() * 100);
//for testing purposes, delete before submitting
console.log(number);
let wrongs = 0;
let output = document.getElementById('output');
let score = document.getElementById('score');


function verify() {
    let guess = Number(document.getElementById('input').value);


    if (isNaN(guess)) {
        output.innerHTML = 'Enter a number.';
    }
    
    else if (number === guess) {
        output.textContent ='You guessed right!';
    } 
    
    else if (guess > 100) {
        wrongs +=1;
        score.innerHTML = `Score = ${10 - wrongs}`;
        output.textContent = 'Your guess is out of the 1 to 100 range.';
        addHistory(guess);
    }
    
    else if (guess > number) {
        wrongs += 1;
        score.innerHTML = `Score = ${10 - wrongs}`;
        output.textContent = 'You\'re getting warmer.';
        addHistory(guess);
    }
    
    else if (guess < number) {
        wrongs += 1;
        score.innerHTML = `Score = ${10 - wrongs}`;
        output.textContent = 'You\'re getting cold.';
        addHistory(guess);
    }
    return false;
}

function addHistory(num){
    let li = document.createElement("li");
    li.appendChild(document.createTextNode(num));
    ul.appendChild(li);
}

function clearHistory(){
    ul.innerHTML = '';
}
