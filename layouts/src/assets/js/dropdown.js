const dropdowns = document.querySelectorAll('.dropdown');


dropdowns.forEach(dropdown => {
    const button = dropdown.querySelector('.dropdown__preview');
    button.addEventListener('click', event=>{
        event.preventDefault();
        dropdown.classList.toggle('active');
    });
});

document.addEventListener('click', event=> {
    const current_target = event.target;

    if (event.type == "focusin" ||
        current_target.closest('.dropdown') ||
        current_target.closest('.dropdown__preview') ||
        current_target.closest('.dropdown__select')) {
        return;
    }

    dropdowns.forEach(dropdown => {
        dropdown.classList.remove('active');
    });
});



