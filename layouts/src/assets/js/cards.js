const department_cards = document.querySelectorAll('.department-card');


department_cards.forEach(item => {
    item.addEventListener('click', event => {
        const current_card = event.currentTarget;
        const link_cont = current_card.querySelector('.department-card__link');
        window.location.replace(link_cont.getAttribute('data-department-link'));
    });
}); 