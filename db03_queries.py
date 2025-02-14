import pathlib
import sqlite3
import pandas as pd

# Define the database file in the current root project directory
db_file = pathlib.Path("project.sqlite3")


def aggregate():
    """Function to read and execute SQL statements to count total rows in books.
    This number will change based on whether or not db02_features.py has been run."""
    try:
        with sqlite3.connect(db_file) as conn:
            sql_file = pathlib.Path("sql_queries", "query_aggregation.sql")
            with open(sql_file, "r") as file:
                sql_script = file.read()
            x = conn.executescript(sql_script)
            # why do I have to execute the script twice like this for the cursor object to return count? No f***ing idea.
            x.execute(sql_script)
            print(f"Row aggregated successfully. Count: {x.fetchone()[0]}")
    except sqlite3.Error as e:
        print("Error aggregating row:", e)


def filter():
    """Function to read and execute SQL statements to filter rows in books that were only written by Tolkien.
    This number will change based on whether or not db02_features.py has been run."""
    try:
        with sqlite3.connect(db_file) as conn:
            sql_file = pathlib.Path("sql_queries", "query_filter.sql")
            with open(sql_file, "r") as file:
                sql_script = file.read()
            x = conn.executescript(sql_script)
            x.execute(sql_script)
            # list of tuples of each row after sql script executes
            booklist = x.fetchall()
            # list comprehension to get value of first index (title) in booklist
            books = [books[0] for books in booklist]
            print(f"Row filtered successfully.\n\tBooks written by Tolkien:{books}")
    except sqlite3.Error as e:
        print("Error filtering row:", e)


def sort():
    """Creates a new books table and sorts by year published"""
    try:
        with sqlite3.connect(db_file) as conn:
            # Selects all from books and sorts by year published #
            sql_file = pathlib.Path("sql_queries", "query_sorting.sql")
            with open(sql_file, "r") as file:
                sql_script = file.read()
            conn.executescript(sql_script)
            #######################################################
            # List of rows in books
            li = conn.executescript(sql_script).execute(sql_script).fetchall()
            # Convert list into dataframe
            df = pd.DataFrame(
                li, columns=["book_id", "title", "year_published", "author_id"]
            )
            # Convert dataframe to sql table
            df.to_sql("books_sorted", conn, if_exists="replace", index=False)
            ########################################################
            print("Table sorted successfully. See new table in db.")
    except sqlite3.Error as e:
        print("Error sorting table:", e)


def group():
    """Creates a new authors table and groups by first name"""
    try:
        with sqlite3.connect(db_file) as conn:
            # Selects all from books and sorts by year published #
            sql_file = pathlib.Path("sql_queries", "query_group_by.sql")
            with open(sql_file, "r") as file:
                sql_script = file.read()
            conn.executescript(sql_script)
            #######################################################
            # List of rows in books
            li = conn.executescript(sql_script).execute(sql_script).fetchall()
            # Convert list into dataframe
            df = pd.DataFrame(li, columns=["author_id", "first", "last"])
            # Convert dataframe to sql table
            df.to_sql("authors_grouped", conn, if_exists="replace", index=False)
            ########################################################
            print("Table grouped successfully. See new table in db.")
    except sqlite3.Error as e:
        print("Error grouping table:", e)


def join():
    """Creates a new table joining authors and books by author_id and sorts by yea published"""
    try:
        with sqlite3.connect(db_file) as conn:
            # Selects all from books and sorts by year published #
            sql_file = pathlib.Path("sql_queries", "query_join.sql")
            with open(sql_file, "r") as file:
                sql_script = file.read()
            conn.executescript(sql_script)
            #######################################################
            # List of rows in books
            li = conn.executescript(sql_script).execute(sql_script).fetchall()
            # Convert list into dataframe
            df = pd.DataFrame(
                li,
                columns=[
                    "book_id",
                    "title",
                    "year_published",
                    "books.author_id",
                    'authors.author_id',
                    'first',
                    'last',
                ],
            )
            # Convert dataframe to sql table
            df.to_sql("joined_tables", conn, if_exists="replace", index=False)
            ########################################################
            print("Tables joined successfully. See new table in db.")
    except sqlite3.Error as e:
        print("Error joining table:", e)


def main():
    aggregate()
    filter()
    sort()
    group()
    join()


if __name__ == "__main__":
    main()
