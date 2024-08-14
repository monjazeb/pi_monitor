let slideIndex = 0;
nextSlide();

// Next/previous controls
function plusSlides(n) {
  currentSlide(slideIndex += n);
}

// Thumbnail image controls
function currentSlide(n) {
    slideIndex = n
    let i;
    let slides = document.getElementsByClassName("data-item");
    let dots = document.getElementsByClassName("dot");
    if (n > slides.length) {slideIndex = 1}
    if (n < 1) {slideIndex = slides.length}
    for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none";
    }
    for (i = 0; i < dots.length; i++) {
      dots[i].className = dots[i].className.replace(" active", "");
    }
    slides[slideIndex-1].style.display = "block";
    dots[slideIndex-1].className += " active";
}

function nextSlide() {
  let i;
  let at_home = document.getElementById("home");
  if (at_home){
    let slides = document.getElementsByClassName("data-item");
    let dots = document.getElementsByClassName("dot");
    for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none";
    }
    for (i = 0; i < dots.length; i++) {
      dots[i].className = dots[i].className.replace(" active", "");
    }
    slideIndex++;
    if (slideIndex > slides.length) {slideIndex = 1}
    slides[slideIndex-1].style.display = "block";
    dots[slideIndex-1].className += " active";
    setTimeout(nextSlide, 2000); // Change image every 2 seconds  
  }
}

function drawChart(tabel, dataset){
  var ctx = document.getElementById("chart"); 
  var myChart = new Chart(ctx, { 
    type: 'line', 
    data: { 
      labels: ['','','','','','','Today'], 
      datasets: dataset[tabel]}, 
    options: { 
          scales: { 
              yAxes: [{ 
                  ticks: { 
                      beginAtZero:true 
                  } 
              }] 
          } 
      } 
  });
}
