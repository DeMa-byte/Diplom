-- Создание базы данных
CREATE DATABASE IF NOT EXISTS avtopark;
USE avtopark;

-- Таблица "Автомобили"
CREATE TABLE Avtomobili (
    id_auto INT AUTO_INCREMENT PRIMARY KEY,
    gos_nomer VARCHAR(10) NOT NULL UNIQUE,
    marka VARCHAR(50) NOT NULL,
    model VARCHAR(50) NOT NULL,
    god_vypuska INT,
    nachalnyy_probeg INT DEFAULT 0
);

-- Таблица "Водители"
CREATE TABLE Voditeli (
    id_driver INT AUTO_INCREMENT PRIMARY KEY,
    fio VARCHAR(100) NOT NULL,
    voditelskoe_udostoverenie VARCHAR(20) UNIQUE,
    data_priema DATE
);

-- Таблица "Пробег"
CREATE TABLE Probeq (
    id_probeg INT AUTO_INCREMENT PRIMARY KEY,
    id_auto INT NOT NULL,
    id_driver INT NOT NULL,
    data_zapisi DATE NOT NULL,
    probeg_km INT NOT NULL,
    comment TEXT,
    FOREIGN KEY (id_auto) REFERENCES Avtomobili(id_auto) ON DELETE CASCADE,
    FOREIGN KEY (id_driver) REFERENCES Voditeli(id_driver) ON DELETE CASCADE
);

-- Таблица "Ремонты"
CREATE TABLE Remonty (
    id_remont INT AUTO_INCREMENT PRIMARY KEY,
    id_auto INT NOT NULL,
    data_remonta DATE NOT NULL,
    tip_remonta VARCHAR(50),
    opisanie TEXT,
    probeg_na_moment INT,
    stoimost DECIMAL(10,2),
    FOREIGN KEY (id_auto) REFERENCES Avtomobili(id_auto) ON DELETE CASCADE
);

-- Добавляем автомобили
INSERT INTO Avtomobili (gos_nomer, marka, model, god_vypuska, nachalnyy_probeg) VALUES
('А123ВС77', 'KAMAZ', '5490', 2020, 15000),
('В456ОК77', 'ГАЗ', 'Газель NEXT', 2021, 5000),
('Е789АВ77', 'Toyota', 'Camry', 2019, 80000);

-- Добавляем водителей
INSERT INTO Voditeli (fio, voditelskoe_udostoverenie, data_priema) VALUES
('Иванов Иван Иванович', '77 01 123456', '2023-01-15'),
('Петров Петр Петрович', '77 02 654321', '2023-03-10');

-- Добавляем пробег
INSERT INTO Probeq (id_auto, id_driver, data_zapisi, probeg_km, comment) VALUES
(1, 1, '2025-04-01', 15200, 'Москва – Тула'),
(1, 1, '2025-04-02', 15450, 'Тула – Москва'),
(2, 2, '2025-04-01', 5200, 'по городу');

-- Добавляем ремонты
INSERT INTO Remonty (id_auto, data_remonta, tip_remonta, opisanie, probeg_na_moment, stoimost) VALUES
(1, '2025-03-15', 'ТО', 'замена масла, фильтров', 15100, 8500.00),
(2, '2025-03-20', 'текущий', 'замена тормозных колодок', 5100, 3200.00);
