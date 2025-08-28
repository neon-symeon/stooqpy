import sqlite3
from rich.console import Console


def check_sqlite():
    """
    Funkcja sprawdzająca czy w systemie jest zainstalowany SQLite.
    """
    conn = None
    try:
        conn = sqlite3.connect(":memory:")
        conn.execute("SELECT sqlite_version();")
        return True
    except Exception as ex:
        print(
            "SQLite not available. Please install it from: "
            "'https://www.sqlite.org/download.html'.\n"
            f"{ex}")
        return False
    finally:
        if conn:
            conn.close()
        print(conn)


if __name__ == '__main__':
    Console().print(check_sqlite())
