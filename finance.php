<!DOCTYPE html>
<html>
  <head>
    <title>My Webpage</title>
    <link rel="stylesheet" type="text/css" href="main.css" />
  </head>
  <body>
    <header>
      <h1>Welcome to Brandon's Webpage</h1>
    </header>

    <nav>
      <ul>
        <li><a href="index.html">Home</a></li>
        <li><a href="aspirations.php">Aspirations</a></li>
        <li><a href="finance.php">Finance</a></li>
      </ul>
    </nav>

    <body>
      <?php
      ini_set('display_errors', 1);
      include_once('connection.php');
      $query="SELECT * FROM finance";
      $result = $conn->query($query);
      $conn->close();
      
      ?>
      <br><br>
      <table class="table">
        <tr>
          <th>Date</th>
          <th>BoA Checkings</th>
          <th>BoA Savings (Vacation)</th>
          <th>BoA Savings Apt./Rainy</th>
          <th>BoA Credit</th>
          <th>BoA Statement</th>
          <th>Amex Credit</th>
          <th>Amex Statement</th>
          <th>Capital One Venture X</th>
          <th>Venture X Statement</th>
          <th>Capital One Savor</th>
          <th>Savor Statement</th>
          <th>Total Credit Debt</th>
          <th>Etrade</th>
		</tr>
    <?php
    while($rows=mysqli_fetch_assoc($result))
    {
    ?>
    <tr>
        <!-- FETCHING DATA FROM EACH
        ROW OF EVERY COLUMN -->
        <td><?php echo $rows['date']; ?></td>
        <td><?php echo $rows['boa_checking']; ?></td>
        <td><?php echo $rows['boa_savings_vacation']; ?></td>
        <td><?php echo $rows['boa_savings_apt']; ?></td>
        <td><?php echo $rows['boa_credit']; ?></td>
        <td><?php echo $rows['boa_statement']; ?></td>
        <td><?php echo $rows['amex_credit']; ?></td>
        <td><?php echo $rows['amex_statement']; ?></td>
        <td><?php echo $rows['capital_one_venture_x']; ?></td>
        <td><?php echo $rows['capital_one_venture_x_statement']; ?></td>
        <td><?php echo $rows['capital_one_savor']; ?></td>
        <td><?php echo $rows['capital_one_savor_statement']; ?></td>
        <td><?php echo $rows['total_credit_debt']; ?></td>
        <td><?php echo $rows['total_amount']; ?></td>
        <td><?php echo $rows['etrade']; ?></td>
    </tr>
    <?php
    }
    ?>
	</table>
    <footer>
      <p>&copy; 2023 My Webpage</p>
    </footer>
  </body>
</html>
