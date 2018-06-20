$(function() {
    var count = 0;
    var running = false;
    var hours = 0;
    var minutes = 0;
    var seconds = 0;
    var milliseconds = 0;
    var element = $('#time');
    var time = element.find('.current-time');
    var hoursElement = element.find('.hours');
    var minutesElement = element.find('.minutes');
    var secondsElement = element.find('.seconds');
    var millisecondsElement = element.find('.milliseconds');
    var timer;

    function prependZero(time, length) {
        // Quick way to turn number to string is to prepend it with a string
        // Also, a quick way to turn floats to integers is to complement with 0
        time = '' + (time | 0);
        // And strings have length too. Prepend 0 until right.
        while (time.length < length) time = '0' + time;
        return time;
    }

    function runTimer() {
        // Using ES5 Date.now() to get current timestamp            
        var startTime = Date.now();
        var prevHours = hours;
        var prevMinutes = minutes;
        var prevSeconds = seconds;
        var prevMilliseconds = milliseconds;
        timer = setInterval(function() {
            var timeElapsed = Date.now() - startTime;
            hours = (timeElapsed / 3600000) + prevHours;
            minutes = ((timeElapsed / 60000) + prevMinutes) % 60;
            seconds = ((timeElapsed / 1000) + prevSeconds) % 60;
            milliseconds = (timeElapsed + prevMilliseconds) % 1000;
            time.text(makeTimeString());
        }, 25);
    }

    function run() {
        running = true;
        runTimer();
    }

    function makeTimeString() {
        var a = false;
        var string = "";
        if (Math.floor(hours) != 0 || a) {
            a = true;
            string += prependZero(hours, 2) + ": ";
        }
        if (Math.floor(minutes) != 0 || a) {
            a = true;
            string += prependZero(minutes, 2) + ": ";
        }
        string += prependZero(seconds, 2) + ".";
        string += prependZero(milliseconds, 3);
        return string;
    }

    function pause() {
        running = false;
        clearTimeout(timer);
        $("#results_list").append('<li>' + makeTimeString() + ' <a href="#" onclick="removeItem(this)"><i class="fas fa-times"></i></a></li>');
    }

    function reset() {
        hours = minutes = seconds = milliseconds = 0;
        time.text(makeTimeString());
    }
    // And button handlers merely call out the responsibilities
    function clickfunction() {
        $('#time').removeClass("hold");
        if ($('#results_list li').length < 5) {
            if (running) {
                pause();
                $("#timing-box").removeClass("fullscreen");
            } else {
                if (milliseconds == 0 && seconds == 0 && minutes == 0 && hours == 0) {
                    $("#timing-box").addClass("fullscreen");
                    run();
                } else {
                    //save;
                    reset();
                }
            }
        }
    }
    $("#timing-box").on('click', function() {
        clickfunction();
        console.log("click")
    });
    document.body.onkeyup = function(e) {
        if (e.which === 32) {
            clickfunction();
            console.log("Spacebar")
            //Your code goes here
        }
    };

    function hold() {
        if (milliseconds == 0 && seconds == 0 && minutes == 0 && hours == 0) {
            $('#time').addClass("hold");
        }
    }
    document.body.onkeydown = function(e) {
        if (e.which === 32) {
            hold();
            //Your code goes here
        }
    };
    document.onmousedown = function() {
        hold();
    }
    $(document).ready(function() {
        reset();
    });
});

function removeItem(item) {
    item.parentNode.parentNode.removeChild(item.parentNode);
}

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

