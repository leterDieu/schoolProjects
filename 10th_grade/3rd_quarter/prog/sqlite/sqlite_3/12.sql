CREATE TABLE users (
    user_id INTEGER PRIMARY KEY,
    user_name VARCHAR(50) NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE orders_temp (
    order_id INTEGER PRIMARY KEY,
    product_id INTEGER,
    user_id INTEGER,
    FOREIGN KEY (product_id) REFERENCES products (id) ON DELETE CASCADE,
    FOREIGN KEY (user_id) REFERENCES users (user_id)
);

INSERT INTO
    orders_temp
SELECT
    order_id,
    product_id,
    NULL
FROM
    orders;

DROP TABLE orders;

ALTER TABLE orders_temp
RENAME TO orders;
