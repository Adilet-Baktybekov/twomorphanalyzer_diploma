var modal = document.getElementById("myModal3");
var btn = document.getElementById("myBtn3");
var span = document.getElementsByClassName("close")[1];
btn.onclick = function () {
    modal.style.display = "block";
}
span.onclick = function () {
    modal.style.display = "none";
}
window.onclick = function (event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}