CREATE TABLE categories (
    cat_id INTEGER PRIMARY KEY,
    cat_name VARCHAR(50) NOT NULL
);

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
    id,
    name,
    price,
    NULL
FROM
    products;

DROP TABLE products;

ALTER TABLE products_temp
RENAME TO products;
