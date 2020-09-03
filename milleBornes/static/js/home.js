var newSession = (sessionStorage.getItem('newSession') == null) ? true : (sessionStorage.getItem('newSession')=='true');
var options =null;

if(newSession) { 
    options = localStorage.getItem('options');
    if(options!=null) {
    // envoyer à l'API (post pour insert/replace)
    const urlOptions=document.getElementById("apiURL").value;
    (async () => {
        const response = await fetch(urlOptions,
            {
                method: 'POST',
                body: options, // envoi des datas json au serveur
                headers: { 'Content-Type': 'application/json' }
            }
        );
        const myJson = await response.json(); //extract JSON from the http response
        console.log(myJson);
    })();
    }
    newSession=false;
    sessionStorage.setItem('newSession',newSession);
}
