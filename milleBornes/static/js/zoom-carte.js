var overlay = document.getElementById('overlay');
var popup = document.getElementById('popup');
var popupWrapper=document.getElementById('popupWrapper');

function zoomCarte(e) {
    popup.setAttribute('src', e.target.attributes.zoom.value);
    // overlay.style.setProperty('left', e.clientX + "px");
    // overlay.style.setProperty('top', e.clientY + "px");
    popupWrapper.style.setProperty('left', e.clientX+"px");
    popupWrapper.style.setProperty('top', e.clientY+"px");

    overlay.style.display = 'flex';
    overlay.style.visibility = 'visible';
    // overlay.style.setProperty('left', 0);
    // overlay.style.setProperty('top', 0);
}

function closeZoomCarte() {
    overlay.classList.add('did-zoom-out');
}

document.addEventListener('animationend', function (e) {
    if (e.animationName === 'zoom-out') {
        overlay.classList.remove('did-zoom-out');
        overlay.style.visibility = 'hidden';
        overlay.style.display = 'none';
    }
});