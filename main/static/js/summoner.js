// console.log("jkljkl");

// window.onload = function() {

//     console.log("jklasjdklas");
    
//     console.log("kjasdklsad");
    
//     };

var tabButtons = document.querySelectorAll(".dlContainer .StatsHeaderElement");
var tabPanels = document.querySelectorAll(".StatsBox .StatsContent");

function showStatsContent(panelIndex) {
    console.log("starting");
    tabButtons.forEach(function(node) {
        node.style.backgroundColor = "#f2f2f2";
    });
    tabButtons[panelIndex].style.backgroundColor = "#ededed";
    tabPanels.forEach(function(node) {
        node.style.display = "none";
        node.style.backgroundColor = "black";
        });
    tabPanels[panelIndex].style.display = "block";
    console.log(tabButtons.length);
    console.log("ending");
}