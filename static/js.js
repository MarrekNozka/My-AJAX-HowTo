var datetime = new Date(0);
var timeelement = document.getElementById("time");
var timeelement = time;

function gettime() {
    timeelement.innerHTML = '<img src="static/load.gif" height="30" />';

    fetch("http://127.0.0.1:5000/time.json", { method:"GET", })
        .then(response => response.json())
        .then(data => {
            var d = data.datetime
            datetime.setFullYear(d.year, d.month-1, d.day);
            datetime.setHours(d.hour);
            datetime.setMinutes(d.minute);
            datetime.setSeconds(d.second)


            //timeelement.innerHTML = d.hour +":"+ d.minute+":"+d.second;
            timeelement.innerHTML = datetime.toLocaleString();
        })
}

var update = function() {
    datetime.setTime(datetime.getTime()+1000);
    timeelement.innerHTML = datetime.toLocaleString();

    function r(el, deg) {
        el.setAttribute('transform', 'rotate('+ deg +' 50 50)')
    }
    var d = new Date()
    r(sec, 6*d.getSeconds())  
    r(min, 6*d.getMinutes())
    r(hour, 30*(d.getHours()%12) + d.getMinutes()/2)

}
var positon = 0;
var redAnimation;
function move() {
    positon++;
    if (positon > 520 ) {
        positon = 0;
        clearInterval(redAnimation);
    }
    red.style.top = positon + 'px';
    red.style.left = positon + 'px';
}

setInterval(update,1000);

document.getElementById("reload").addEventListener("click", gettime);

red.addEventListener("click", function() {
   redAnimation = setInterval(move,10);
});


gettime();

