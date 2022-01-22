let ul = document.getElementById("history");
function addHistory(num){
    let li = document.createElement("li");
    li.appendChild(document.createTextNode(num));
    ul.appendChild(li);
}

function clearHistory(){
    ul.innerHTML = '';
}

addHistory(4);