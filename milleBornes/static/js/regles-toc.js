
// gestion de l'affichage de la table des matières

document.getElementsByClassName('toctitle')[0].setAttribute('onclick','clickTOC()');

var toggleTOC = (sessionStorage.getItem('toggleTOC') == null) ?
    window.getComputedStyle(document.getElementsByClassName('toc')[0].getElementsByTagName('ul')[0]).display :
    sessionStorage.getItem('toggleTOC');

if (sessionStorage.getItem('toggleTOC') != null) {
    document.getElementsByClassName('toc')[0].getElementsByTagName('ul')[0].style.display = sessionStorage.getItem('toggleTOC');
}

function clickTOC() {
    toggleTOC = (toggleTOC == 'none') ? 'inherit' : 'none';
    sessionStorage.setItem('toggleTOC',toggleTOC);
    document.getElementsByClassName('toc')[0].getElementsByTagName('ul')[0].style.display = toggleTOC;
}
