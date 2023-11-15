<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="styles.css">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>

</head>

<body>
    <h1>"De ingevulde gegevens zijn:"</h1>
    <?php
    $naam = $_POST['naam'];
    echo "Naam: " . $naam;
    echo "<br>";
    $number = $_POST['number'];
    echo "Age: " . $number;
    echo "<br>";
    $email = $_POST['email'];
    echo "Email: " . $email;
    echo "<br>";
    $password = $_POST['password'];
    echo "Password: " . $password;










    ?>

</body>

</html>