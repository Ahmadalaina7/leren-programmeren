<?php
            $huidigUur = date('H');

            if($huidigUur > 18){
                $hallo = 'Goede avond';
                $achtergrond = 'evening';

            }
            elseif($huidigUur > 12){
                $hallo = 'Goede middag';
                $achtergrond = 'afternoon';

            }
            elseif($huidigUur > 6){
                $hallo = 'Goede morgen';
                $achtergrond = 'morning';
            }
            else{
                $hallo = 'Goede Nacht';
                $achtergrond= 'night';
            }
            ?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Eindopdracht van de intro</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body class= "<?php echo $achtergrond;?>">
    <h1><?php echo $hallo; ?></h1>
    <h1> Het is nu <?php echo date("H:i"); ?> </h1>


    </div>
</body>
</html>
