import argparse
from tabulate import tabulate
from db.models import *


def custom_print(info: list[tuple]) -> None:
    print(tabulate(info))


def main():
    db_path = "./database.db"
    conn = sqlite3.connect(db_path)
    book_table = Book(conn)
    user_table = User(conn)
    rent_table = Rent(conn)

    parser = argparse.ArgumentParser(description = "db manager")

    # books
    parser.add_argument("-ab", "--all-books", nargs = '*',
                        help = "Shows all books.")

    parser.add_argument("-nb", "--new-book", type = str, nargs = 6,
                        metavar = ('name', 'author', 'year', 'edition', 'locker', 'shelf'),
                        help = "Creates a new book.")

    parser.add_argument("-rmb", "--remove-book", type = str, nargs = 1,
                        metavar = 'book id',
                        help = "Removes book by id.")

    parser.add_argument("-gb", "--get-book", type = str, nargs = 2,
                        metavar = ('name', 'author'),
                        help = "Gets book's id and it's location.")

    parser.add_argument("-gbi", "--get-book-info", type = str, nargs = 1,
                        metavar = 'book id',
                        help = "Gets book's info.")

    # users
    parser.add_argument("-au", "--all-users", nargs = '*',
                        help = "Shows all users.")

    parser.add_argument("-nu", "--new-user", type = str, nargs = 5,
                        metavar = ('name', 'lastname', 'middlename', 'ticket', 'address'),
                        help = "Creates a new user.")

    parser.add_argument("-rmu", "--remove-user", type = str, nargs = 1,
                        metavar = 'user id',
                        help = "Removes user by id.")

    parser.add_argument("-gu", "--get-user", type = str, nargs = 2,
                        metavar = ('name', 'lastname'),
                        help = "Gets user's id and their ticket.")

    parser.add_argument("-gbu", "--get-user-info", type = str, nargs = 1,
                        metavar = 'user id',
                        help = "Gets user's info.")

    # rents
    parser.add_argument("-ar", "--all-rents", type = str, nargs = '*',
                        help = "Shows all rents.")

    parser.add_argument("-nr", "--new-rent", type = str, nargs = 2,
                        metavar = ('user id', 'book id'),
                        help = "Creates a new rent.")

    parser.add_argument("-rmr", "--remove-rent", type = str, nargs = 1,
                        metavar = 'rent id',
                        help = "Removes rent by id.")

    parser.add_argument("-grb", "--get-rent-book", type = str, nargs = 1,
                        metavar = 'user id',
                        help = "Gets book's id by user's id.")

    parser.add_argument("-gru", "--get-rent-user", type = str, nargs = 1,
                        metavar = 'book id',
                        help = "Gets user's id by book's id.")

    # relations
    parser.add_argument("-goi", "--get-owner-info", type = str, nargs = 1,
                        metavar = 'book id',
                        help = "Gets user's info by book's id.")

    parser.add_argument("-gbsi", "--get-books-info", type = str, nargs = 1,
                        metavar = 'user id',
                        help = "Gets books' info by user's id.")



    args = parser.parse_args()

    # books
    if args.all_books != None:
        custom_print(book_table.objects.all())
    if args.new_book != None:
        book_table.objects.create(*args.new_book)
    if args.remove_book != None:
        book_table.objects.delete(*args.remove_book)
    if args.get_book != None:
        custom_print(book_table.objects.get_book(*args.get_book))
    if args.get_book_info != None:
        custom_print(book_table.objects.get_info(*args.get_book_info))

    # users
    if args.all_users != None:
        custom_print(user_table.objects.all())
    if args.new_user != None:
        user_table.objects.create(*args.new_user)
    if args.remove_user != None:
        user_table.objects.delete(*args.remove_user)
    if args.get_user != None:
        custom_print(user_table.objects.get_user(*args.get_user))
    if args.get_user_info != None:
        custom_print(user_table.objects.get_info(*args.get_user_info))

    # rents
    if args.all_rents != None:
        custom_print(rent_table.objects.all())
    if args.new_rent != None:
        rent_table.objects.create(*args.new_rent)
    if args.remove_rent != None:
        rent_table.objects.delete(*args.remove_rent)
    if args.get_rent_book != None:
        custom_print(rent_table.objects.get_book(*args.get_rent_book))
    if args.get_rent_user != None:
        custom_print(rent_table.objects.get_user(*args.get_rent_user))

    # relations
    if args.get_owner_info != None:
        custom_print(book_table.objects.get_owner_info(*args.get_owner_info))
    if args.get_books_info != None:
        custom_print(user_table.objects.get_books_info(*args.get_books_info))


if __name__ == "__main__":
    main()
