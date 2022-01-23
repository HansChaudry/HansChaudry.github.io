//Elements that will be eddited 
let ul = document.getElementsByClassName('history');
let scoreTables = document.getElementsByClassName('points');
let highScores = document.getElementsByClassName('high');
let output = document.getElementById('output');
let score = document.getElementById('score');
let main = document.getElementById('main');
let lose = document.getElementById('lose');
let win = document.getElementById('win');

//global variables
let number = Math.ceil(Math.random() * 100);
//for testing purposes, delete before submitting
console.log(number);
let wrongs = 0;
let high = 0;


function check() {
    let input = Number(document.getElementById('input').value);

    if (isNaN(input)) {
        output.innerHTML = 'Enter a number.';
    }
    
    else if (input === number) {
        switchToWin()
    } 
    
    else if (input > 100 || input > number || input < number) {
        wrongNumber(input);
        if(wrongs === 10){
            switchToLose()
        }
        switch (input > number) {
            case true:
                output.textContent = 'You\'re guess was too high';
                break;
        
            case false:
                output.textContent = 'You\'re guess was too low';
                break;
        }
    }
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
    if((10 - wrongs) > high){
        for(let n = 0; n < highScores.length; n++){
            high = 10 - wrongs;
            highScores[n].innerHTML = `High Score = ${high}`;
        }
    }
}

function replay(){
    main.style.display = 'flex';
    lose.style.display = 'none';
    win.style.display = 'none'
    output.innerHTML = '';
    wrongs = 0;
    number = Math.ceil(Math.random() * 100);
    console.log(`new num ${number}`);
    updateScore();
    clearHistory();
}

function switchToLose(){
    main.style.display = 'none';
    lose.style.display = 'flex';
    document.getElementById('lost').textContent = `${number}`;
}

function switchToWin(){
    main.style.display = 'none';
    win.style.display = 'flex';
    updateHighScore();
    document.getElementById('secret').textContent = `${number}`;
    document.getElementById('yourScore').textContent = `Your Score = ${10-wrongs}`;
    document.getElementById('best').textContent = `Best = ${high}`;
}

function wrongNumber(x){
    wrongs +=1;
    updateScore();
    addHistory(x);
}