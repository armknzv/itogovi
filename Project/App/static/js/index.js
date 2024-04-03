const rotatingImage = document.querySelector(".indexLogo");
const images = ["static/assets/img/Logotype RGB 1.jpg", "static/assets/img/Logotype RGB 2.jpg", "static/assets/img/Logotype RGB 3.jpg"];
let currentIndex = 0;

function changeImage() {
    rotatingImage.src = images[currentIndex];
    currentIndex = Math.floor(Math.random() * images.length);
}

setInterval(changeImage, 3000);