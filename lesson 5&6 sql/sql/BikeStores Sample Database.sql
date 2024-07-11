CREATE Database BikeStores;
go

use BikeStores;
go

-- create schemas
CREATE SCHEMA production;
go


CREATE SCHEMA sales;
go

-- create tables
CREATE TABLE production.categories (
	category_id INT IDENTITY (1, 1) PRIMARY KEY,
	category_name VARCHAR (255) NOT NULL
);

CREATE TABLE production.brands (
	brand_id INT IDENTITY (1, 1) PRIMARY KEY,
	brand_name VARCHAR (255) NOT NULL
);

CREATE TABLE production.products (
	product_id INT IDENTITY (1, 1) PRIMARY KEY,
	product_name VARCHAR (255) NOT NULL,
	brand_id INT NOT NULL,
	category_id INT NOT NULL,
	model_year SMALLINT NOT NULL,
	list_price DECIMAL (10, 2) NOT NULL,
	FOREIGN KEY (category_id) REFERENCES production.categories (category_id) ON DELETE CASCADE ON UPDATE CASCADE,
	FOREIGN KEY (brand_id) REFERENCES production.brands (brand_id) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE sales.customers (
	customer_id INT IDENTITY (1, 1) PRIMARY KEY,
	first_name VARCHAR (255) NOT NULL,
	last_name VARCHAR (255) NOT NULL,
	phone VARCHAR (25),
	email VARCHAR (255) NOT NULL,
	street VARCHAR (255),
	city VARCHAR (50),
	state VARCHAR (25),
	zip_code VARCHAR (5)
);

CREATE TABLE sales.stores (
	store_id INT IDENTITY (1, 1) PRIMARY KEY,
	store_name VARCHAR (255) NOT NULL,
	phone VARCHAR (25),
	email VARCHAR (255),
	street VARCHAR (255),
	city VARCHAR (255),
	state VARCHAR (10),
	zip_code VARCHAR (5)
);

CREATE TABLE sales.staffs (
	staff_id INT IDENTITY (1, 1) PRIMARY KEY,
	first_name VARCHAR (50) NOT NULL,
	last_name VARCHAR (50) NOT NULL,
	email VARCHAR (255) NOT NULL UNIQUE,
	phone VARCHAR (25),
	active tinyint NOT NULL,
	store_id INT NOT NULL,
	manager_id INT,
	FOREIGN KEY (store_id) REFERENCES sales.stores (store_id) ON DELETE CASCADE ON UPDATE CASCADE,
	FOREIGN KEY (manager_id) REFERENCES sales.staffs (staff_id) ON DELETE NO ACTION ON UPDATE NO ACTION
);

CREATE TABLE sales.orders (
	order_id INT IDENTITY (1, 1) PRIMARY KEY,
	customer_id INT,
	order_status tinyint NOT NULL,
	-- Order status: 1 = Pending; 2 = Processing; 3 = Rejected; 4 = Completed
	order_date DATE NOT NULL,
	required_date DATE NOT NULL,
	shipped_date DATE,
	store_id INT NOT NULL,
	staff_id INT NOT NULL,
	FOREIGN KEY (customer_id) REFERENCES sales.customers (customer_id) ON DELETE CASCADE ON UPDATE CASCADE,
	FOREIGN KEY (store_id) REFERENCES sales.stores (store_id) ON DELETE CASCADE ON UPDATE CASCADE,
	FOREIGN KEY (staff_id) REFERENCES sales.staffs (staff_id) ON DELETE NO ACTION ON UPDATE NO ACTION
);

CREATE TABLE sales.order_items (
	order_id INT,
	item_id INT,
	product_id INT NOT NULL,
	quantity INT NOT NULL,
	list_price DECIMAL (10, 2) NOT NULL,
	discount DECIMAL (4, 2) NOT NULL DEFAULT 0,
	PRIMARY KEY (order_id, item_id),
	FOREIGN KEY (order_id) REFERENCES sales.orders (order_id) ON DELETE CASCADE ON UPDATE CASCADE,
	FOREIGN KEY (product_id) REFERENCES production.products (product_id) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE production.stocks (
	store_id INT,
	product_id INT,
	quantity INT,
	PRIMARY KEY (store_id, product_id),
	FOREIGN KEY (store_id) REFERENCES sales.stores (store_id) ON DELETE CASCADE ON UPDATE CASCADE,
	FOREIGN KEY (product_id) REFERENCES production.products (product_id) ON DELETE CASCADE ON UPDATE CASCADE
);


insert into sales.customers(first_name, last_name, phone, email)
values('Amira', 'Fouda', '01021400185', 'a.am@gmail.com');


insert into sales.customers(first_name, last_name, phone, email)
values('Ezz', 'Ali', '0115482800', 'ezz@gmail.com'),
	  ('Ali', 'Hisham', '0151872250', 'ali@gmail.com'),
	  ('Salma', 'Hassan', '01254458201', 'sal@gmail.com'),
	  ('Eman', 'Salem', '01518748870', 'eman@gmail.com'),
	  ('Aya', 'Gabr', '0127596518', 'aya@gmail.com'),
	  ('Basem', 'Gamil', '0101254880', 'bas@gmail.com'),
	  ('Nour', 'Ahmed', '015487621', 'nor@gmail.com');


select * from sales.customers;

insert into sales.stores(store_name, city, phone)
output inserted.store_id,inserted.store_name,inserted.phone
values
('store1','Cairo','012355879'),
('store2','Alex','0457924598'),
('store3','Giza','04587625');


select * from sales.customers;
select * from sales.stores;


update sales.customers
set email ='mira@gmail.com'
where customer_id = 1;

update sales.stores
set email ='khaled@gmail.com',
	street ='elmoez st',
	zip_code ='54023'
where store_id=2;


delete from sales.customers
where customer_id =2;

delete from sales.customers
where customer_id between 1 and 3;

delete top(5) from sales.customers;

delete top(10) percent from sales.customers;

select * from sales.customers;

select customer_id, first_name, last_name, city
from sales.customers;


select * from production.products;

select product_id, product_name,list_price
from production.products;


select customer_id, first_name + ' ' + last_name naaame, city
from sales.customers;

select customer_id, first_name + ' ' + last_name name, city
from sales.customers;

select * from production.products 

select product_id,product_name,list_price,model_year
from production.products 
where model_year >= 2017 and list_price <= 18000.00;


select product_id,product_name,list_price,model_year
from production.products 
where model_year = 2017 and list_price < 18000.00;


select product_id,product_name,list_price,model_year
from production.products 
where model_year = 2022 or list_price < 18000.00;


select * from sales.customers
where phone = null;  --wrong


select * from sales.customers
where phone is null;


select * from sales.customers
where phone is not null;


select * from sales.customers
where state = 'CA' or state = 'NY';


select * from sales.customers
where state in ('CA','NY');

select * from production.products
where model_year= 2017 or model_year= 2019;


select * from production.products
where model_year in (2017,2019)


select * from production.products
where model_year not in (2017,2019)


select * from production.products
where list_price >= 1500.80 and list_price<= 19000.00;



select * from production.products
where list_price between 1500.80 and 19000.00;


select * from production.products
where list_price not between 1500.80 and 19000.00;

select state from sales.customers;

select distinct state from sales.customers;

select distinct first_name,state from sales.customers;


select * from sales.customers
where first_name like '%n';  -- ends with "a"


select * from sales.customers
where first_name like 'n%';    -- starts with "a"


select * from sales.customers
where first_name like '%li%';  --include this 2 character


select * from sales.customers
where first_name like '___';  --dont remember which word but remember no.of character of word


select * from sales.customers
where first_name like 'S____';   --start with character and know the no. of character of word


select * from sales.customers
where email like '%@gmail.com';   --to get the email with gmail type


select * from sales.customers
where first_name like '[NE]%';   -- the word start with N or E  despite of  the no.of character of this word



select * from sales.customers
where first_name like '[A-E]%';  --get the words starts with A to E "Include :A,B,C,D,E"


select * from sales.customers
where first_name not like '[A-C]%'; -- get any words didn't start with A to E


select * from production.products
where list_price like '8__.%'   --get the no. that start with 8 and consists of 4 digits before the point 


select * from sales.customers
where first_name like 'S__m%';  --get the word that starts with S and after 2 character theres m character 


select first_name, last_name, email
from sales.customers
order by first_name;    ---asc


select first_name, last_name, email
from sales.customers
order by first_name desc;

select state,first_name, last_name, email
from sales.customers
order by state asc,first_name desc;


select category_id,product_id, product_name, list_price
from production.products
order by category_id, list_price desc;
-- order by is the last thing in the statement




select * from sales.customers;
select * from sales.orders;

select first_name, last_name, email, order_id, order_date, store_id
from sales.customers c, sales.orders o
where c.customer_id = o.customer_id;


select first_name, last_name, email, order_id, order_date, store_id
from sales.customers c join sales.orders o
on c.customer_id = o.customer_id;

select first_name, last_name, email, order_id, order_date,order_status
from sales.orders o, sales.staffs s
where s.staff_id = o.staff_id;



select first_name, last_name, email, order_id, order_date,order_status
from sales.orders o inner join sales.staffs s
on s.staff_id = o.staff_id;


select c.customer_id, first_name, last_name, email, order_id, order_date,order_status
from sales.customers c inner join sales.orders o
on c.customer_id = o.customer_id
order by customer_id desc;

select c.customer_id, first_name, last_name, email, order_id, order_date,order_status
from sales.customers c left outer join sales.orders o
on c.customer_id = o.customer_id
order by customer_id desc;


select c.customer_id, first_name, last_name, email, order_id, order_date,order_status
from sales.customers c right outer join sales.orders o
on c.customer_id = o.customer_id
order by order_id desc;


select c.customer_id, first_name, last_name, email, order_id, order_date,order_status
from sales.customers c full outer join sales.orders o
on c.customer_id = o.customer_id
order by order_id desc;

select * from sales.customers;


select first_name, last_name, order_id, order_date, street, city
from sales.customers c ,sales.orders o, sales.stores s
where c.customer_id = o.customer_id and o.store_id =s.store_id;


select first_name, last_name, order_id, order_date,s.street, s.city
from sales.customers c ,sales.orders o, sales.stores s
where c.customer_id = o.customer_id and o.store_id =s.store_id;


select first_name, last_name, order_id, order_date,s.street, s.city
from sales.customers c join sales.orders o on c.customer_id = o.customer_id 
join sales.stores s on o.store_id =s.store_id;



select o.order_id, order_date, p.product_id, product_name, p.list_price
from sales.orders o, sales.order_items oi, production.products p
where o.order_id=oi.order_id and oi.product_id=p.product_id;


select o.order_id, order_date, p.product_id, product_name, p.list_price
from sales.orders o join sales.order_items oi on o.order_id=oi.order_id 
join production.products p on oi.product_id=p.product_id;


select first_name +' '+ last_name as "Customer Name", brand_name 
from sales.customers c, sales.orders o, sales.order_items oi,
production.products p, production.brands b
where c.customer_id=o.customer_id and o.order_id=oi.order_id 
and oi.product_id=p.product_id and p.brand_id=b.brand_id;


select first_name +' '+ last_name as "Customer Name", brand_name 
from sales.customers c join sales.orders o on c.customer_id=o.customer_id
join sales.order_items oi on o.order_id=oi.order_id 
join production.products p on oi.product_id=p.product_id
join production.brands b on p.brand_id=b.brand_id;


select max(list_price), min(list_price),
avg(list_price), sum(list_price),
count(*)
from production.products;

select max(list_price) "Highest Price", min(list_price) "Lowest Price",
avg(list_price) Average, sum(list_price) "Total Prices",
count(*) "NO of Products"
from production.products;


select count (*) "No of Orders", min(order_date)"First Order",
max(order_date)"Last Order"
from sales.orders
where customer_id=2;



-- for each category, list category_id, max price, lowest price, average price;
select category_id, count(*) "No of products", max(list_price)"Highest Price",
min(list_price) as "Lowest Price", avg(list_price) as "Average Price"
from production.products
group by category_id;


--for each brand, display a list of brand name, no of products for that
-- the highest and lowest price in the brand.

select brand_name, count(*)"No of Products", max(list_price)"Highest Price",
min(list_price)"Lowest Price"
from production.brands b join production.products p 
on b.brand_id = p.brand_id
group by brand_name;



select customer_id, count (*) "No of Orders", min(order_date)"First Order",
max(order_date)"Last Order"
from sales.orders
group by customer_id
having count (*)>= 1;



select store_name, count(*) as "NO of Orders"
from sales.stores s join sales.orders o 
on s.store_id = o.store_id
group by store_name
having count(*)> 400
order by COUNT(*) desc;

select brand_name, count(*)
from production.brands b join production.products p 
on b.brand_id = p.brand_id join sales.order_items oi 
on p.product_id = oi.product_id
group by brand_name
having count(*)> 1000
order by count(*)desc;

select top 10 product_name, list_price
from production.products
order by list_price desc;

select top 5 percent product_name, list_price
from production.products
order by list_price desc;

select top 3 with ties product_name, list_price
from production.products
order by list_price desc;

