window.onscroll = function () {
    scrollFunction()
};

function scrollFunction() {
    // 导航栏  https://www.w3schools.com/howto/howto_js_navbar_slide.asp
    // https://www.w3schools.com/howto/howto_js_navbar_shrink_scroll.asp
    // When the user scrolls down 20px from the top of the document, slide down the navbar
    // When the user scrolls to the top of the page, slide up the navbar (50px out of the top view)

    // Scroll Back To Top Button   https://www.w3schools.com/howto/howto_js_scroll_to_top.asp
    // When the user scrolls down 20px from the top of the document, show the button        
    if (document.body.scrollTop > 10 || document.documentElement.scrollTop > 10) {
        // document.getElementById("navbar").style.top = "0";  // howto_js_navbar_slide
        document.getElementById("navbar").style.padding = "5px 10px";
        document.getElementById("logo").style.fontSize = "25px";
        document.getElementById("myBtn").style.display = "block";
    } else {
        // document.getElementById("navbar").style.top = "-60px"; // howto_js_navbar_slide
        document.getElementById("navbar").style.padding = "30px 10px";
        document.getElementById("logo").style.fontSize = "35px";
        document.getElementById("myBtn").style.display = "none";
    }
}

// When the user clicks on the button, scroll to the top of the document
function topFunction() {
    document.body.scrollTop = 0; // For Safari
    document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
}