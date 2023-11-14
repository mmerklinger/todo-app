function toggleMenu() {
    const content = document.querySelector('.content');
    const sidebar = document.querySelector('.sidebar');

    if (sidebar.style.display === 'inline') { // sidebar visible
        sidebar.style.display = 'none';
        content.style.display = 'inline';
    } else { // content visible
        content.style.display = 'none';
        sidebar.style.display = 'inline';
    }
}