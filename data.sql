create database QLKho;
use QLKho;
create table Suplier
(
IdSuplier int primary key,
NameSuplier varchar(50),
Email varchar(50),
Phone varchar(10),
Address text,
ContractDate DateTime
);

create table Customer
(
IdCustomer int primary key,
NameCustomer varchar(50),
Email varchar(50),
Phone varchar(10),
Address text,
ContractDate DateTime
);

create table User
(
IdUser int primary key,
NameUser text,
Password varchar(6),
Role varchar(20)
);

create table Product
(
IdProduct char(5) primary key,
NameProduct varchar(50),
Size varchar(20),
Size_json JSON
);

create table Receipt
(
IdReceipt char (10) primary key ,
IdSuplier int,
IdUser int,
Products text,
Quantity int,
Date date,
Expense float,
foreign key (IdSuplier) references Suplier(IdSuplier),
foreign key (IdUser) references User(IdUser)
);

create table Delivery
(
IdDelivery char (10) primary key,
IdCustomer int,
IdUser int,
Products text,
Quantity int,
Date date,
foreign key (IdCustomer) references Customer(IdCustomer),
foreign key (IdUser) references User(IdUser)
);

INSERT INTO Suplier (IdSuplier, NameSuplier, Email, Phone, Address, ContractDate) VALUES
(1, 'ABC Furniture', 'abc@furniture.com', '0987654321', '1 Nguyen Van Linh Street, District 7, Ho Chi Minh City', '2023-10-26'),
(2, 'DEF Interiors', 'def@interiors.com', '0912345678', '2 Le Van Luong Street, Thanh Xuan District, Hanoi', '2023-10-27'),
(3, 'GHI Home Decor', 'ghi@homedecor.com', '0934567890', '3 Tran Hung Dao Street, Hoan Kiem District, Hanoi', '2023-10-28'),
(4, 'JKL Furniture Company', 'jkl@furnitureco.com', '0956789012', '4 Nguyen Trai Street, Thanh Xuan District, Hanoi', '2023-10-29'),
(5, 'MNO Design Studio', 'mno@designstudio.com', '0978901234', '5 Pham Van Dong Street, Thu Duc District, Ho Chi Minh City', '2023-10-30');
 
INSERT INTO Customer (IdCustomer, NameCustomer, Email, Phone, Address, ContractDate) VALUES
(1, 'Nguyen Van A', 'a@gmail.com', '0987654321', '1 Nguyen Van Linh Street, District 7, Ho Chi Minh City', '2023-10-26'),
(2, 'Tran Thi B', 'b@yahoo.com', '0912345678', '2 Le Van Luong Street, Thanh Xuan District, Hanoi', '2023-10-27'),
(3, 'Le Van C', 'c@hotmail.com', '0934567890', '3 Tran Hung Dao Street, Hoan Kiem District, Hanoi', '2023-10-28'),
(4, 'Pham Thi D', 'd@outlook.com', '0956789012', '4 Nguyen Trai Street, Thanh Xuan District, Hanoi', '2023-10-29'),
(5, 'Huynh Van E', 'e@gmail.com', '0978901234', '5 Pham Van Dong Street, Thu Duc District, Ho Chi Minh City', '2023-10-30');

INSERT INTO User (IdUser, NameUser, Password, Role) VALUES
(1, 'Nguyen Thuy Loan', '001001', 'Owner'),
(2, 'Le Thi Hoa', '002002', 'Manager'),
(3, 'Nguyen Thuy Linh', '003003', 'Employee'),
(4, 'Do Van Linh', '004004', 'Employee'),
(5, 'Pham Thu Ha', '005005', 'Employee');

INSERT INTO Product (IdProduct, NameProduct, Size, Size_json) VALUES
('P0001', 'Sofa Bed', '80x200x100', '{"height": 80, "length": 200, "width": 100}'),
('P0002', 'Dining Table', '75x180x90', '{"height": 75, "length": 180, "width": 90}'),
('P0003', 'Office Chair', '90x50x60', '{"height": 90, "length": 50, "width": 60}'),
('P0004', 'Coffee Table', '45x100x60', '{"height": 45, "length": 100, "width": 60}'),
('P0005', 'Bookcase', '180x80x40', '{"height": 180, "length": 80, "width": 40}');

INSERT INTO Receipt (IdReceipt, IdSuplier, IdUser, Products, Quantity, Date, Expense) VALUES
('R00000001', 1, 2, 'P0001,P0002', 2, '2023-10-27', 1000000),
('R00000002', 3, 4, 'P0003,P0004', 1, '2023-10-28', 500000),
('R00000003', 2, 1, 'P0005', 3, '2023-10-29', 1500000),
('R00000004', 4, 3, 'P0001,P0003', 4, '2023-10-30', 2000000),
('R00000005', 1, 5, 'P0002,P0004,P0005', 2, '2023-10-31', 1200000);

INSERT INTO Delivery (IdDelivery, IdCustomer, IdUser, Products, Quantity, Date) VALUES
('D00000001', 1, 2, 'P0001,P0002', 2, '2023-10-27'),
('D00000002', 3, 4, 'P0003,P0004', 1, '2023-10-28'),
('D00000003', 2, 1, 'P0005', 3, '2023-10-29'),
('D00000004', 4, 3, 'P0001,P0003', 4, '2023-10-30'),
('D00000005', 1, 5, 'P0002,P0004,P0005', 2, '2023-10-31');