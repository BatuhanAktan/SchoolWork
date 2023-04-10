<html>
<head>
	<link rel="stylesheet" href="index.css">
</head>
<div class="topnav">
	<a href="restaurant.html"> Back </a>
	<a href="find.html"> Search for more </a>
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
	<div class="item2">
		<a>
			<?php 
			$date=$_POST['dateInput'];
			echo "Order Date: ";
			echo $date; 
			?>
			</a>
	</div>
	<div class="item3">
		<a>
			<?php 
			$date=$_POST['dateInput'];
			$sql="SELECT c.firstName, c.lastName, f.totalPrice, f.tip, e.firstName as 'dFirstName', e.lastName as 'dLastName' FROM customeraccount c, orderplacement o, foodorder f, employee e, delivery d WHERE o.orderTime='$date' AND o.customerEmail=c.emailAddress AND o.orderID=f.orderID AND o.orderID=d.orderID AND d.deliveryPerson=e.ID;";

			$q=$dbh->query($sql);
			
			try{
				if($q->rowCount()==0){
					echo "No Results";
				}else{
				while($item = $q->fetch()){
							echo "<table class='tableCenter' border='4'>
							<tr>
							<th> Customer First Name </th>
							<th> Customer Last Name </th>
							<th>Total Price </th>
							<th> Tip </th>
							<th> Employee First Name </th>
							<th> Employee Last Name </th>
							</tr>";
							echo "<tr>
									<td> $item[firstName] </td>
									<td> $item[lastName] </td>
									<td> $item[totalPrice] </td>
									<td> $item[tip] </td>
									<td> $item[dFirstName] </td>
									<td> $item[dLastName] </td>
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
