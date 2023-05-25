<!DOCTYPE html>
<html>
<head>
</head>

<body>

<form action="" method="post">
Naam:<input type="text" name="naam"><br>

age:<input type="text" name="number"><br>

email:<input type="text" name="email"><br>

<input type="submit" name="submit" value="verzenden">

</form>

<?php

$email=$_POST['email'];

if(filter_var($email, FILTER_VALIDATE_EMAIL) ) {
print"het emailadres is juist";

}else {
print"het emailadres is niet juist, probeer het opnieuw";

}

$age=$_POST['number'];


if(filter_var($age, FILTER_VALIDATE_INT)) {
print"$age is een getal";

}else {
print"$age is geen getal, probeer het opnieuw";

}

?>


</body>
</html>