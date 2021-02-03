const linked_cards = document.querySelectorAll('.linked-card');

linked_cards.forEach(item => {
    item.addEventListener('click', event => {
        const current_card = event.currentTarget;
        const link_cont = current_card.querySelector('.card__link');
        const win = window.open(link_cont.getAttribute('data-link'), '_blank');
        win.focus();
    });
}); 