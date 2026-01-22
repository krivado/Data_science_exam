# Denna fil används som ett separat datalager.
# Syftet med detta arbete är att samla all databashantering på ett ställe,
# på så sätt kan analys och visualisering kan hållas rena och lättlästa.
import sqlite3
import pandas as pd
from pathlib import Path
from typing import Any

# Databasfilen ligger i samma mapp som koden för att undvika hårdkodade sökvägar
DB_NAME = "movies.sqlite"



def get_connection() -> sqlite3.Connection:
    # En gemensam funktion för databaskoppling gör att resten av projektet
    # inte behöver känna till var databasen ligger eller hur kopplingen skapas.
    db_path = Path(__file__).parent / DB_NAME
    return sqlite3.connect(db_path)


def run_query(
    con: sqlite3.Connection,
    sql: str,
    params: tuple[Any, ...] = ()
) -> list[dict[str, Any]]:
    # Genom att samla alla SQL-frågor i en och samma funktion
    # blir koden mer återanvändbar och enklare att felsöka.
    con.row_factory = sqlite3.Row
    cursor = con.execute(sql, params)
    return [dict(row) for row in cursor.fetchall()]


# Jag vill skapa JOINS mellan tabellerna "Directors" samt "Movies"
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