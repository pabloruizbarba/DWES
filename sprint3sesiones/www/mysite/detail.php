<?php
	$db = mysqli_connect('172.16.0.2','root','1234','mysitedb') or die('Fail');
?>
<html>
<body>
	<?php
		if (!isset($_GET['pelicula_id'])) {
			die('No se ha especificado la pelicula');
		}
		$pelicula_id = $_GET['pelicula_id'];
		$query = 'SELECT * FROM tPeliculas where id='.$pelicula_id;
		$result = mysqli_query($db, $query) or die('Query error');
		$only_row = mysqli_fetch_array($result);
		echo '<h1>'.$only_row['nombre'].'</h1>';
		echo '<h2>'.$only_row['anyo'].'</h2>';
	?>
	<h3>Comentarios:</h3>
	<ul>
		<?php
			$query2 = 'SELECT * FROM tComentarios c join tUsuarios u  on u.id=c.usuario_id WHERE c.pelicula_id='.$pelicula_id;
			$result2 = mysqli_query($db, $query2) or die('Query Error');
			while ($row = mysqli_fetch_array($result2)) {
				echo '<li>'.$row['nombre'].' : ' .$row['comentario'].' '.$row['fecha'].'</li>';
			}
			mysqli_close($db);
		?>
	</ul>
	<p>Deja un nuevo comentario:</p>
	<form action="/comment.php" method="post">
		<textarea rows="4" cols="50" name="new_comment"></textarea><br>
		<input type="hidden" name="pelicula_id" value="<?php echo $pelicula_id; ?>">
		<input type="submit" value="Comentar">
	</form>
	<a href="/logout.php">Logout</a>
</body>
</html>
