/******/ (function(modules) { // webpackBootstrap
/******/ 	// The module cache
/******/ 	var installedModules = {};
/******/
/******/ 	// The require function
/******/ 	function __webpack_require__(moduleId) {
/******/
/******/ 		// Check if module is in cache
/******/ 		if(installedModules[moduleId]) {
/******/ 			return installedModules[moduleId].exports;
/******/ 		}
/******/ 		// Create a new module (and put it into the cache)
/******/ 		var module = installedModules[moduleId] = {
/******/ 			i: moduleId,
/******/ 			l: false,
/******/ 			exports: {}
/******/ 		};
/******/
/******/ 		// Execute the module function
/******/ 		modules[moduleId].call(module.exports, module, module.exports, __webpack_require__);
/******/
/******/ 		// Flag the module as loaded
/******/ 		module.l = true;
/******/
/******/ 		// Return the exports of the module
/******/ 		return module.exports;
/******/ 	}
/******/
/******/
/******/ 	// expose the modules object (__webpack_modules__)
/******/ 	__webpack_require__.m = modules;
/******/
/******/ 	// expose the module cache
/******/ 	__webpack_require__.c = installedModules;
/******/
/******/ 	// define getter function for harmony exports
/******/ 	__webpack_require__.d = function(exports, name, getter) {
/******/ 		if(!__webpack_require__.o(exports, name)) {
/******/ 			Object.defineProperty(exports, name, { enumerable: true, get: getter });
/******/ 		}
/******/ 	};
/******/
/******/ 	// define __esModule on exports
/******/ 	__webpack_require__.r = function(exports) {
/******/ 		if(typeof Symbol !== 'undefined' && Symbol.toStringTag) {
/******/ 			Object.defineProperty(exports, Symbol.toStringTag, { value: 'Module' });
/******/ 		}
/******/ 		Object.defineProperty(exports, '__esModule', { value: true });
/******/ 	};
/******/
/******/ 	// create a fake namespace object
/******/ 	// mode & 1: value is a module id, require it
/******/ 	// mode & 2: merge all properties of value into the ns
/******/ 	// mode & 4: return value when already ns object
/******/ 	// mode & 8|1: behave like require
/******/ 	__webpack_require__.t = function(value, mode) {
/******/ 		if(mode & 1) value = __webpack_require__(value);
/******/ 		if(mode & 8) return value;
/******/ 		if((mode & 4) && typeof value === 'object' && value && value.__esModule) return value;
/******/ 		var ns = Object.create(null);
/******/ 		__webpack_require__.r(ns);
/******/ 		Object.defineProperty(ns, 'default', { enumerable: true, value: value });
/******/ 		if(mode & 2 && typeof value != 'string') for(var key in value) __webpack_require__.d(ns, key, function(key) { return value[key]; }.bind(null, key));
/******/ 		return ns;
/******/ 	};
/******/
/******/ 	// getDefaultExport function for compatibility with non-harmony modules
/******/ 	__webpack_require__.n = function(module) {
/******/ 		var getter = module && module.__esModule ?
/******/ 			function getDefault() { return module['default']; } :
/******/ 			function getModuleExports() { return module; };
/******/ 		__webpack_require__.d(getter, 'a', getter);
/******/ 		return getter;
/******/ 	};
/******/
/******/ 	// Object.prototype.hasOwnProperty.call
/******/ 	__webpack_require__.o = function(object, property) { return Object.prototype.hasOwnProperty.call(object, property); };
/******/
/******/ 	// __webpack_public_path__
/******/ 	__webpack_require__.p = "";
/******/
/******/
/******/ 	// Load entry module and return exports
/******/ 	return __webpack_require__(__webpack_require__.s = 0);
/******/ })
/************************************************************************/
/******/ ({

/***/ "./src/assets/js/cards.js":
/*!********************************!*\
  !*** ./src/assets/js/cards.js ***!
  \********************************/
/*! no static exports found */
/***/ (function(module, exports) {

eval("const linked_cards = document.querySelectorAll('.linked-card');\r\n\r\nlinked_cards.forEach(item => {\r\n    item.addEventListener('click', event => {\r\n        const current_card = event.currentTarget;\r\n        const link_cont = current_card.querySelector('.card__link');\r\n        const win = window.open(link_cont.getAttribute('data-link'), '_blank');\r\n        win.focus();\r\n    });\r\n}); \n\n//# sourceURL=webpack:///./src/assets/js/cards.js?");

/***/ }),

/***/ "./src/assets/js/hiding-list.js":
/*!**************************************!*\
  !*** ./src/assets/js/hiding-list.js ***!
  \**************************************/
/*! no static exports found */
/***/ (function(module, exports) {

eval("const hiding_lists = document.querySelectorAll('.hiding-list .hiding-list__title');\r\n\r\nhiding_lists.forEach(item => {\r\n    item.addEventListener('click',event => {\r\n        let $this = event.currentTarget;\r\n        let parent = $this.parentElement;\r\n\r\n        if (parent.classList.contains('active')) {\r\n            parent.classList.remove('active');\r\n        }else{\r\n            parent.classList.add('active');\r\n        }\r\n    });\r\n});\n\n//# sourceURL=webpack:///./src/assets/js/hiding-list.js?");

/***/ }),

/***/ "./src/assets/js/sections.js":
/*!***********************************!*\
  !*** ./src/assets/js/sections.js ***!
  \***********************************/
/*! no static exports found */
/***/ (function(module, exports) {

eval("const hiding_sections_header = document.querySelectorAll('section.hiding .section-title');\r\n\r\nhiding_sections_header.forEach(item => {\r\n    item.addEventListener('click',event => {\r\n        let $this = event.currentTarget;\r\n        let parent = $this.parentElement;\r\n\r\n        if (parent.classList.contains('active')) {\r\n            parent.classList.remove('active');\r\n        }else{\r\n            parent.classList.add('active');\r\n        }\r\n    });\r\n});\n\n//# sourceURL=webpack:///./src/assets/js/sections.js?");

/***/ }),

/***/ "./src/assets/js/sliders.js":
/*!**********************************!*\
  !*** ./src/assets/js/sliders.js ***!
  \**********************************/
/*! no static exports found */
/***/ (function(module, exports) {

eval("const radio_sliders = document.querySelectorAll('.slider-radio');\r\n\r\nconst sliderstate = {\r\n    counter:0,\r\n    loop_time:4000\r\n};\r\n\r\nfunction start_radio_slider_loop(slider,i){\r\n    const container = slider.querySelector('.slider__container');\r\n    const navigation = container.querySelector('.navigation-manual');\r\n    const radio_inputs = navigation.querySelectorAll('input[type=\"radio\"]');\r\n    const interval_loop = setInterval(()=>{\r\n        if (sliderstate.counter === radio_inputs.length) {\r\n            sliderstate.counter = 0;\r\n        }\r\n        radio_inputs[sliderstate.counter].checked = true;\r\n        var event = new Event('change');\r\n        radio_inputs[sliderstate.counter].dispatchEvent(event);\r\n        sliderstate.counter++;\r\n    },sliderstate.loop_time);\r\n    sliderstate['r' + i] = interval_loop;\r\n}\r\n\r\nfunction stop_radio_slider_loop(i){\r\n    clearInterval(sliderstate['r' + i]);\r\n}\r\n\r\nradio_sliders.forEach(function (item, i) {\r\n    const container = item.querySelector('.slider__container');\r\n    const navigation_manual = document.createElement('div');\r\n    const slides = container.querySelectorAll('.slider__slide');\r\n\r\n    navigation_manual.classList.add('navigation-manual');\r\n    container.appendChild(navigation_manual);\r\n\r\n    for (let index = 0; index < slides.length; index++) {\r\n\r\n        const radio_button = document.createElement('input');\r\n        radio_button.setAttribute('type','radio');\r\n        radio_button.setAttribute('name','radioBtn');\r\n        radio_button.setAttribute('id','radio' + (index + 1));\r\n        if (index === 0) {\r\n            radio_button.checked = true;\r\n            console.log(radio_button);\r\n        }\r\n\r\n        const navigation_label = document.createElement('label');\r\n        navigation_label.classList.add('manual-btn');\r\n        navigation_label.setAttribute('for','radio' + (index + 1));\r\n\r\n        navigation_manual.appendChild(radio_button);\r\n        navigation_manual.appendChild(navigation_label);\r\n\r\n        const current_slide = slides[index];\r\n        current_slide.style.width = 100/slides.length + '%';\r\n\r\n        // set margin for slide while radio was checked\r\n\r\n        navigation_label.addEventListener('click', event => {\r\n            stop_radio_slider_loop(i);\r\n            sliderstate.counter = index + 1;\r\n            setTimeout(()=>{\r\n                start_radio_slider_loop(item,i);\r\n            },3000);\r\n        });\r\n\r\n        radio_button.addEventListener('change', event => {\r\n            const button = event.currentTarget;\r\n            if (button.checked) {\r\n                slides[0].style.marginLeft = -index*100/slides.length + '%';\r\n            }\r\n        })\r\n    }\r\n\r\n    start_radio_slider_loop(item,i);\r\n    container.style.width = slides.length*100 + '%';\r\n    navigation_manual.style.width = 100/slides.length + '%';    \r\n});\n\n//# sourceURL=webpack:///./src/assets/js/sliders.js?");

/***/ }),

/***/ 0:
/*!****************************************************************************************************************************!*\
  !*** multi ./src/assets/js/cards.js ./src/assets/js/hiding-list.js ./src/assets/js/sections.js ./src/assets/js/sliders.js ***!
  \****************************************************************************************************************************/
/*! no static exports found */
/***/ (function(module, exports, __webpack_require__) {

eval("__webpack_require__(/*! /mnt/c/Users/nikkr/Programming/ksau/project/layouts/src/assets/js/cards.js */\"./src/assets/js/cards.js\");\n__webpack_require__(/*! /mnt/c/Users/nikkr/Programming/ksau/project/layouts/src/assets/js/hiding-list.js */\"./src/assets/js/hiding-list.js\");\n__webpack_require__(/*! /mnt/c/Users/nikkr/Programming/ksau/project/layouts/src/assets/js/sections.js */\"./src/assets/js/sections.js\");\nmodule.exports = __webpack_require__(/*! /mnt/c/Users/nikkr/Programming/ksau/project/layouts/src/assets/js/sliders.js */\"./src/assets/js/sliders.js\");\n\n\n//# sourceURL=webpack:///multi_./src/assets/js/cards.js_./src/assets/js/hiding-list.js_./src/assets/js/sections.js_./src/assets/js/sliders.js?");

/***/ })

/******/ });