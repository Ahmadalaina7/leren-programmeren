<?php
function sort_lijst_asc($getal) {
    $to_sort = true;
    while ($to_sort) {
        $to_sort = false;
        for ($x = 0; $x < count($getal) - 1; $x++) {
            if ($getal[$x] > $getal[$x + 1]) {
                $temp = $getal[$x];
                $getal[$x] = $getal[$x + 1];
                $getal[$x + 1] = $temp;
                $to_sort = true;
            }
        }
    }
    return $getal;
}

print_r(sort_lijst_asc([5, 3, 2]));
?>