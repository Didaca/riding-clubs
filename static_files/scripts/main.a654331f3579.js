function Load() {
    document.querySelector('.nav-user').addEventListener('click', () => {
        let div = document.querySelector('.enter');
        let has_name = div.className.split(' ')[1];
        if(has_name){
            div.classList.remove('switch');
        } else {
            div.classList.add('switch');
        }
        })

    document.querySelectorAll('.select-page').forEach(element => {
        if(element.href === window.location.href) {
            element.classList.add('active');
        }
    })
}

Load()

function ShowBackToTop() {
    document.querySelector('.back-to-top').addEventListener('click', () => {
      window.scrollTo({
        top: 0,
        left: 0,
        behavior: "smooth"
      });
    });

    if(window.scrollY > 200) {
      document.querySelector('.back-to-top').style.visibility = "visible";
    }else {
      document.querySelector('.back-to-top').style.visibility = "hidden";
    }
  }

window.onscroll = ShowBackToTop;
