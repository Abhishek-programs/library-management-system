-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 04, 2020 at 05:21 PM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.4.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `library`
--

-- --------------------------------------------------------

--
-- Table structure for table `book`
--

CREATE TABLE `book` (
  `id` int(11) NOT NULL,
  `title` varchar(100) DEFAULT NULL,
  `author` varchar(100) DEFAULT NULL,
  `publisher` varchar(100) DEFAULT NULL,
  `genre` varchar(100) DEFAULT NULL,
  `price` double DEFAULT NULL,
  `quantity` int(11) DEFAULT NULL,
  `synopsis` text DEFAULT NULL,
  `image` varchar(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `book`
--

INSERT INTO `book` (`id`, `title`, `author`, `publisher`, `genre`, `price`, `quantity`, `synopsis`, `image`) VALUES
(1, 'Amara', 'Matt Zhang', 'Ninja', 'Mystery', 1200, 1, 'This is a book about a ninja in my town named Hatori\n\n', 'C:/Users/default.LAPTOP-QJV8QIRO/PycharmProjects/Class/Project/second_sem/Images/amara.jpg'),
(2, 'The Arrivals', 'Lucas Lloyd', 'Book', 'Sci-fi', 1400, 5, 'This is Sci-fi story about a alien that is warning you about your past from future.\n', 'C:/Users/default.LAPTOP-QJV8QIRO/PycharmProjects/Class/Project/second_sem/Images/Arriavals.jpg'),
(3, 'NotCheck', 'NotCheck', 'NotCheck', 'NotCheck', 10, 5, 'NotCheck', '../Images/add_cover.jpg'),
(4, 'The King of Drugs', 'Nora Barrett', 'The Book', 'Real Story', 2000, 11, 'This is a book about drugs and drugs\n', 'C:/Users/default.LAPTOP-QJV8QIRO/PycharmProjects/Class/Project/second_sem/Images/TKOD.jpg'),
(5, 'Where the crawdads sing', 'Delia Owens', 'Publis', 'Bibliography', 400, 17, 'This is a check book for my final project in algorithm\n', 'C:/Users/default.LAPTOP-QJV8QIRO/PycharmProjects/Class/Project/second_sem/Images/WTCS.jpg'),
(7, 'Check', 'Check', 'Check', 'Check', 1000, 20, 'Check', '../Images/add_cover.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `register`
--

CREATE TABLE `register` (
  `Id` int(100) NOT NULL,
  `firstname` varchar(100) NOT NULL,
  `lastname` varchar(100) NOT NULL,
  `username` varchar(100) NOT NULL,
  `id_no` int(100) NOT NULL,
  `address` varchar(100) NOT NULL,
  `contact` bigint(100) NOT NULL,
  `status` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `register`
--

INSERT INTO `register` (`Id`, `firstname`, `lastname`, `username`, `id_no`, `address`, `contact`, `status`, `password`) VALUES
(1, 'Abhishek', 'Bhattarai', 'admin', 100, 'Kapan', 6456456456, 'Staff', '$2a$10$BXvY/JAFWf/RNDTOjN8RHOHoj5PFqhx.w967OeUg5hzCp.vg1B9XO'),
(4, 'admintest', 'admintest', 'admintest', 6357, 'admintest', 685959, 'Staff', '$2a$10$nI5OKX80NTp20fKLFh44Nuopa1TUTVM3UMmJ384zAJuc9.BaqwVSC'),
(6, 'usertest', 'usertest', 'usertest', 8098, 'usertest', 797979, 'Student', '$2a$10$RJOK3GU9HAADwUtVkMquN.h4E7bkuPkxTjiyPaNMp3LXZhVwr4WFe'),
(7, 'test', 'test', 'test', 7987979, 'test', 699868969, 'Student', '$2a$10$XeBJ2zNXAZD4r0aG25mfruVL354uNeYwanfYW/B1L2VZ.3dC9kGc2'),
(8, 'Abhishek', 'Bhattarai', 'Sans', 69, 'Ghar', 69420, 'Staff', 'yeiho');

-- --------------------------------------------------------

--
-- Table structure for table `requested_books`
--

CREATE TABLE `requested_books` (
  `id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `book_id` int(11) DEFAULT NULL,
  `issued_date` varchar(100) DEFAULT NULL,
  `returned_date` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `requested_books`
--

INSERT INTO `requested_books` (`id`, `user_id`, `book_id`, `issued_date`, `returned_date`) VALUES
(3, 7, 4, NULL, NULL),
(4, 7, 5, '2020-08-04', '2020-09-04'),
(5, 7, 3, NULL, NULL),
(6, 6, 1, '2020-09-04', '2020-09-04');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `book`
--
ALTER TABLE `book`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `register`
--
ALTER TABLE `register`
  ADD PRIMARY KEY (`Id`) USING BTREE,
  ADD UNIQUE KEY `id_no` (`id_no`);

--
-- Indexes for table `requested_books`
--
ALTER TABLE `requested_books`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`),
  ADD KEY `book_id` (`book_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `book`
--
ALTER TABLE `book`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `register`
--
ALTER TABLE `register`
  MODIFY `Id` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `requested_books`
--
ALTER TABLE `requested_books`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `requested_books`
--
ALTER TABLE `requested_books`
  ADD CONSTRAINT `requested_books_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `register` (`Id`),
  ADD CONSTRAINT `requested_books_ibfk_2` FOREIGN KEY (`book_id`) REFERENCES `book` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
