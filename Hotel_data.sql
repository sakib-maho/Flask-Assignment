-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Dec 10, 2021 at 01:16 PM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 8.0.13

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `My_hotel`
--

-- --------------------------------------------------------

--
-- Table structure for table `Hotel_data`
--

CREATE TABLE `Hotel_data` (
  `Title` varchar(255) NOT NULL,
  `Sleeps` varchar(255) DEFAULT NULL,
  `Bedrooms` varchar(255) DEFAULT NULL,
  `Bathrooms` varchar(255) DEFAULT NULL,
  `Price` varchar(255) DEFAULT NULL,
  `Picture_1` varchar(255) DEFAULT NULL,
  `Picture_2` varchar(255) DEFAULT NULL,
  `Picture_3` varchar(255) DEFAULT NULL,
  `Location` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `Hotel_data`
--

INSERT INTO `Hotel_data` (`Title`, `Sleeps`, `Bedrooms`, `Bathrooms`, `Price`, `Picture_1`, `Picture_2`, `Picture_3`, `Location`) VALUES
('A Pinch of Paradise at Edgewater Beach and Golf Resort', '4', '1', '2', '93', '[\'https://media.vrbo.com/lodging/73000000/72630000/72626000/72625904/4e492c08.c6.jpg\']', '[\'https://media.vrbo.com/lodging/73000000/72630000/72626000/72625904/96a751d2.c6.jpg\']', '[\'https://media.vrbo.com/lodging/73000000/72630000/72626000/72625904/4f00df2f.c6.jpg\']', 'Panama'),
('Gorgeous Oceanfront Condo-Beach Service Incl-Huge Balcony-Great Rates-Pier Park', '6', '2', '2', '90', '[\'https://media.vrbo.com/lodging/23000000/22500000/22492400/22492314/90-8531ed78.c6.jpg\']', '[\'https://media.vrbo.com/lodging/23000000/22500000/22492400/22492314/8e64ad8f.c6.jpg\']', '[\'https://media.vrbo.com/lodging/23000000/22500000/22492400/22492314/e4e4ba3c.c6.jpg\']', 'Panama'),
('Gulf Front w/ Pool!! Walk To Pier Park & Gulf World! Brand new! Dog friendly!', '4', '1', '1', '145', '[\'https://media.vrbo.com/lodging/26000000/25740000/25730400/25730372/11debc90.c6.jpg\']', '[\'https://media.vrbo.com/lodging/26000000/25740000/25730400/25730372/e5616dea.c6.jpg\']', '[\'https://media.vrbo.com/lodging/26000000/25740000/25730400/25730372/31c40138.c6.jpg\']', 'Panama'),
('New- Beach Front -4 Bedroom 3 Bath-Best View- Best Price and Luxury -2 Masters', '8', '4', '3', '175', '[\'https://media.vrbo.com/lodging/35000000/34160000/34157000/34156929/6dab554f.c6.jpg\']', '[\'https://media.vrbo.com/lodging/35000000/34160000/34157000/34156929/b83a119b.c6.jpg\']', '[\'https://media.vrbo.com/lodging/35000000/34160000/34157000/34156929/607ed78e.c6.jpg\']', 'Panama'),
('Stunning Gulf-Front Condo w/Balcony, Shared Pool, Hot Tub, Gym, Beach Views', '8', '3', '2', '123', '[\'https://media.vrbo.com/lodging/73000000/72540000/72537600/72537516/cf1151bf.c6.jpg\']', '[\'https://media.vrbo.com/lodging/73000000/72540000/72537600/72537516/015569ad.c6.jpg\']', '[\'https://media.vrbo.com/lodging/73000000/72540000/72537600/72537516/09bf67f7.c6.jpg\']', 'Panama'),
('Walk Out 2 Beach Ground Floor No Elevators!', '4', '1', '1', '55', '[\'https://media.vrbo.com/lodging/35000000/34330000/34326500/34326477/f3b9560a.c6.jpg\']', '[\'https://media.vrbo.com/lodging/35000000/34330000/34326500/34326477/e0a34376.c6.jpg\']', '[\'https://media.vrbo.com/lodging/35000000/34330000/34326500/34326477/d2fabeb9.c6.jpg\']', 'Panama');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `Hotel_data`
--
ALTER TABLE `Hotel_data`
  ADD PRIMARY KEY (`Title`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
