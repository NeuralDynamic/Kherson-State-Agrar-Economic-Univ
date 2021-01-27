const hiding_sections_header = document.querySelectorAll('section.hiding .section-title');

hiding_sections_header.forEach(item => {
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