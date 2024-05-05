// Función para desplazarse al principio de la página
function toTop() {
    window.scroll({
        top: 0,
        left: 0,
        behavior: 'smooth'
    });
}

// Evento de desplazamiento de la ventana
window.onscroll = function (ev) {
    if ((window.innerHeight + window.scrollY) >= document.body.offsetHeight - 20) {
        // Estás en la parte inferior de la página
        document.querySelector(".scale-out").classList.add("scale-in");
    } else {
        document.querySelector(".scale-out").classList.remove("scale-in");
    }
};

// Evento de carga del DOM
document.addEventListener('DOMContentLoaded', function () {
    const menuButton = document.querySelector('.menu-button');
    const mobileMenu = document.querySelector('.lg\\:hidden > div');

    // Agrega un event listener al botón del menú
    menuButton.addEventListener('click', function () {
        // Alternar la visibilidad del menú desplegable
        mobileMenu.classList.toggle('hidden');
    });
});