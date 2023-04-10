<html>
<head>
	<link rel="stylesheet" href="index.css">
	<meta content="text/html; charset=utf-8" http-equiv="Content-Type">
</head>
<div class="topnav">
	<a href="restaurant.html"> Back </a>
</div>
<div class="container">
	<div class="item3">
		<a>
			<?php 
			try {
				$dbh = new 
				PDO('mysql:host=localhost;dbname=restaurant',"root","");
			}
			catch (PDOException $e) {
			print "Error!: " . $e->getMessage() . "<br/>";
			die(); 
			}

			$sql="SELECT date(orderTime) as dateoforder, COUNT(orderID) as number FROM orderplacement GROUP BY orderTime; ";

			$q=$dbh->query($sql);
			
			try{
				if($q->rowCount()==0){
					echo "No Results";
				}else{
				while($item = $q->fetch()){
							echo "<table class='tableCenter' border='4'>
							<tr>
							<th> Date </th>
							<th> Number of Orders</th>
							</tr>";
							echo "<tr>
									<td> $item[dateoforder] </td>
									<td> $item[number] </td>
								  	</tr>";
								  echo "</table>";
						
					}
				}
			} catch (Exception) {
				echo "Something went Wrong, ".$e;
			}
			?>
		</a>
	</div>
</div>
