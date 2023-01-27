-- MySQL dump 10.13  Distrib 8.0.20, for Win64 (x86_64)
--
-- Host: localhost    Database: management
-- ------------------------------------------------------
-- Server version	8.0.20

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `library`
--

DROP TABLE IF EXISTS `library`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `library` (
  `Member_type` varchar(40) NOT NULL,
  `PRN_No` int NOT NULL,
  `ID_No` varchar(45) NOT NULL,
  `FirstName` varchar(45) DEFAULT NULL,
  `LastName` varchar(45) DEFAULT NULL,
  `Address1` varchar(45) DEFAULT NULL,
  `Address2` varchar(45) DEFAULT NULL,
  `PostCode` varchar(45) DEFAULT NULL,
  `Mobile` varchar(45) DEFAULT NULL,
  `Bookid` varchar(45) DEFAULT NULL,
  `Booktitle` varchar(45) DEFAULT NULL,
  `Auther` varchar(45) DEFAULT NULL,
  `DateBorrowed` varchar(45) DEFAULT NULL,
  `DateDue` varchar(45) DEFAULT NULL,
  `DaysOfBook` varchar(45) DEFAULT NULL,
  `LateReturnFine` varchar(45) DEFAULT NULL,
  `DateOverDue` varchar(45) DEFAULT NULL,
  `FinalPrice` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`PRN_No`,`ID_No`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `library`
--

LOCK TABLES `library` WRITE;
/*!40000 ALTER TABLE `library` DISABLE KEYS */;
INSERT INTO `library` VALUES ('Admin Staf',457896,'45789','Dhruva','Rathi','Delhi','Mumbai','214578','3214567890','BKID8796','Basic Of Pythpn','Ref.Kapil Kamble','2020-12-17','2021-01-01','15','Rs.25','NO','Rs.289'),('Lecturer',548855,'2155','kk','jjij','44554','jjj','kjkj','2155488532','BKID1245','Intro to python Comp Science','John Zhelle','2021-01-20','2021-02-04','15','Rs.25','NO','Rs.500'),('Lecturer',2145871,'624954','Anil','Kamble','Makni','Vasur,Mukhed','431715','78946561230','BKID5487','Python manual','Paull berry','2020-12-17','2021-01-01','15','Rs.25','NO','Rs.375'),('Student',5487981,'54821','Kapil','Kamble','Sultanpur','Delhi','458721','9876543210','BKID8796','Basic Of Pythpn','ZED A.SHAW','2020-12-17','2021-01-01','15','Rs.25','NO','Rs.725'),('Student',45219887,'124589','Yashwant','Kumar','Madhurai','South','548712','7894561230','BKID2546','Python Cookbook','Brian Jones','2020-12-17','2021-01-01','15','Rs.25','NO','Rs.354'),('Student',76454398,'329865','Pranit','Memani','Pune','Maharastra','457896','7894561230','BKID8796','Basic Of Pythpn','Ref.Kapil Kamble','2020-12-17','2021-01-01','15','Rs.25','NO','Rs.289'),('Lecturer',87023154,'78541269','Mahesh','Bhat','Delhi','New Delhi','874512','87965441230','BKID2546','Python Cookbook','Brian Jones','2021-01-28','2021-02-12','15','Rs.25','NO','Rs.354');
/*!40000 ALTER TABLE `library` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-01-28 10:19:33
