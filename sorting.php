<?php
$numbers = array(3, 25, 1, 6, 23, 56);

function permutation($numbers, $i) {
    $temp = current($numbers);
    current($numbers) = current($numbers+1);
    current($numbers+1) = $temp;
    return true;
    
}

$sorted = false;

while ($sorted == false) {
    $moved = false;
    $i = 0;
    while ($i < count($numbers) - 1) {
        if (current($numbers+1) < current($numbers)) {
            $moved = permutation($numbers, i);
        }
        $i = $i+1;
    }
    if ($moved == false) {
        $sorted = true;
    }
}
        
echo $numbers;
?>