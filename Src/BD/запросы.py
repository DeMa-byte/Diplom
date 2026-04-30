--Текущий пробег кадого автомобиля
    SELECT 
    a.gos_nomer,
    a.marka,
    MAX(p.probeg_km) AS tekuciy_probeg
FROM Avtomobili a
LEFT JOIN Probeq p ON a.id_auto = p.id_auto
GROUP BY a.id_auto;

--Все ремонты за последние 3 месяца
SELECT 
    a.gos_nomer,
    r.data_remonta,
    r.tip_remonta,
    r.opisanie,
    r.stoimost
FROM Remonty r
JOIN Avtomobili a ON r.id_auto = a.id_auto
WHERE r.data_remonta >= CURDATE() - INTERVAL 3 MONTH
ORDER BY r.data_remonta DESC;

--Какой водитель на каких машинах ездил
SELECT 
    v.fio,
    a.gos_nomer,
    COUNT(p.id_probeg) AS kolichestvo_poezdok
FROM Probeq p
JOIN Voditeli v ON p.id_driver = v.id_driver
JOIN Avtomobili a ON p.id_auto = a.id_auto
GROUP BY v.id_driver, a.id_auto;


