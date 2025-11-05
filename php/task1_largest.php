<?php
// Task 1: Largest of three numbers using nested if
$a = 12;
$b = 25;
$c = 7;

if ($a >= $b) {
    if ($a >= $c) {
        $largest = $a;
    } else {
        $largest = $c;
    }
} else { // $b > $a
    if ($b >= $c) {
        $largest = $b;
    } else {
        $largest = $c;
    }
}

echo "Input numbers: $a, $b, $c\n";
echo "Largest number is: $largest\n";
