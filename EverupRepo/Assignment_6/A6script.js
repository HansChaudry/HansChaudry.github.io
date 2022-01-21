//Part A
function findWinner(id1, id2, id3, id4, id5, id6, loc){
    netsavg = (Number(document.getElementById(id1).value) + Number(document.getElementById(id2).value) 
    + Number(document.getElementById(id3).value))/3;

    knicksavg = (Number(document.getElementById(id4).value) + Number(document.getElementById(id5).value) 
    + Number(document.getElementById(id6).value))/3;


    //DID NETS WIN?
    if( netsavg > knicksavg && netsavg >= 100){
         document.getElementById(loc).innerHTML = "Nets Win";
    }
    //DID KNICKS WIN?
    else if( knicksavg > netsavg && knicksavg >= 100){
        document.getElementById(loc).innerHTML = "Knicks Win";
    }
    //IS IT A DRAW?
    else if (netsavg === knicksavg && (netsavg >= 100 && knicksavg)){
        document.getElementById(loc).innerHTML = "It's a Draw";
    }
    //NOBODY WINS?
    else{
        document.getElementById(loc).innerHTML = "Nonobody Wins";
    }
}

//Part B
function tipCalc(cost, loc){
    n = Number(document.getElementById(cost).value);
    switch(n > 30 && n < 100){
        case true:
            document.getElementById(loc).innerHTML= n + (n * .15);
            break;
        case false:
            document.getElementById(loc).innerHTML= n + (n * .20);
            break;
    }
}

//Part C
const ConvertCelsiusToFahrenheit = (input, loc) => {
    temp = Number(document.getElementById(input).value);
    document.getElementById(loc).innerHTML = `${((temp * 1.8) + 32).toFixed(1)}°F`;
}

const ConvertFahrenheitToCelsius = (input, loc) => {
    temp = Number(document.getElementById(input).value);
    document.getElementById(loc).innerHTML = `${((temp - 32) * 5/9).toFixed(1)}°C`
}

// console.log(ConvertCelsiusToFahrenheit(37));
// console.log(ConvertFahrenheitToCelsius(98.6));

// function sayhi(){console.log("hello");}

// sayhi();
