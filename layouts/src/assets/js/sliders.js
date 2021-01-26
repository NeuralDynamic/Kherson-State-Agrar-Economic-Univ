import { tns } from 'tiny-slider/src/tiny-slider';


// Teacher sliders

const sliders = document.querySelectorAll('.slider');

sliders.forEach(item => {
    const container = item.querySelector('.slider__container');
    const prev_button = item.querySelector('.slider__prevSlideButton');
    const next_button = item.querySelector('.slider__nextSlideButton');
    
    const slider = tns({
        container: container,
        items: 3,
        autoplay: true,
        // mouseDrag: true,
        autoplayButton:false,
        autoplayTimeout:3000,
        nav:false,
        prevButton: prev_button,
        nextButton: next_button,
    });

    item.querySelector('[data-action="stop"]').style.display = 'none'
});