<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Web service REST Básico</title>
</head>

<body>
    <?php
    $data = 'http://127.0.0.1:5000//products/mouse';
    $datajson = file_get_contents($data);
    $produts = json_decode($datajson);
    foreach ($product as $product) {
        echo "<p>" . $product->products . "</p>";
    }
    ?>
</body>

</html>