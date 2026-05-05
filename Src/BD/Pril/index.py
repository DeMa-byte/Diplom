<?php
require_once 'config.php';

// Получаем статистику
$totalCars = $pdo->query("SELECT COUNT(*) FROM Avtomobili")->fetchColumn();
$totalDrivers = $pdo->query("SELECT COUNT(*) FROM Voditeli")->fetchColumn();
$totalRepairs = $pdo->query("SELECT SUM(stoimost) FROM Remonty")->fetchColumn();

// Последние ремонты
$recentRepairs = $pdo->query("
    SELECT r.*, a.gos_nomer 
    FROM Remonty r 
    JOIN Avtomobili a ON r.id_auto = a.id_auto 
    ORDER BY r.data_remonta DESC 
    LIMIT 5
")->fetchAll();
?>
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Автопарк - Учёт транспорта</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="container">
        <h1>🚛 Система учёта автопарка</h1>
        
        <div class="stats">
            <div class="stat-card">
                <h3>🚗 Автомобилей</h3>
                <p class="number"><?= $totalCars ?></p>
            </div>
            <div class="stat-card">
                <h3>👨‍✈️ Водителей</h3>
                <p class="number"><?= $totalDrivers ?></p>
            </div>
            <div class="stat-card">
                <h3>💰 Расходы на ремонт</h3>
                <p class="number"><?= number_format($totalRepairs, 0, '.', ' ') ?> ₽</p>
            </div>
        </div>

        <div class="menu">
            <a href="cars.php" class="btn">🚗 Автомобили</a>
            <a href="drivers.php" class="btn">👨‍✈️ Водители</a>
            <a href="mileage.php" class="btn">📊 Пробег</a>
            <a href="repairs.php" class="btn">🔧 Ремонты</a>
        </div>

        <h2>Последние ремонты</h2>
        <table class="table">
            <tr>
                <th>Автомобиль</th>
                <th>Дата</th>
                <th>Тип ремонта</th>
                <th>Стоимость</th>
            </tr>
            <?php foreach($recentRepairs as $repair): ?>
            <tr>
                <td><?= htmlspecialchars($repair['gos_nomer']) ?></td>
                <td><?= $repair['data_remonta'] ?></td>
                <td><?= htmlspecialchars($repair['tip_remonta']) ?></td>
                <td><?= number_format($repair['stoimost'], 0, '.', ' ') ?> ₽</td>
            </tr>
            <?php endforeach; ?>
        </table>
    </div>
</body>
</html>