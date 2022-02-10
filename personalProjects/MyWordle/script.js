function wordSearch(){
    let word = $("#searchWord").value;

    let request = new XMLHttpRequest();
    request.open('GET','https://api.dictionaryapi.dev/api/v2/entries/en/trick')
}

let myRequest = new XMLHttpRequest();
myRequest.open('GET','https://dictionary.yandex.net/api/v1/dicservice.json/lookup?key=dict.1.1.20220210T220903Z.5e240d6d2c57dcdd.f070e59491449c3c610806df69d2286b234be20f&lang=en-ru&text=trick')
myRequest.send();

// let myData = myRequest.responseText;
// let myData2 = JSON.parse(myRequest);
// console.log(myData2);

myRequest.responseType = 'text';
console.log(myRequest);

let data = myRequest.responseText;
let x  = JSON.parse(data);
console.log(x)