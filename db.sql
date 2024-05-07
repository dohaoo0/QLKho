-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: qlkho
-- ------------------------------------------------------
-- Server version	8.3.0

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
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customer` (
  `IdCustomer` int NOT NULL,
  `NameCustomer` varchar(50) DEFAULT NULL,
  `Email` varchar(50) DEFAULT NULL,
  `Phone` varchar(10) DEFAULT NULL,
  `Address` text,
  `ContractDate` datetime DEFAULT NULL,
  PRIMARY KEY (`IdCustomer`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer`
--

LOCK TABLES `customer` WRITE;
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
INSERT INTO `customer` VALUES (1,'Nguyen Van A','a@gmail.com','0987654321','1 Nguyen Van Linh Street, District 7, Ho Chi Minh City','2023-10-26 00:00:00'),(2,'Tran Thi B','b@yahoo.com','0912345678','2 Le Van Luong Street, Thanh Xuan District, Hanoi','2023-10-27 00:00:00'),(3,'Le Van C','c@hotmail.com','0934567890','3 Tran Hung Dao Street, Hoan Kiem District, Hanoi','2023-10-28 00:00:00'),(4,'Pham Thi D','d@outlook.com','0956789012','4 Nguyen Trai Street, Thanh Xuan District, Hanoi','2023-10-29 00:00:00'),(5,'Huynh Van E','e@gmail.com','0978901234','5 Pham Van Dong Street, Thu Duc District, Ho Chi Minh City','2023-10-30 00:00:00');
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `delivery`
--

DROP TABLE IF EXISTS `delivery`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `delivery` (
  `IdDelivery` char(10) NOT NULL,
  `IdCustomer` int DEFAULT NULL,
  `IdUser` int DEFAULT NULL,
  `Products` text,
  `Quantity` int DEFAULT NULL,
  `Date` date DEFAULT NULL,
  PRIMARY KEY (`IdDelivery`),
  KEY `IdCustomer` (`IdCustomer`),
  KEY `IdUser` (`IdUser`),
  CONSTRAINT `delivery_ibfk_1` FOREIGN KEY (`IdCustomer`) REFERENCES `customer` (`IdCustomer`),
  CONSTRAINT `delivery_ibfk_2` FOREIGN KEY (`IdUser`) REFERENCES `user` (`IdUser`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `delivery`
--

LOCK TABLES `delivery` WRITE;
/*!40000 ALTER TABLE `delivery` DISABLE KEYS */;
INSERT INTO `delivery` VALUES ('D00000001',1,2,'P0001,P0002',2,'2023-10-27'),('D00000002',3,4,'P0003,P0004',1,'2023-10-28'),('D00000003',2,1,'P0005',3,'2023-10-29'),('D00000004',4,3,'P0001,P0003',4,'2023-10-30'),('D00000005',1,5,'P0002,P0004,P0005',2,'2023-10-31');
/*!40000 ALTER TABLE `delivery` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product`
--

DROP TABLE IF EXISTS `product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `product` (
  `IdProduct` char(5) NOT NULL,
  `NameProduct` varchar(50) DEFAULT NULL,
  `Size` varchar(20) DEFAULT NULL,
  `Size_json` json DEFAULT NULL,
  PRIMARY KEY (`IdProduct`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product`
--

LOCK TABLES `product` WRITE;
/*!40000 ALTER TABLE `product` DISABLE KEYS */;
INSERT INTO `product` VALUES ('P0001','Sofa Bed','80x200x100','{\"width\": 100, \"height\": 80, \"length\": 200}'),('P0002','Dining Table','75x180x90','{\"width\": 90, \"height\": 75, \"length\": 180}'),('P0003','Office Chair','90x50x60','{\"width\": 60, \"height\": 90, \"length\": 50}'),('P0004','Coffee Table','45x100x60','{\"width\": 60, \"height\": 45, \"length\": 100}'),('P0005','Bookcase','180x80x40','{\"width\": 40, \"height\": 180, \"length\": 80}');
/*!40000 ALTER TABLE `product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `receipt`
--

DROP TABLE IF EXISTS `receipt`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `receipt` (
  `IdReceipt` char(10) NOT NULL,
  `IdSuplier` int DEFAULT NULL,
  `IdUser` int DEFAULT NULL,
  `Products` text,
  `Quantity` int DEFAULT NULL,
  `Date` date DEFAULT NULL,
  `Expense` float DEFAULT NULL,
  PRIMARY KEY (`IdReceipt`),
  KEY `IdSuplier` (`IdSuplier`),
  KEY `IdUser` (`IdUser`),
  CONSTRAINT `receipt_ibfk_1` FOREIGN KEY (`IdSuplier`) REFERENCES `suplier` (`IdSuplier`),
  CONSTRAINT `receipt_ibfk_2` FOREIGN KEY (`IdUser`) REFERENCES `user` (`IdUser`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `receipt`
--

LOCK TABLES `receipt` WRITE;
/*!40000 ALTER TABLE `receipt` DISABLE KEYS */;
/*!40000 ALTER TABLE `receipt` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `suplier`
--

DROP TABLE IF EXISTS `suplier`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `suplier` (
  `IdSuplier` int NOT NULL,
  `NameSuplier` varchar(50) DEFAULT NULL,
  `Email` varchar(50) DEFAULT NULL,
  `Phone` varchar(10) DEFAULT NULL,
  `Address` text,
  `ContractDate` datetime DEFAULT NULL,
  PRIMARY KEY (`IdSuplier`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `suplier`
--

LOCK TABLES `suplier` WRITE;
/*!40000 ALTER TABLE `suplier` DISABLE KEYS */;
INSERT INTO `suplier` VALUES (1,'ABC Furniture','abc@furniture.com','0987654321','1 Nguyen Van Linh Street, District 7, Ho Chi Minh City','2023-10-26 00:00:00'),(2,'DEF Interiors','def@interiors.com','0912345678','2 Le Van Luong Street, Thanh Xuan District, Hanoi','2023-10-27 00:00:00'),(3,'GHI Home Decor','ghi@homedecor.com','0934567890','3 Tran Hung Dao Street, Hoan Kiem District, Hanoi','2023-10-28 00:00:00'),(4,'JKL Furniture Company','jkl@furnitureco.com','0956789012','4 Nguyen Trai Street, Thanh Xuan District, Hanoi','2023-10-29 00:00:00'),(5,'MNO Design Studio','mno@designstudio.com','0978901234','5 Pham Van Dong Street, Thu Duc District, Ho Chi Minh City','2023-10-30 00:00:00');
/*!40000 ALTER TABLE `suplier` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `IdUser` int NOT NULL,
  `NameUser` text,
  `Password` varchar(6) DEFAULT NULL,
  `Role` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`IdUser`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'Nguyen Thuy Loan','001001','Owner'),(2,'Le Thi Hoa','002002','Manager'),(3,'Nguyen Thuy Linh','003003','Employee'),(4,'Do Van Linh','004004','Employee'),(5,'Pham Thu Ha','005005','Employee');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-05-08  0:44:32
