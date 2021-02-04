const burger = document.querySelector('.header__burger');

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