
// désactiver Back button
history.pushState(null, document.title, location.href);
window.addEventListener('popstate', function (event) {
    history.pushState(null, document.title, location.href);
});

