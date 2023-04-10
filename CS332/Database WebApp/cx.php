<html>
<head>
	<link rel="stylesheet" href="index.css">
</head>
<div class="topnav">
	<a href="restaurant.html"> Back </a>
	<a href="cx.html"> Add More </a>
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
			$email=$_POST['email'];
			$fname=$_POST['fname'];
			$lname=$_POST['lname'];
			$cell=$_POST['cell'];
			$street=$_POST['street'];
			$city=$_POST['city'];
			$pc=$_POST['pc'];

			$sql="INSERT INTO customeraccount (emailAddress, firstName, lastName, cellNum, streetAddress, city, pc, creditAmt) VALUES ('$email', '$fname', '$lname', '$cell', '$street', '$city', '$pc', 5);";

			$check="SELECT * FROM customeraccount WHERE emailAddress='$email';";


			$q=$dbh->query($check);
			try{
				if($q->rowCount()==0){
					$dbh->exec($sql);
					echo "Added to the Database";
					$q=$dbh->query("SELECT * FROM customeraccount");
					echo "<table class='tableCenter' border='4'>
							<tr>
							<th> Customer Email </th>
							<th> First Name </th>
							<th> Last Name </th>
							<th> Cell Number </th>
							<th> Street Address </th>
							<th> City </th>
							<th> Postal Code </th>
							<th> Credit </th>
							</tr>";
					while($item = $q->fetch()){
							echo "<tr>
									<td> $item[emailAddress] </td>
									<td> $item[firstName] </td>
									<td> $item[lastName] </td>
									<td> $item[cellNum] </td>
									<td> $item[streetAddress] </td>
									<td> $item[city] </td>
									<td> $item[pc] </td>
									<td> $item[creditAmt] </td>
								  </tr>";
						
					}
					echo "</table>";
				}else{
					echo "<h1> Customer Already in DB </h1>";
				}
			} catch (Exception) {
				echo "Something went Wrong, ".$e;
			}
			?>
		</a>
	</div>
</div>
