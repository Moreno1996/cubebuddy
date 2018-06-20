<!DOCTYPE html>
<html lang="en">
<?php 
			include "php/general_head.php";
?>
<script>
function setTime() {
	var vid = document.getElementById("video-active");
	console.log(vid.currentTime);
	$("#time").text(vid.currentTime);
	
	
	if(solve.end.length==solve.names.length){
	console.log("Already full!!");	
		
	}else{
	if (solve.start.length == solve.end.length) {
		solve.start.push((vid.currentTime).toFixed(2));
	} else {
		solve.end.push((vid.currentTime).toFixed(2));
	}
	console.log(solve.start + " - " + solve.end);
	load();
}
}
function removeTime() {
	if (solve.start.length == solve.end.length) {
		solve.end.pop();
	} else {
		solve.start.pop();
	}
	console.log(solve.start + " - " + solve.end);
	load();
}
function pause(){
		var vid = document.getElementById("video-active");
vid.pause();
}
function reset() {
	solve.start=[];
	solve.end=[];
	load();
}

function speed(a) {
	var vid = document.getElementById("video-active");
	vid.playbackRate = a;
	vid.play();
}

function frameStep(a) {
	frameTime = 1 / 30; //assume 25 fps
	var vid = document.getElementById("video-active");
	vid.pause();
	//one frame back
	vid.currentTime += a * frameTime;
}

function load() {
	text = "<thead><tr><th>Sort</th>";
	for (var i = 0; i < solve.names.length; i++) {
		text += "<th>" + solve.names[i] + "</th> ";
	}
	text += "</tr></thead>";
	text += "<tbody><tr><th>Times</th>";
	for (var i = 0; i < solve.names.length; i++) {
		text += "<th>";
		if (solve.start[i] != null && solve.end[i] != null) {
			text += (solve.end[i] - solve.start[i]).toFixed(2) + "</th>";
		} else {
			text += "--:--</th>";
		}
	}
	text += "</tr><tr><th>Start</th>";
	for (var i = 0; i < solve.names.length; i++) {
		text += "<th>";
		if (solve.start[i] != null) {
			text += solve.start[i] + "</th>";
		} else {
			text += "--:--</th>";
		}
	}
		text += "</tr><tr><th>End</th>";
	for (var i = 0; i < solve.names.length; i++) {
		text += "<th>";
		if (solve.start[i] != null && solve.end[i] != null) {
			text += solve.end[i]  + "</th>";
		} else {
			text += "--:--</th>";
		}
	}

	text += "</tr></tbody>"
	var frame = document.getElementById("dataTable");
	frame.innerHTML = text;
}
	
	
	
	var solve = {
		start: [],
		end: [],
		names: ["Cross", "F2L-1", "F2L-2", "F2L-3", "F2L-4", "OLL", "PLL"],
	};
</script>
<body>
  <!-- Navigation-->
<?php include "php/menu.php";?> 
 <div class="content-wrapper">
    <div class="container-fluid">
      <!-- Breadcrumbs-->
      <ol class="breadcrumb">
        <li class="breadcrumb-item">
          <a href="index.html">Dashboard</a>
        </li>
        <li class="breadcrumb-item active">Blank Page</li>
      </ol>
      <div class="row">
        <div class="col-12">
          <h1>Blank</h1>
		  <video id="video-active" width="640" height="264" controls>
  <source src= "video/solve.mp4" type="video/mp4">
Your browser does not support the video tag.
</video></br>
<button onClick="setTime()">Add TimeStamp</button><span id="time"></span>
<button onClick="removeTime()">Remove TimeStamp</button>
<button onClick="reset()">Reset TimeStamps</button></br>
<button onClick="speed(0.125)">-8x</span>
<button onClick="speed(0.25)">-4x</button>
<button onClick="speed(0.5)">-2x </button>
<button onClick="speed(1.0)">normal</button>
<button onClick="speed(2.0)">2x</button>
<br/>
<button onClick="frameStep(-5.0)"><i class="fa fa-fw fa-fast-backward"></i></button>
<button onClick="frameStep(-1.0)"><i class="fa fa-fw fa-step-backward"></i></button>
<button onClick="pause()"><i class="fa fa-fw fa-pause"></i></button>
<button onClick="frameStep(1.0)"><i class="fa fa-fw fa-step-forward"></i></button>
<button onClick="frameStep(5.0)"><i class="fa fa-fw fa-fast-forward"></i></button>

<div id="times"></div>

          <div class="table-responsive">
            <table class="table table-bordered" id="dataTable" width="100%" cellspacing="0">
              <thead>
                <tr>
                  <th>Name</th>
                  <th>Position</th>
                  <th>Office</th>
                  <th>Age</th>
                  <th>Start date</th>
                  <th>Salary</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>Tiger Nixon</td>
                  <td>System Architect</td>
                  <td>Edinburgh</td>
                  <td>61</td>
                  <td>2011/04/25</td>
                  <td>$320,800</td>
                </tr>
               
              </tbody>
            </table>
          </div>


        </div>
      </div>
    </div>
    <!-- /.container-fluid-->
    <!-- /.content-wrapper-->
<?php include 'footer.php';?>

<script>

$(document).ready(function(){
	load();
	var video = document.getElementById('video-active'),
    frameTime = 1 / 25; //assume 25 fps
		console.log("loaded");

window.addEventListener('keypress', function (evt) {
	console.log("typed");
        if (evt.keyCode === 37) { //left arrow
            if (video.currentTime > 0) {
                //one frame back
                video.currentTime -= frameTime;
            }
        } else if (evt.keyCode === 39) { //right arrow
            if (video.currentTime < video.duration) {
                //one frame forward
                //Don't go past the end, otherwise you may get an error
                video.currentTime = Math.min(video.duration, video.currentTime + frameTime);
            }
        }
			
});
});

</script>
  </div>
</body>

</html>
