import sqlite3

from db.utils import get_script_from_file


class Book:
    class BookObjects:
        conn: sqlite3.Connection

        def __init__(self, conn: sqlite3.Connection) -> None:
            self.conn = conn

        def _template_query(self, script: str, *args) -> list[tuple]:
            cursor = self.conn.cursor()
            script = get_script_from_file(f"book/{script}")
            res = cursor.execute(script, args)
            self.conn.commit()
            return res.fetchall()

        def all(self) -> list[tuple[str, str, int, str, int, int]]:
            return self._template_query("all.sql")

        def create(self, name: str, author: str, year: int, edition: str, locker: int, shelf: int) -> None:
            self._template_query("create.sql", name, author, year, edition, locker, shelf)

        def delete(self, book_id: int) -> None:
            self._template_query("delete.sql", book_id)

        def get_book(self, name: str, author: str) -> list[tuple[int, int, int]]:
            return self._template_query("get_book.sql", name, author)

        def get_info(self, book_id: int) -> list[tuple[str, str, int, str]]:
            return self._template_query("get_info.sql", book_id)


    conn: sqlite3.Connection
    objects: BookObjects

    def __init__(self, db_path: str) -> None:
        self.conn = sqlite3.connect(db_path)
        cursor = self.conn.cursor()
        cursor.executescript(get_script_from_file("db_init.sql"))
        self.conn.commit()
        self.objects = Book.BookObjects(self.conn)

class User:
    class UserObjects:
        conn: sqlite3.Connection

        def __init__(self, conn: sqlite3.Connection) -> None:
            self.conn = conn

        def _template_query(self, script: str, *args) -> list[tuple]:
            cursor = self.conn.cursor()
            script = get_script_from_file(f"user/{script}")
            res = cursor.execute(script, args)
            self.conn.commit()
            return res.fetchall()

        def all(self) -> list[tuple[str, str, str, int, str]]:
            return self._template_query("all.sql")

        def create(self, name: str, lastname: str, middlename: str | None, ticket: int, address: str) -> None:
            self._template_query("create.sql", name, lastname, middlename, ticket, address)

        def delete(self, user_id: int) -> None:
            self._template_query("delete.sql", user_id)

        def get_user(self, name: str, lastname: str) -> list[tuple[int, int]]:
            return self._template_query("get_user.sql", name, lastname)

        def get_info(self, user_id: int) -> list[tuple[str, str, str, int]]:
            return self._template_query("get_info.sql", user_id)

    conn: sqlite3.Connection
    objects: UserObjects

    def __init__(self, db_path: str) -> None:
        self.conn = sqlite3.connect(db_path)
        cursor = self.conn.cursor()
        cursor.executescript(get_script_from_file("db_init.sql"))
        self.conn.commit()
        self.objects = User.UserObjects(self.conn)

class Rent:
    class RentObjects:
        conn: sqlite3.Connection

        def __init__(self, conn: sqlite3.Connection) -> None:
            self.conn = conn

        def _template_query(self, script: str, *args) -> list[tuple]:
            cursor = self.conn.cursor()
            script = get_script_from_file(f"rent/{script}")
            res = cursor.execute(script, args)
            self.conn.commit()
            return res.fetchall()

        def all(self) -> list[tuple[int, int]]:
            return self._template_query("all.sql")

        def create(self, user_id: int, book_id: int) -> None:
            self._template_query("create.sql", user_id, book_id)

        def delete(self, rent_id: int) -> None:
            self._template_query("delete.sql", rent_id)

        def get_book(self, user_id: int) -> list[tuple[int]]:
            return self._template_query("get_book.sql", user_id)

        def get_user(self, book_id: int) -> list[tuple[int]]:
            return self._template_query("get_book.sql", book_id)

    conn: sqlite3.Connection
    objects: RentObjects

    def __init__(self, db_path: str) -> None:
        self.conn = sqlite3.connect(db_path)
        cursor = self.conn.cursor()
        cursor.executescript(get_script_from_file("db_init.sql"))
        self.conn.commit()
        self.objects = Rent.RentObjects(self.conn)
