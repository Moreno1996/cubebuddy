function openCube(cube, elmnt) {

    // Remove the background color of all tablinks/buttons
    var items = document.getElementsByClassName("active");
    for(var i = 0; i< items.length; i++){
        items[i].classList.remove("active");
    }
    // Hide all elements with class="tabcontent" by default */
    console.log(cube + " - " + elmnt);
    elmnt.classList.add("active");
    // Show the specific tab content
}

// Get the element with id="active" and click on it
var start = document.getElementsByClassName("active")
for(var i = 0; i< start.length; i++){
        start[i].click();
}

