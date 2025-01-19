var hoverOnButton = document.getElementById("lb").addEventListener("click", clickOnLayersButton);
//var RoadIcon = document.getElementById("Ro").addEventListener("click", clickOnRoadButton);
var RoadStatus = 0
var map = document.getElementById("map");
var layersPanelStatus = 0
function clickOnLayersButton() {
    if (layersPanelStatus==0){
        document.getElementById("layersPanel").style.visibility = 'visible';
        layersPanelStatus = 1;
    } else{
        document.getElementById("layersPanel").style.visibility = 'hidden';
        layersPanelStatus = 0;
    }
}

function clickOnRoadButton(map) {
    if (RoadStatus ==0 ){
        map.removeLayer(
            RoadL);
    }
}