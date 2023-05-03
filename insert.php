<!-- PHP CODE TO FETCH DATA FROM ROWS -->
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