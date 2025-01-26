CREATE TABLE orders_temp (
    order_id INTEGER PRIMARY KEY,
    product_id INTEGER,
    FOREIGN KEY (product_id) REFERENCES products (id)
);

INSERT INTO
    orders_temp
SELECT
    *
FROM
    orders;

DROP TABLE orders;

ALTER TABLE orders_temp
RENAME TO orders;

CREATE TABLE products_temp (
    id INTEGER PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    price FLOAT CHECK (price >= 0),
    cat_id INTEGER,
    FOREIGN KEY (cat_id) REFERENCES categories (cat_id)
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
