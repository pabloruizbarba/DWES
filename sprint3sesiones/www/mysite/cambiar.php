<?php
	$db = mysqli_connect('localhost','root','1234','mysitedb') or die('Fail');

	session_start();
	$user = 'NULL';
	if (!empty($_SESSION['user_id'])) {
		$user = $_SESSION['user_id'];
	}
	
	$old=$_POST['old'];
	$new=$_POST['new'];
	$new2=$_POST['new2'];

	echo "El usuario actual tiene id = ".$user;
	$query="select contraseña from tUsuarios where id=".$user;
	$result = mysqli_query($db, $query) or die('Query error');

	if(mysqli_num_rows($result) > 0){
		$only_row = mysqli_fetch_array($result);
		if($only_row[0] == $old){
			if($new2 == $new){
				echo "<p>La nueva clave es: ".$new2;
				echo "</p><br>";
				$query2 = "UPDATE tUsuarios SET contraseña = '".$new."' where id =".$user;
				$result = mysqli_query($db, $query2) or die('Query error');

				echo '<p>Se ha actualizado la clave</p>';
			} else {
				echo '<p>Las nuevas claves no son iguales</p>';
			}
		} else {
			echo '<p>Clave incorrecta</p>';
		}
	} else {
		echo '<p>El usuario con ese email no consta en el registro</p>';
	}		
	mysqli_close($db);   
?>  


