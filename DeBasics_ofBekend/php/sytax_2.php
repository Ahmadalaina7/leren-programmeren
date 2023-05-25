<?php 
function langste_woord($woordenlijst) {
    $langsteWoord = '';

foreach ($woordenlijst as $woord) {
    if(strlen ($woord) > strlen($langsteWoord)){
        $langsteWoord = $woord;
        }
        
    }

return $langsteWoord;

}

 

$woordenlijst =  ['kat', 'hond', 'olifant'] ;

$result = langste_woord($woordenlijst);

echo $result; // Output: 6
