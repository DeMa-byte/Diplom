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
