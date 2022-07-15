window.onload = function(){
$(".dataframe").DataTable()
$("#table").DataTable()

var elemento = document.querySelectorAll(".dataframe")
    for(var i=0; i<elemento.length; i++){
        elemento[i].classList.add("table")
    }
}