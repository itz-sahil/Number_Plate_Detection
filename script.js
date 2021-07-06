function Info() {
    var i = document.getElementById("number").value;
    var xhr = new XMLHttpRequest();
    xhr.open("GET", `http://localhost/task8/num.cgi?x=${i}`, true);
    xhr.send();
    xhr.onload = async() => {
        document.getElementById("output").innerHTML = xhr.responseText;
    }   
}