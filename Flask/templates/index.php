<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Web service REST Básico</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/styles.css') }}">
</head>

<body>
    <div class="head">
        <h1>Bienvenido al web server REST con flask</h1>
        <img src="{{ url_for('static', filename='images/rest.jpeg')}}" alt="REST" class="center">
    </div>
    <div class="block">
        <h2>
            Integrantes del equipo
        </h2>
        <ul class="list">
            <li>Paula Pérez Benítez</li>
            <li>Marcel Fernández de la Peña </li>
            <li>Victor Ramos Cruz</li>
            <li>Ricardo Saldaña Zepeda</li>
            <li>Florentino Ángel Pérez Arce</li>
        </ul>
    </div>
</body>

</html>