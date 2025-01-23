CREATE TABLE products_temp (
    id INTEGER PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    price FLOAT CHECK (price >= 0)
);

INSERT INTO
    products_temp
SELECT
    *
FROM
    products;

DROP TABLE products;

ALTER TABLE products_temp
RENAME TO products;
