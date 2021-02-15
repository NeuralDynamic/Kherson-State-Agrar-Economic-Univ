const burger = document.querySelector('.header__burger');
const header = document.querySelector('header');

burger.addEventListener('click', event=>{
    const current_burder = event.currentTarget;
    const menu = document.getElementById('menu');
    const body = document.getElementsByTagName('body');

    if (current_burder.classList.contains('active')) {
        current_burder.classList.remove('active');
        menu.classList.remove('active');
        document.body.classList.remove('no-scroll');
    }else{
        current_burder.classList.add('active');
        menu.classList.add('active');
        document.body.classList.add('no-scroll');
    }
});


window.addEventListener('scroll',(event) => {
    if (window.scrollY > 100 && !header.classList.contains('scrolled')) {
        header.classList.add('scrolled');
        return;
    }

    if (window.scrollY < 100 && header.classList.contains('scrolled')) {
        header.classList.remove('scrolled');
    }
});

document.addEventListener("DOMContentLoaded", function(event) { 
    if (window.scrollY > 100 && !header.classList.contains('scrolled')) {
        header.classList.add('scrolled');
        return;
    }
});