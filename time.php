<?php
// return timestamp for Jan 5 2008 10:16:

echo mktime(10, 16, 00, 1, 5, 2008);
echo "<br />";
?>

<?php
// return timestamp for now
echo 'Current Unix time: ' . mktime();
echo "<br />";
?>

<?php
// get current date and time as array
$now = getdate();

// output: 'It is now ....'
echo 'It is now ' . $now['hours'] . ':' . $now['minutes'] . ':' . $now['seconds'] . ' on ' . $now['mday'] . '-'
 . $now['mon'] . '-' . $now ['year'];
 $now = getdate();
 echo "<br />";
 ?>

 <?php
    echo 'It is now ' . date("h:i a d M Y", mktime(12, 28, 13, 3, 20, 2008));
    echo "<br />";
    echo 'It is now ' . date("H:i d F Y", mktime(8, 15, 0, 2, 14, 2008));
    echo "<br />";
    echo 'Today\'s date is ' . date("M-d-Y", mktime(0, 0, 0, 10, 5, 2007));
?>

<?php
 echo "<br />";
// output: 'Date is invalid'
if (checkdate(2,30,2008)) {
echo 'Date is valid';
} else {
echo 'Date is invalid';
}
echo "<br />";
?>

<?php
    echo date('d M y', strtotime('next Tuesday'));
    echo "<br />";
    echo date("d M Y", strtotime('7 Months ago'));
    echo "<br />";
?>

<?php
    echo date('D', mktime(0,0,0, 17, 9, 1977));
    echo "<br />";
?>

<?php
    foreach(range(1,12) as $m) {
        $months[] = date('F', mktime(0,0,0,$m,1,0));
    }
    echo implode($months, ', ');
    echo "<br />";
?>

<?php
    foreach(range(1,7) as $d) {
        $days[] = date('D', mktime(0,0,0,0,$d,0));
    }
    echo implode($days, ', ');
?>

