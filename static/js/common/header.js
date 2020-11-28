$(document).ready(() => {

    let sidebar = document.getElementById("sidebar")
    let menuIcon = document.getElementById("header__menu__icon")
    let sidebarBackspace = document.getElementById("sidebar__side__backspace")

    /* SHOW SIDEBAR */
    menuIcon.addEventListener('click', (e) => {
        e.stopPropagation();
        sidebar.classList.toggle("show-sidebar")
        if (sidebar.classList.contains('show-sidebar')) {
            flex(sidebar)
            sidebar.classList.remove('hide-sidebar')
        }
        else {
            sidebar.classList.add("hide-sidebar")
        }
    });
    sidebar.addEventListener('click', (e) => {
        e.stopPropagation();
    });
    document.querySelector('body, html').addEventListener('click', (e) => {
        sidebar.classList.remove('show-sidebar')
        sidebar.classList.add("hide-sidebar")
    });
    sidebarBackspace.addEventListener('click', () => {
        sidebar.classList.remove('show-sidebar')
        sidebar.classList.add("hide-sidebar")
    })


    /* SIDEBAR__SIDE ACTIVE */

    let sidebar__side__item = document.querySelectorAll(".sidebar__side__item")

    sidebar__side__item.forEach(element => {
        element.addEventListener("click", (e) => {
            let current = document.querySelectorAll(".sidebar__side__item__active")
            current[0].classList.remove("sidebar__side__item__active")
            current[1].classList.remove("sidebar__side__item__active")
            if (e.target.classList.contains('sidebar__side__item')) {
                e.target.classList.add("sidebar__side__item__active")
                e.target.childNodes[1].classList.add("sidebar__side__item__active");
            }
            else {
                e.target.classList.add("sidebar__side__item__active")
                e.target.parentNode.classList.add("sidebar__side__item__active");
            }
        })
    });

}
)