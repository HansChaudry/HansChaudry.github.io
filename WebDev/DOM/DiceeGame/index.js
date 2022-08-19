var randomNumber1 = Math.floor(Math.random() * (7-1) + 1);
var randomNumber2 = Math.floor(Math.random() * (7-1) + 1);

document.querySelector(".img1").setAttribute("src", "images/dice"+randomNumber1+".png")
document.querySelector(".img2").setAttribute("src", "images/dice"+randomNumber2+".png")

if(randomNumber1 > randomNumber2){
    document.querySelector("h1").textContent = "Player 1 Wins!🚩";
}else{
    document.querySelector("h1").textContent = "Player 2 Wins!🚩";
}