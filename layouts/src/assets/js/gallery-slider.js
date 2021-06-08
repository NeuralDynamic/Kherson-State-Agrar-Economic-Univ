require('lightgallery.js/dist/js/lightgallery.js');

const gallery = document.getElementById('gallery-list');

if (gallery) {
    lightGallery(gallery, {
        download:true,
        loop:true
    }); 
}