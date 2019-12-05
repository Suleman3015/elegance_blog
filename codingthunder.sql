-- phpMyAdmin SQL Dump
-- version 4.9.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 05, 2019 at 10:48 AM
-- Server version: 10.4.8-MariaDB
-- PHP Version: 7.1.33

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `codingthunder`
--

-- --------------------------------------------------------

--
-- Table structure for table `contact`
--

CREATE TABLE `contact` (
  `sno` int(12) NOT NULL,
  `name` text NOT NULL,
  `phone_num` int(12) NOT NULL,
  `msg` varchar(200) NOT NULL,
  `date` datetime(6) DEFAULT current_timestamp(6),
  `email` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `contact`
--

INSERT INTO `contact` (`sno`, `name`, `phone_num`, `msg`, `date`, `email`) VALUES
(1, 'first post', 1234567891, 'my first post', '2019-11-11 14:07:58.000000', 'myfirstpost@gmail.com');

-- --------------------------------------------------------

--
-- Table structure for table `posts`
--

CREATE TABLE `posts` (
  `SNO` int(11) NOT NULL,
  `add_pic` varchar(12) NOT NULL,
  `title` text NOT NULL,
  `tagline` text NOT NULL,
  `slug` varchar(25) NOT NULL,
  `content` text NOT NULL,
  `img_file` varchar(12) NOT NULL,
  `date` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `posts`
--

INSERT INTO `posts` (`SNO`, `add_pic`, `title`, `tagline`, `slug`, `content`, `img_file`, `date`) VALUES
(1, 'xQWqfD.jpg', 'YAMAHA R1', 'Rs:56,0000 ', 'second-post', 'A template contains variables and/or expressions, which get replaced with values when a template is rendered; and tags, which control the logic of the template. The template syntax is heavily inspired by Django and Python.\r\n\r\nBelow is a minimal template that illustrates a few basics using the default Jinja configuration. We will cover the details later in this document:', 'xQWqfD.jpg', '2019-12-04 12:21:30'),
(3, 'O5CqGAd.jpg', 'NISSAN 360z', 'Rs 36,00000', 'NISSAN', 'Class	Sports car (S)\r\nBody style	\r\n3-door hatchback coupé\r\n2-door roadster\r\nLayout	Front mid-engine, rear-wheel drive\r\nPlatform	Nissan FM platform\r\nRelated	\r\nInfiniti G35\r\nNissan Skyline', 'O5CqGAd.jpg', '2019-12-04 12:30:21'),
(6, 'fdadfasf', 'fsafsa', 'fasfas', 'asfas', 'fasfas', 'fasfas', '2019-12-04 13:30:42'),
(7, 'dasfas', 'fasfsa', 'fasfsa', 'fsafsa', 'fsafsaf', 'fsasa', '2019-12-04 13:30:58'),
(8, 'GFJDGHDFKJ', 'GJDFKGJDFKL', 'FJDLKGJDFLK', 'FJDKGJDFLK', 'GFDJKLGJFDLK', 'GJDSGDS', '2019-12-04 15:37:48'),
(9, 'FEASFJKA', 'FBEJFEJ', 'FEJFEJ', 'FEFHUU', 'FEHUFHEU', 'FQQQWF', '2019-12-04 15:38:08'),
(10, 'FHEKJWQHFKJ', 'FHEWJKFHEJK', 'FJEWKFJEWL', 'FEJQLKFJ', 'FJEQKLJ', 'FQWFQW', '2019-12-04 15:38:36'),
(11, 'SSSSSSSS', 'SSSSSSSSSSS', 'SSSSSSSSSSSSS', 'SSSSSSSSSS', 'SSSSSSSSSSSSSSSSSSSSSS', 'SSSSSSSSSSSS', '2019-12-04 15:38:59');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `contact`
--
ALTER TABLE `contact`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `posts`
--
ALTER TABLE `posts`
  ADD PRIMARY KEY (`SNO`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `contact`
--
ALTER TABLE `contact`
  MODIFY `sno` int(12) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=38;

--
-- AUTO_INCREMENT for table `posts`
--
ALTER TABLE `posts`
  MODIFY `SNO` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
