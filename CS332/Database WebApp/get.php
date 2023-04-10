<html>
<head>
	<link rel="stylesheet" href="index.css">
</head>
<div class="topnav">
	<a href="restaurant.html"> Back </a>
	<a href="schedules.php"> Search for more </a>
</div>
<div class="container">

	<div class="item1">
		<a>
			<?php
			try {
				$dbh = new 
				PDO('mysql:host=localhost;dbname=restaurant',"root","");
				echo "Connected";
			}
			catch (PDOException $e) {
			print "Error!: " . $e->getMessage() . "<br/>";
			die(); 
			}
			?>
		</a>
	</div>
	<div class="item3">
		<a>
			<?php 
			$employee=$_POST['employees'];
			$sql="SELECT e.ID, e.firstName, e.lastName, s.day, s.startTime, s.endTime FROM employee e, shift s WHERE
				s.empID='$employee' AND s.empID=e.ID AND s.day NOT IN ('Saturday', 'Sunday');";

			$q=$dbh->query($sql);
			
			try{
				if($q->rowCount()==0){
					echo "No Results";
				}else{
				echo "<table class='tableCenter' border='4'>
						<tr>
						<th> Employee ID </th>
						<th> First Name </th>
						<th> Last Name </th>
						<th> Day </th>
						<th> Start </th>
						<th> End </th>
						</tr>";
				while($item = $q->fetch()){
							echo "<tr>
									<td> $item[ID] </td>
									<td> $item[firstName] </td>
									<td> $item[lastName] </td>
									<td> $item[day] </td>
									<td> $item[startTime] </td>
									<td> $item[endTime] </td>
								  </tr>";
						
					}
					echo "</table>";
				}
			} catch (Exception) {
				echo "Something went Wrong, ".$e;
			}
			?>
		</a>
	</div>
</div>