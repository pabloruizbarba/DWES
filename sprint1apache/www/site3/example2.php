<html>
	<body>
		<h1>Página de bienvenida</h1>
		<?php
			function dar_bienvenida($nombre) {
				echo "¡Bienvenido, " . $nombre . "!";
			}

			dar_bienvenida("Jean claude Van Damme");
		?>
	</body>
</html>
