
--create database:
CREATE TABLE laptops (
    name TEXT,
    price NUMERIC,
    category TEXT,
    ram TEXT,
    os TEXT,
    batterie INTEGER,
    poids INTEGER
);

---change price type for load only :
ALTER TABLE laptops
ALTER COLUMN price TYPE TEXT;

--check types :
select * 
from laptops

-- types check!!
	--1. price to numeric:
UPDATE laptops
SET price = REPLACE(REPLACE(price, '.', ''), ',', '.');

ALTER TABLE laptops
ALTER COLUMN price TYPE NUMERIC
USING price::NUMERIC;

--EDA:

SELECT *
FROM laptops;

--low  price :
SELECT name
FROM laptops
ORDER BY price ASC
LIMIT 10;

--hight price :
SELECT name
FROM laptops
ORDER BY price DESC
LIMIT 10;


--how many batterie life :
SELECT batterie, COUNT(*) AS frequency
FROM laptops
GROUP BY batterie
ORDER BY frequency DESC;

--poids :
SELECT poids , COUNT(*) AS t_poids
FROM laptops 
GROUP BY poids
ORDER BY t_poids DESC;

--make group mark :

SELECT name
FROM laptops;

--make rank mark with price :

SELECT 
  CASE 
    WHEN name LIKE 'Lenovo%' THEN 'Lenovo'
    WHEN name LIKE 'HP%' THEN 'HP'
    WHEN name LIKE 'DELL%' THEN 'DELL'
    WHEN name LIKE 'Asus%' THEN 'Asus'
    WHEN name LIKE 'Macbook%' THEN 'Apple'
    WHEN name LIKE 'Alienware%' THEN 'Alienware'
    WHEN name LIKE 'Honor%' THEN 'Honor'
    ELSE 'Other'
  END AS brand,
  COUNT(*) AS total
FROM laptops
GROUP BY brand
ORDER BY total DESC;


--min / max price :

SELECT 
  CASE 
    WHEN name LIKE 'Lenovo%' THEN 'Lenovo'
    WHEN name LIKE 'HP%' THEN 'HP'
    WHEN name LIKE 'DELL%' THEN 'DELL'
    WHEN name LIKE 'Asus%' THEN 'Asus'
    WHEN name LIKE 'Macbook%' THEN 'Apple'
    WHEN name LIKE 'Alienware%' THEN 'Alienware'
    WHEN name LIKE 'Honor%' THEN 'Honor'
    ELSE 'Other'
  END AS brand,
  MAX(price) AS highest_price
FROM laptops
GROUP BY brand
ORDER BY highest_price DESC;


---price and ram :
SELECT ram, AVG(price) AS avg_price
FROM laptops
GROUP BY ram
ORDER BY avg_price DESC;

--price with ram and os 
SELECT ram, os, AVG(price) AS avg_price
FROM laptops
GROUP BY ram, os
ORDER BY avg_price DESC;

--Highest-Priced Laptop for Each Feature :
SELECT ram, MAX(price) AS highest_price
FROM laptops
GROUP BY ram
ORDER BY highest_price DESC;







