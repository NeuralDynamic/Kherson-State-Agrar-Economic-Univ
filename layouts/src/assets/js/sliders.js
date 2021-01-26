import { tns } from 'tiny-slider/src/tiny-slider';


// Teacher sliders
const teacher_sliders = tns({
    container: '.teacherSlider__container',
    items: 3,
    autoplay: true,
    // mouseDrag: true,
    autoplayButton:false,
    autoplayTimeout:3000,
    nav:false,
    prevButton: '.teacherSlider__prevSlideButton',
    nextButton: '.teacherSlider__nextSlideButton',
});


document.getElementById('tns1-ow').querySelector('[data-action="stop"]').style.display = 'none';