function onlyOne(checkbox) {
  var checkboxes = document.getElementsByName('check')
  checkboxes.forEach((item) => {
      if (item !== checkbox) item.checked = false
  })
}


document.addEventListener("DOMContentLoaded", function() {
  var shrinkHeader = 70;
  window.addEventListener("scroll", function() {
    var scroll = getCurrentScroll();
    if (scroll >= shrinkHeader) {
      document.querySelector('.header-box').classList.add('smaller');
      document.querySelector('header').classList.add('shadow');
    } else {
      document.querySelector('.header-box').classList.remove('smaller');
      document.querySelector('header').classList.remove('shadow');
    }
  });

  function getCurrentScroll() {
    return window.pageYOffset || document.documentElement.scrollTop;
  }
});