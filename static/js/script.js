
function mostrarModalLogin(){
    var modal = document.getElementById("modalControlLogin");
    modal.style.display = "block";
    }
function esconderModal(){
    var modalLogin = document.getElementById("modalControlLogin");
    modalLogin.style.display = "none"
    var modalCadastro = document.getElementById("modalControlCadastro");
    modalCadastro.style.display = "none"
    }
function mostrarModalCadastro(){
        var modal = document.getElementById("modalControlCadastro");
        modal.style.display = "block";
}

var swiper = new Swiper(".mySwiper", {
  
    keyboard: {
    enabled: true,
    onlyInViewport: false,
  },
});




/* Get the element you want displayed in fullscreen mode (a video in this example): */
var elem = document.getElementById("myswipe");

/* When the openFullscreen() function is executed, open the video in fullscreen.
Note that we must include prefixes for different browsers, as they don't support the requestFullscreen method yet */
function openFullscreen() {
   if (document.webkitFullscreenElement) {
      document.webkitCancelFullScreen();
    } else {
      const el = document.documentElement;
      el.webkitRequestFullscreen(Element.ALLOW_KEYBOARD_INPUT);
    }
  if (elem.requestFullscreen) {
    elem.requestFullscreen();
  } else if (elem.webkitRequestFullscreen) { /* Safari */
    elem.webkitRequestFullscreen();
  } else if (elem.msRequestFullscreen) { /* IE11 */
    elem.msRequestFullscreen();
  }
}