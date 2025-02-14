import pathlib
import sqlite3

# Define the database file in the current root project directory
db_file = pathlib.Path("project.sqlite3")

def update_row():
    """Function to read and execute SQL statements to update row"""
    try:
        with sqlite3.connect(db_file) as conn:
            sql_file = pathlib.Path("sql_features", "update_records.sql")
            with open(sql_file, "r") as file:
                sql_script = file.read()
            conn.executescript(sql_script)
            print("Row updated successfully.")
    except sqlite3.Error as e:
        print("Error updating row:", e)

def remove_row():
    """Function to read and execute SQL statements to delete rows with Tolkien"""
    try:
        with sqlite3.connect(db_file) as conn:
            sql_file = pathlib.Path("sql_features", "delete_records.sql")
            with open(sql_file, "r") as file:
                sql_script = file.read()
            conn.executescript(sql_script)
            print("Row removed successfully.")
    except sqlite3.Error as e:
        print("Error removing row:", e)


def main():
    update_row()
    remove_row()


if __name__ == "__main__":
    main()
