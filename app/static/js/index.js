// Your system time
var t = null;
t = setTimeout(showTime, 1000); //开始执行
function showTime() {
    clearTimeout(t); //清除定时器
    dt = new Date();
    document.getElementById("system-time").innerHTML = 'Your current server time: ' + dt;
    t = setTimeout(showTime, 1000); //设定定时器，循环执行             
}


window.onscroll = function () {
    scrollFunction()
};

function scrollFunction() {
    // 导航栏  https://www.w3schools.com/howto/howto_js_navbar_shrink_scroll.asp
    // When the user scrolls down 80px from the top of the document, resize the navbar's padding and the logo's font size
    if (document.documentElement.scrollTop > 25) {
        document.getElementById("navbar").style.padding = "10px 50px";
        document.getElementById("logo").style.fontSize = "25px";
    } else {
        document.getElementById("navbar").style.padding = "50px 90px";
        document.getElementById("logo").style.fontSize = "35px";
    }
    // Scroll Back To Top Button   https://www.w3schools.com/howto/howto_js_scroll_to_top.asp
    // When the user scrolls down 20px from the top of the document, show the button        
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        document.getElementById("myBtn").style.display = "block";
    } else {
        document.getElementById("myBtn").style.display = "none";
    }
}
// When the user clicks on the button, scroll to the top of the document
function topFunction() {
    document.body.scrollTop = 0; // For Safari
    document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
}


// https://blog.csdn.net/dcb_ripple/article/details/54347339
var Cookie = {
    setCookie: function (name, value, option) {
        var str = name + "=" + escape(value);
        if (option) {
            if (option.expireDays) {
                var date = new Date();
                var ms = option.expireDays * 24 * 3600 * 1000;
                date.setTime(date.getTime() + ms);
                str += "; expires=" + date.toGMTString();
            }
            if (option.path) str += ";path=" + option.path;
            if (option.domain) str += ";domain=" + option.domain;
            if (option.secure) str += ";true";
        }
        document.cookie = str;
    },
    getCookie: function (name) {
        var cookies = document.cookie.split(";");
        for (var i = 0; i < cookies.length; i++) {
            var arr = cookies[i].split("=");
            if (arr[0].trim() == name) {
                return unescape(arr[1]);
            }
        }
        return "";
    },
    delCookie: function (name) {
        this.setCookie(name, "", {
            expireDays: -1
        });
    }
}
window.onload = function () {
    if ("1" == Cookie.getCookie("diffmaker")) {
        //alert("找到Cookie，我将不再刷新页面，并删除Cookie");  
        Cookie.delCookie("diffmaker");
    } else {
        //alert("没有找到Cookie，我将刷新页面!");  
        Cookie.setCookie("diffmaker", "1", null);
        //window.location.reload(true);  // Development....
    }
}