const radio_sliders = document.querySelectorAll('.slider-radio');

const sliderstate = {
    counter:0,
    loop_time:4000
};

function start_radio_slider_loop(slider,i){
    stop_radio_slider_loop(i)
    const container = slider.querySelector('.slider__container');
    const navigation = container.querySelector('.navigation-manual');
    const radio_inputs = navigation.querySelectorAll('input[type="radio"]');
    const interval_loop = setInterval(()=>{
        if (sliderstate.counter === radio_inputs.length) {
            sliderstate.counter = 0;
        }
        radio_inputs[sliderstate.counter].checked = true;
        var event = new Event('change');
        radio_inputs[sliderstate.counter].dispatchEvent(event);
        sliderstate.counter++;
    },sliderstate.loop_time);
    sliderstate['r' + i] = interval_loop;
}

function stop_radio_slider_loop(i){
    clearInterval(sliderstate['r' + i]);
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
            console.log(radio_button);
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
            stop_radio_slider_loop(i);
            sliderstate.counter = index + 1;
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