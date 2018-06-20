<!DOCTYPE html>
<html>
    <head>
	<?php 
			include "php/general_head.php";
?>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
  		<script src="js/stopwatch.js"></script>
        <script src="js/scripts.js"></script>


    </head>
    <body>
        <header>
            <?php 
			include "php/header.php";
			include "php/menu.php";
		?>
        </header>
        <div id="cube-menu">
            <button class="item active" onclick="openCube('2x2', this)">
                2x2
            </button>
            <button class="item" onclick="openCube('3x3', this)">
                3x3
            </button>
            <button class="item" onclick="openCube('4x4', this)">
                4x4
            </button>
            <button class="item" onclick="openCube('5x5', this)">
                5x5
            </button>
            <button class="item" onclick="openCube('pyraminx', this)">
                Pyraminx
            </button>
        </div>
        <div id="main-container">
            <div id="time-container">
            <div id="timing-box">
            	<div id="scramble-container">
            	<div id="scramble">
            		F2 R2 D2 F R R'
            	</div>
            	<div id="time">
					<span class="current-time"></span>

    </div>
            </div>
            </div>
            <div id="statistics-box">
            	<h4>Results</h4>
            	<ol id="results_list">
            		<li> 20.187
            		</li>
            		<li> 30.265
            		</li>

            	</ol>
            </div>
        </div>
        </div>
        
        </script>
    </body>
</html>