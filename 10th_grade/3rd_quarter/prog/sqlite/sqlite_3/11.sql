CREATE TABLE orders_temp (
    order_id INTEGER PRIMARY KEY,
    product_id INTEGER,
    FOREIGN KEY (product_id) REFERENCES products (id) ON DELETE CASCADE
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
