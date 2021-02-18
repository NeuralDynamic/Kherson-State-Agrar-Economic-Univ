import { tns } from 'tiny-slider/src/tiny-slider';

const radio_sliders = document.querySelectorAll('.slider-radio');
const scroller_sliders = document.querySelectorAll('.slider-scroller');

const slidersstate = {
    counter:0,
    loop_time:4000,
    per_slide:3,
    line_items:3
};

function start_radio_slider_loop(slider,i){
    stop_slider_loop(i)
    const container = slider.querySelector('.slider__container');
    const navigation = container.querySelector('.navigation-manual');
    const radio_inputs = navigation.querySelectorAll('input[type="radio"]');
    const interval_loop = setInterval(()=>{
        if (slidersstate.counter === radio_inputs.length) {
            slidersstate.counter = 0;
        }
        radio_inputs[slidersstate.counter].checked = true;
        var event = new Event('change');
        radio_inputs[slidersstate.counter].dispatchEvent(event);
        slidersstate.counter++;
    },slidersstate.loop_time);
    slidersstate['r' + i] = interval_loop;
}

function stop_slider_loop(i){
    clearInterval(slidersstate['r' + i]);
}

radio_sliders.forEach(function (item, i) {
    const container = item.querySelector('.slider__container');
    const navigation_manual = document.createElement('div');
    const slides = container.querySelectorAll('.slider__slide');

    navigation_manual.classList.add('navigation-manual');
    container.appendChild(navigation_manual);

    for (let index = 0; index < slides.length; index++) {

        const radio_button = document.createElement('input');
        radio_button.setAttribute('type','radio');
        radio_button.setAttribute('name','radioBtn');
        radio_button.setAttribute('id','radio' + (index + 1));
        if (index === 0) {
            radio_button.checked = true;
        }

        const navigation_label = document.createElement('label');
        navigation_label.classList.add('manual-btn');
        navigation_label.setAttribute('for','radio' + (index + 1));

        navigation_manual.appendChild(radio_button);
        navigation_manual.appendChild(navigation_label);

        const current_slide = slides[index];
        current_slide.style.width = 100/slides.length + '%';

        // set margin for slide while radio was checked

        navigation_label.addEventListener('click', event => {
            stop_slider_loop(i);
            slidersstate.counter = index + 1;
            setTimeout(()=>{
                start_radio_slider_loop(item,i);
            },5000);
        });

        radio_button.addEventListener('change', event => {
            const button = event.currentTarget;
            if (button.checked) {
                slides[0].style.marginLeft = -index*100/slides.length + '%';
            }
        })
    }

    start_radio_slider_loop(item,i);
    container.style.width = slides.length*100 + '%';
    navigation_manual.style.width = 100/slides.length + '%';    
});


scroller_sliders.forEach(item => {
    const container = item.querySelector('.slider__container');
    const prev_button = item.querySelector('.slider__prevSlideButton');
    const next_button = item.querySelector('.slider__nextSlideButton');
    let items = 3;
    let autoWidth = false;
    let autoplay = true;

    const params = {
        container: container,
        autoplay: true,
        // mouseDrag: true,
        autoplayButton:false,
        autoplayTimeout:3000,
        nav:false,
        prevButton: prev_button,
        nextButton: next_button,
        autoWidth: false,
        loop:true
    };

    if (item.classList.contains('teachers-scroller')) {
        const responsive = {
            640:{
                items: 2
            },
            900:{
                items: 3
            },
            1200: {
                items: 4
            },
            1500: {
                items: 5
            }
        }
        params.responsive = responsive;
    }

    if (item.classList.contains('gallery-scroller')) {
        params.autoWidth = true;
        const responsive = {
            640:{
                items: 1
            },
            1200: {
                items: 2
            },
            1440: {
                items: 3
            }
        }
        params.responsive = responsive;
    }

    const slider = tns(params);

    // item.querySelector('[data-action="stop"]').style.display = 'none';
}); 