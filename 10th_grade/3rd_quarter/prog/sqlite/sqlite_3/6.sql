ALTER TABLE products
ADD COLUMN price_temp DECIMAL(10, 2);

UPDATE products
SET
    price_temp = price;

ALTER TABLE products
DROP COLUMN price;

ALTER TABLE products
ADD COLUMN price FLOAT;

UPDATE products
SET
    price = price_temp
