function toggleMenu() {
    const content = document.querySelector('.content');
    const menu = document.querySelector('.menu');

    if (menu.style.display === 'inline') { // menu visible
        menu.style.display = 'none';
        content.style.display = 'inline';
    } else { // content visible
        content.style.display = 'none';
        menu.style.display = 'inline';
    }
}