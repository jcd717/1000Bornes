

// const userAction = async () => {
//     const response = await fetch('/testAPI/hello');
//     const myJson = await response.json(); //extract JSON from the http response
//     // do something with myJson
//     document.getElementById('cpt').innerHTML=myJson.result;
// }

// userAction()


(async () => {
    const response = await fetch(document.getElementById('urlAPI').value,
        {
            method: 'POST',
            body: '{ "a": 1, "b": 2 }', // envoi des datas json au serveur
            headers: { 'Content-Type': 'application/json' }
        }   
    );
    const myJson = await response.json(); //extract JSON from the http response
    // do something with myJson
    document.getElementById('cpt').innerHTML = myJson.result;
})();


// (async () => {
//     const response = await fetch(document.getElementById('urlAPI').value);
//     const myJson = await response.json(); //extract JSON from the http response
//     // do something with myJson
//     document.getElementById('cpt').innerHTML = myJson.result;
// })();

