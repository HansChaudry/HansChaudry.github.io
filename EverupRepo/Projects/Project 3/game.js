let ul = document.getElementsByClassName('history');
let scoreTables = document.getElementsByClassName('points');
let highScores = document.getElementsByClassName('high');
let number = Math.ceil(Math.random() * 100);
//for testing purposes, delete before submitting
console.log(number);
let wrongs = 0;
let high = 0;
let output = document.getElementById('output');
let score = document.getElementById('score');
let main = document.getElementById('main');
let lose = document.getElementById('lose');
let win = document.getElementById('win');


function check() {
    let input = Number(document.getElementById('input').value);


    if (isNaN(input)) {
        output.innerHTML = 'Enter a number.';
    }
    
    else if (input === number) {
        main.style.display = 'none';
        win.style.display = 'flex';
        updateHighScore();
    } 
    
    else if (input > 100) {
        wrongs +=1;
        updateScore();
        output.textContent = 'Your input is out of the 1 to 100 range.';
        addHistory(input);
        if(wrongs === 10){
            main.style.display = 'none';
            lose.style.display = 'flex';
        }
    }
    
    else if (input > number) {
        wrongs += 1;
        updateScore();
        output.textContent = 'You\'re guess was too high';
        addHistory(input);
        if(wrongs === 10){
            main.style.display = 'none';
            lose.style.display = 'flex';
        }
    }
    
    else if (input < number) {
        wrongs += 1;
        updateScore();
        output.textContent = 'You\'re guess was too low';
        addHistory(input);
        if(wrongs === 10){
            main.style.display = 'none';
            lose.style.display = 'flex';
        }
    }
    return false;
}

function addHistory(num){
    for(let i = 0; i < ul.length; i++){
        let li = document.createElement("li");
        li.appendChild(document.createTextNode(num));
        ul[i].appendChild(li);
        console.log('added');  
    }
}

function clearHistory(){
    for(let i = 0; i < ul.length; i++){
        ul[i].innerHTML = '';
    }
}

function updateScore(){
    for(let n = 0; n < scoreTables.length; n++){
        scoreTables[n].innerHTML = `Score = ${10 - wrongs}`;
    }
}

function updateHighScore(){
    for(let n = 0; n < highScores.length; n++){
        high = 10 - wrongs;
        highScores[n].innerHTML = `High Score = ${high}`;
    }
}

function replay(){
    main.style.display = 'flex';
    lose.style.display = 'none';
    win.style.display = 'none'
    wrongs = 0;
    number = Math.ceil(Math.random() * 100);
    console.log(`new num ${number}`);
    updateScore();
    clearHistory();
}