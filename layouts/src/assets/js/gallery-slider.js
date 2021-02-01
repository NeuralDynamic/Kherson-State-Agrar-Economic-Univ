
const gallery = document.getElementById('gallery-list');

if (gallery) {
    require('lightgallery.js/dist/js/lightgallery.js');

    lightGallery(gallery, {
        download:true,
        loop:true
    }); 
}

