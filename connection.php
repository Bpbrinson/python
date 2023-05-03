<?php
// Connect to database
$servername = "finance.c2kupgap5up8.us-east-1.rds.amazonaws.com";
$username = "Brandon";
$password = "PfjRn7jk7598";
$dbname = "finance";
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}

// Select data from table
$sql = "SELECT * FROM finance";
$result = $conn->query($sql);

// Close connection
$conn->close();
?>
