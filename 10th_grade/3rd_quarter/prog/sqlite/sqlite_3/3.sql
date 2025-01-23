CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    quantity INTEGER,
    product_id INTEGER,
    FOREIGN KEY (product_id) REFERENCES products (id)
);
