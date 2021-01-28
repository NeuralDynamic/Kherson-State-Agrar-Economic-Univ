const hiding_lists = document.querySelectorAll('.hiding-list .hiding-list__title');

hiding_lists.forEach(item => {
    item.addEventListener('click',event => {
        let $this = event.currentTarget;
        let parent = $this.parentElement;

        if (parent.classList.contains('active')) {
            parent.classList.remove('active');
        }else{
            parent.classList.add('active');
        }
    });
});