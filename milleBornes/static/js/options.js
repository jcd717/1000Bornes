
var isCancelClicked=false;

function cancelClicked() {
    isCancelClicked=true;
}

function stockageLocal(f) {
    if(isCancelClicked) return true;

    optionsJSON = '{"MOI":"' + f.elements['moi'].value+'"';
    optionsJSON += ',"PARTENAIRE":"' + f.elements['partenaire'].value + '"';
    optionsJSON += ',"ADVERSAIRE_DROITE":"' + f.elements['adversaireDroite'].value + '"';
    optionsJSON += ',"ADVERSAIRE_GAUCHE":"' + f.elements['adversaireGauche'].value + '"';
    optionsJSON += ',"MAIN":"' + (f.elements['droite'].checked ? 'MAIN_A_DROITE' : 'MAIN_A_GAUCHE') + '"';
    optionsJSON += '}';

    localStorage.setItem('options',optionsJSON);
    
    return true;
}