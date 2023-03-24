<?php
  $ip = $_POST["ip"];
  $count = $_POST["count"];

  $filename = "visitors.txt";
  $file = fopen($filename, "w");
  fwrite($file, $count);
  fclose($file);
?>
