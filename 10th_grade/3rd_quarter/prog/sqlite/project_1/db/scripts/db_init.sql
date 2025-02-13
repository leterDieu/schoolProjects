CREATE TABLE IF NOT EXISTS books (
    book_id INTEGER PRIMARY KEY,
    name VARCHAR(1024) NOT NULL,
    author VARCHAR(1024) NOT NULL,
    year INT,
    edition VARCHAR(1024) NOT NULL,
    case INT,
    shelf INT
);

CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    name VARCHAR(1024) NOT NULL,
    lastname VARCHAR(1024) NOT NULL,
    middlename VARCHAR(1024),
    ticket INT,
    address VARCHAR(1024) NOT NULL
);

CREATE TABLE IF NOT EXISTS rents (
    rent_id INTEGER PRIMARY KEY,
    user_id INTEGER,
    book_id INTEGER,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (book_id) REFERENCES books(book_id)
);
