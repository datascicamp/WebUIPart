// Your system time
var t = null;
t = setTimeout(showTime, 1000); //开始执行
function showTime() {
    clearTimeout(t); //清除定时器
    dt = new Date();
    document.getElementById("system-time").innerHTML = 'Your current server time: ' + dt;
    t = setTimeout(showTime, 1000); //设定定时器，循环执行             
}