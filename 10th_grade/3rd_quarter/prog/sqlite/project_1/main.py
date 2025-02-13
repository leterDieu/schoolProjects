from db.models import *
import argparse


def main():
    db_path = "./database.db"

    book_table = Book(db_path)
    user_table = User(db_path)
    rent_table = Rent(db_path)

    parser = argparse.ArgumentParser(description = "db manager")

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
                        help = "Gets book's id and it's location")

    parser.add_argument("-gbi", "--get-book-info", type = str, nargs = 1,
                        metavar = 'book id',
                        help = "Gets book's info")

    args = parser.parse_args()

    if args.all_books != None:
        print(book_table.objects.all())
    if args.new_book != None:
        book_table.objects.create(*args.new_book)
    if args.remove_book != None:
        book_table.objects.delete(*args.remove_book)
    if args.get_book != None:
        print(book_table.objects.get_book(*args.get_book))
    if args.get_book_info != None:
        print(book_table.objects.get_info(*args.get_book_info))




if __name__ == "__main__":
    main()
