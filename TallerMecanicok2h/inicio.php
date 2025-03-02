<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Taller mecánico K2H</title>
    <link rel="stylesheet" href="VIEW/inicio.css">
</head>
<body>
    
    <div class="container">

        <img src="media\logok2h.png" alt="K2H Logo" class="logo">
    
        <button class="main-btn" onclick="irIniciodeSesion()">INICIAR SESIÓN</button>
    
        <a href="PHP/registro.php" class="register-link">REGISTRARTE</a>
    
    </div>

    <script>
        function irIniciodeSesion(){
            window.location.href = "PHP/iniciodesesion.php";
        }
    </script>

</body>
</html>


