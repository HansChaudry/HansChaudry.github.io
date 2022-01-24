//Elements with mutiple instances
let ul = document.getElementsByClassName('history')
    ,scoreTables = document.getElementsByClassName('points')
    ,highScores = document.getElementsByClassName('high')
//Other Elements that will be edited
    ,output = document.getElementById('output')
    ,main = document.getElementById('main')
    ,lose = document.getElementById('lose')
    ,win = document.getElementById('win')
//global variables
    ,number = Math.ceil(Math.random() * 100)
    ,wrongs = 0
    ,high = 0;


//MAIN FUNCTION
function check() {
    let input = Number(document.getElementById('input').value);

    if (isNaN(input)) {
        output.innerHTML = 'Enter a number.';
        document.getElementById('input').value = '';
    }
    
    else if (input === number) {
        switchToWin()
        document.getElementById('input').value = '';
    } 
    
    else if (input > 100 || input > number || input < number) {
        wrongNumber(input);
        document.getElementById('input').value = '';
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
    output.innerHTML = 'Guess a Number';
    wrongs = 0;
    number = Math.ceil(Math.random() * 100);
    console.log(`new num ${number}`);
    updateScore();
    clearHistory();
}

let wonAudio = new Audio('sounds/homer-woohoo.mp3')
    ,lostAudio = new Audio('sounds/homerCrying.mp3')
    ,wrongAudio = new Audio('sounds/doh.mp3');

function switchToLose(){
    main.style.display = 'none';
    lose.style.display = 'flex';
    document.getElementById('lost').textContent = `${number}`;
    lostAudio.play();
}

function switchToWin(){
    main.style.display = 'none';
    win.style.display = 'flex';
    updateHighScore();
    document.getElementById('secret').textContent = `${number}`;
    document.getElementById('yourScore').textContent = `Your Score = ${10-wrongs}`;
    document.getElementById('best').textContent = `Best = ${high}`;
    wonAudio.play();
}

function wrongNumber(x){
    wrongs +=1;
    updateScore();
    addHistory(x);
    wrongAudio.play();
}