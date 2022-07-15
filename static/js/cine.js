window.onload = function(){
    fetch("/cine/listarcine").then(res=>res.json())
    .then(res=>{
        var contenido="<table class='table'>";
        alert(JSON.stringify(res));
        var keys=Object.keys(res[0]);
        contenido+="<thead><tr>";
        for(var i=0; i<keys.length; i++){
            contenido+="<td>";
            contenido+=keys[i].toUpperCase();
            contenido+="</td>";
        }
        contenido+="</tr></thead>";
        contenido="</table>";
        document.getElementById("divTabla").innerHTML=contenido
    });
}