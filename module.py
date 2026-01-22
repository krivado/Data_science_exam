# This file is used as a separate data access layer.
# The purpose is to keep all database handling in one place,
# so that analysis and visualization code can remain clean and easy to read.
import sqlite3
import pandas as pd
from pathlib import Path
from typing import Any

# The database file is located in the same directory as the code
# to avoid hard-coded file paths.
DB_NAME = "movies.sqlite"



def get_connection() -> sqlite3.Connection:
    # A shared database connection function allows the rest of the project
    # to remain unaware of where the database is located or how the connection is created.
    db_path = Path(__file__).parent / DB_NAME
    return sqlite3.connect(db_path)


def run_query(
    con: sqlite3.Connection,
    sql: str,
    params: tuple[Any, ...] = ()
) -> list[dict[str, Any]]:
   # By collecting all SQL queries in a single function,
   # the code becomes more reusable and easier to debug.
    con.row_factory = sqlite3.Row
    cursor = con.execute(sql, params)
    return [dict(row) for row in cursor.fetchall()]


# I want to create JOINs between the "Directors" and "Movies" tables.
def get_movies_with_directors() -> pd.DataFrame:
    """
    Hämtar filmer tillsammans med regissörsinformation 
    och returnerar en DataFrame redo för visualisering.
    """

    query = """
    SELECT
        m.id AS movie_id,
        m.title,
        m.release_date,
        m.popularity,
        m.vote_average,
        m.vote_count,
        m.director_id,
        d.name AS director_name,
        d.department
    FROM movies m
    LEFT JOIN directors d
        ON m.director_id = d.id
    
    """

    with get_connection() as con:
        df = pd.read_sql_query(query, con)

    return df 
