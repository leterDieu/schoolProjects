CREATE TABLE IF NOT EXISTS books (
    book_id INTEGER PRIMARY KEY,
    name VARCHAR(1024) NOT NULL,
    author VARCHAR(1024),
    year INTEGER,
    edition VARCHAR(1024) NOT NULL,
    locker INTEGER,
    shelf INTEGER
);

CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    name VARCHAR(1024) NOT NULL,
    lastname VARCHAR(1024) NOT NULL,
    middlename VARCHAR(1024),
    ticket INTEGER,
    address VARCHAR(1024) NOT NULL
);

CREATE TABLE IF NOT EXISTS rents (
    rent_id INTEGER PRIMARY KEY,
    user_id INTEGER,
    book_id INTEGER,
    FOREIGN KEY (user_id) REFERENCES user (user_id),
    FOREIGN KEY (book_id) REFERENCES book (book_id)
);
