// JS首次进入刷新一次界面--利用Cookie
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