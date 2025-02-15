'''
link to sql tables
'''

import sqlite3
import dataclasses
from db.utils import get_script_from_file


@dataclasses.dataclass
class Book:
    '''
    class for book table
    '''
    class BookObjects:
        '''
        class for book object
        '''
        conn: sqlite3.Connection

        def __init__(self, conn: sqlite3.Connection) -> None:
            '''
            init
            '''
            self.conn = conn

        def _template_query(self, script: str, *args) -> list[tuple]:
            '''
            executive method
            '''
            cursor = self.conn.cursor()
            script = get_script_from_file(f"book/{script}")
            res = cursor.execute(script, args)
            self.conn.commit()
            return res.fetchall()

        def all(self) -> list[tuple[str, str, int, str, int, int]]:
            '''
            get all books
            '''
            return self._template_query("all.sql")

        def create(self, name: str, author: str, year: int,
                   edition: str, locker: int, shelf: int) -> None:
            '''
            new book
            '''
            self._template_query("create.sql", name, author, year, edition, locker, shelf)

        def delete(self, book_id: int) -> None:
            '''
            rm book
            '''
            self._template_query("delete.sql", book_id)

        def get_book(self, name: str, author: str) -> list[tuple[int, int, int]]:
            '''
            book by name and author
            '''
            return self._template_query("get_book.sql", name, author)

        def get_info(self, book_id: int) -> list[tuple[str, str, int, str]]:
            '''
            book info by its id
            '''
            return self._template_query("get_info.sql", book_id)

        def get_owner_info(self, book_id: int) -> list[tuple[int, str, str]]:
            '''
            owner by book id
            '''
            return self._template_query('get_owner_info.sql', book_id)

    conn: sqlite3.Connection
    objects: BookObjects

    def __init__(self, conn: sqlite3.Connection) -> None:
        '''
        init
        '''
        self.conn = conn
        cursor = self.conn.cursor()
        cursor.executescript(get_script_from_file("db_init.sql"))
        self.conn.commit()
        self.objects = Book.BookObjects(self.conn)

@dataclasses.dataclass
class User:
    '''
    class for user table
    '''
    class UserObjects:
        '''
        class for user object
        '''
        conn: sqlite3.Connection

        def __init__(self, conn: sqlite3.Connection) -> None:
            '''
            init
            '''
            self.conn = conn

        def _template_query(self, script: str, *args) -> list[tuple]:
            '''
            executive method
            '''
            cursor = self.conn.cursor()
            script = get_script_from_file(f"user/{script}")
            res = cursor.execute(script, args)
            self.conn.commit()
            return res.fetchall()

        def all(self) -> list[tuple[str, str, str, int, str]]:
            '''
            gets all users
            '''
            return self._template_query("all.sql")

        def create(self, name: str, lastname: str,
                   middlename: str | None, ticket: int, address: str) -> None:
            '''
            new user
            '''
            self._template_query("create.sql", name, lastname, middlename, ticket, address)

        def delete(self, user_id: int) -> None:
            '''
            rm user
            '''
            self._template_query("delete.sql", user_id)

        def get_user(self, name: str, lastname: str) -> list[tuple[int, int]]:
            '''
            get user by name and lastname
            '''
            return self._template_query("get_user.sql", name, lastname)

        def get_info(self, user_id: int) -> list[tuple[str, str, str, int]]:
            '''
            get user info by their id
            '''
            return self._template_query("get_info.sql", user_id)

        def get_books_info(self, user_id: int) -> list[tuple[int, str, str]]:
            '''
            get book by user id
            '''
            return self._template_query('get_books_info.sql', user_id)

    conn: sqlite3.Connection
    objects: UserObjects

    def __init__(self, conn: sqlite3.Connection) -> None:
        '''
        init
        '''
        self.conn = conn
        cursor = self.conn.cursor()
        cursor.executescript(get_script_from_file("db_init.sql"))
        self.conn.commit()
        self.objects = User.UserObjects(self.conn)

@dataclasses.dataclass
class Rent:
    '''
    class for rent table
    '''
    class RentObjects:
        '''
        class for rent object
        '''
        conn: sqlite3.Connection

        def __init__(self, conn: sqlite3.Connection) -> None:
            '''
            init
            '''
            self.conn = conn

        def _template_query(self, script: str, *args) -> list[tuple]:
            '''
            executive method
            '''
            cursor = self.conn.cursor()
            script = get_script_from_file(f"rent/{script}")
            res = cursor.execute(script, args)
            self.conn.commit()
            return res.fetchall()

        def all(self) -> list[tuple[int, int]]:
            '''
            gets all rents
            '''
            return self._template_query("all.sql")

        def create(self, user_id: int, book_id: int) -> None:
            '''
            new rent
            '''
            self._template_query("create.sql", user_id, book_id)

        def delete(self, rent_id: int) -> None:
            '''
            rm rent
            '''
            self._template_query("delete.sql", rent_id)

        def get_book(self, user_id: int) -> list[tuple[int]]:
            '''
            book by user id
            '''
            return self._template_query("get_book.sql", user_id)

        def get_user(self, book_id: int) -> list[tuple[int]]:
            '''
            user by book id
            '''
            return self._template_query("get_book.sql", book_id)

    conn: sqlite3.Connection
    objects: RentObjects

    def __init__(self, conn: sqlite3.Connection) -> None:
        '''
        init
        '''
        self.conn = conn
        cursor = self.conn.cursor()
        cursor.executescript(get_script_from_file("db_init.sql"))
        self.conn.commit()
        self.objects = Rent.RentObjects(self.conn)
