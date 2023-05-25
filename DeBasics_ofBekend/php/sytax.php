<?php 
function lijst_optellen($numbers) {
    $sum = 0;

foreach ($numbers as $number) {
    if($number % 2 == 0){
        $sum += $number;
        }
        
    }

return $sum;

}

 

$getallenLijst = [1, 2, 3, 4 , 5 , 6 , 7 , 8];

$result = lijst_optellen($getallenLijst);

echo $result; // Output: 6
