var buttonColours = ["red", "blue", "green", "yellow"];
var randomNumber = 0;
var gamePattern = [];
var userClickedPattern= [];
var level = 0;

$(".btn").on("click", function(event){
    var userChosenColour = $(this).attr("id");
    userClickedPattern.push(userChosenColour);
    playSound(userChosenColour);
    animatePress(userChosenColour);

    checkAnswer(userClickedPattern.length - 1);
})

$(document).keypress(function() {
    nextSequence();
})

function nextSequence(){
    randomNumber = Math.floor(Math.random() * 4);
    var randomChosenColour = buttonColours[randomNumber];
    gamePattern.push(randomChosenColour);
    
    $("#" + randomChosenColour).fadeOut(100).fadeIn(100).fadeOut(100).fadeIn(100);
    playSound(randomChosenColour);

    level += 1;
    $("h1").text("Level " + level);
}

function playSound(name){
    var colorAudio = new Audio("sounds/" + name + ".mp3");
    colorAudio.play();
}

function animatePress(currentColour){
    $("div ." + currentColour).addClass("pressed")
    setTimeout(function(){
        $("div ." + currentColour).removeClass("pressed");
    }, 100);
}

function checkAnswer(currentlevel) {  
    if (userClickedPattern[currentlevel] == gamePattern[currentlevel]) {
        console.log("success");
        if(gamePattern.length == userClickedPattern.length){
            setTimeout(nextSequence, 1000);
            userClickedPattern = [];
        }
    }else{
        console.log("wrong");
        let overAudio = new Audio("sounds/wrong.mp3");
        overAudio.play();
        $("body").addClass("game-over");
        setTimeout(function (){
            $("body").removeClass("game-over");
        }, 200)
        $("h1").text("Game Over, Press Any Key to Restart");
        startOver();
    }
}

function startOver() {
    level = 0;
    gamePattern = [];
    userClickedPattern = [];
}