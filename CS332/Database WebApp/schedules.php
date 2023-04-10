<html>
<head>
	<link rel="stylesheet" href="index.css">
</head>
<div class="topnav">
	<a href="restaurant.html"> Back </a>
</div>
<h1 class="order-list"> Find Orders </h1> 
<br> 
<br>
<div class="orderDate">
<form action="get.php" method="post">
  <label for="employees">Choose an employee:</label>
  <select name="employees" id="employees">
  	<?php 
			try {
				$dbh = new 
				PDO('mysql:host=localhost;dbname=restaurant',"root","");
			}
			catch (PDOException $e) {
			print "Error!: " . $e->getMessage() . "<br/>";
			die(); 
			}

			$sql="SELECT ID, firstName, lastName FROM employee;";

			$q=$dbh->query($sql);
			
			try{
				if($q->rowCount()==0){
					echo "No Results";
				}else{
				while($item = $q->fetch()){
						echo "<option value='$item[ID]'> $item[firstName] $item[lastName]</option>";
					}
				}
			} catch (Exception) {
				echo "Something went Wrong, ".$e;
			}
			?>
  </select>
  <br><br>
  <input type="submit" value="Submit">
</form>
<br> 
</div> 
</html>