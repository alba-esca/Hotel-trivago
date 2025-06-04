-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 04, 2025 at 06:47 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `hospedaje`
--

-- --------------------------------------------------------

--
-- Table structure for table `habitacion`
--

CREATE TABLE `habitacion` (
  `cod_hab` varchar(4) NOT NULL COMMENT 'Código de la habitación',
  `num_hab` varchar(4) NOT NULL COMMENT 'Número de la habitación',
  `tip_hab` char(1) NOT NULL DEFAULT 'N' COMMENT 'Tipo de habitación (N normal, E ejecutiva, S suite)',
  `cap_hab` char(1) NOT NULL DEFAULT 'I' COMMENT 'Capacidad de la habitación (I individual, M matrimonial, D doble, T triple)',
  `pre_hab` decimal(12,2) NOT NULL DEFAULT 0.00 COMMENT 'Precio de la habitación',
  `sta_hab` char(1) NOT NULL DEFAULT 'D' COMMENT 'Status de la habitación (O ocupada, D desocupada)'
) ENGINE=InnoDB DEFAULT CHARSET=utf16 COLLATE=utf16_spanish_ci COMMENT='Tabla que almacena la información de las habitaciones';

-- --------------------------------------------------------

--
-- Table structure for table `huesped`
--

CREATE TABLE `huesped` (
  `ced_hue` int(10) UNSIGNED NOT NULL COMMENT 'Cédula del huésped',
  `ape_hue` varchar(50) NOT NULL COMMENT 'Apellidos del huésped',
  `nom_hue` varchar(50) NOT NULL COMMENT 'Nombres del huésped',
  `dir_hue` varchar(100) NOT NULL COMMENT 'Dirección del huésped',
  `ciu_hue` varchar(30) NOT NULL COMMENT 'Ciudad del huésped',
  `email_hue` varchar(70) NOT NULL COMMENT 'Email del huésped',
  `tel_hue` varchar(12) NOT NULL COMMENT 'Teléfono del huésped'
) ENGINE=InnoDB DEFAULT CHARSET=utf16 COLLATE=utf16_spanish_ci COMMENT='Tabla que guarda información de los huéspedes del hotel';

-- --------------------------------------------------------

--
-- Table structure for table `ingreso`
--

CREATE TABLE `ingreso` (
  `cod_ing` int(10) UNSIGNED NOT NULL COMMENT 'Código de ingreso',
  `ced_hue` int(10) UNSIGNED NOT NULL COMMENT 'Cédula del huésped',
  `cod_hab` varchar(4) NOT NULL COMMENT 'Código de habitación del huésped',
  `fec_ing` datetime NOT NULL DEFAULT current_timestamp() COMMENT 'Fecha de ingreso del huésped',
  `fec_sal` datetime NOT NULL COMMENT 'Fecha de salida del huésped',
  `can_per` tinyint(3) UNSIGNED NOT NULL DEFAULT 1 COMMENT 'Cantidad de personas que ocupan la habitación'
) ENGINE=InnoDB DEFAULT CHARSET=utf16 COLLATE=utf16_spanish_ci COMMENT='Tabla que registra los ingresos de los huéspedes en el hotel';

-- --------------------------------------------------------

--
-- Table structure for table `usuarios`
--

CREATE TABLE `usuarios` (
  `id` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `usuarios`
--

INSERT INTO `usuarios` (`id`, `username`, `password`) VALUES
(1, 'admin', '1234');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `habitacion`
--
ALTER TABLE `habitacion`
  ADD PRIMARY KEY (`cod_hab`) USING BTREE;

--
-- Indexes for table `huesped`
--
ALTER TABLE `huesped`
  ADD PRIMARY KEY (`ced_hue`) USING BTREE;

--
-- Indexes for table `ingreso`
--
ALTER TABLE `ingreso`
  ADD PRIMARY KEY (`cod_ing`),
  ADD KEY `FK_huesped` (`ced_hue`),
  ADD KEY `FK_habitacion` (`cod_hab`);

--
-- Indexes for table `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `ingreso`
--
ALTER TABLE `ingreso`
  MODIFY `cod_ing` int(10) UNSIGNED NOT NULL AUTO_INCREMENT COMMENT 'Código de ingreso';

--
-- AUTO_INCREMENT for table `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `ingreso`
--
ALTER TABLE `ingreso`
  ADD CONSTRAINT `FK_habitacion` FOREIGN KEY (`cod_hab`) REFERENCES `habitacion` (`cod_hab`) ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_huesped` FOREIGN KEY (`ced_hue`) REFERENCES `huesped` (`ced_hue`) ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
