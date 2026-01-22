# API:t används som ett enkelt presentationslager ovanpå datan.
# Det var inte nödvändigt för just denna uppgift.
# Syftet är inte att bygga ett fullskaligt system,
# utan att visa hur data kan exponeras strukturerat via endpoints.

from fastapi import FastAPI, HTTPException
from module import get_connection, run_query

# FastAPI används för att snabbt kunna visa datan i webbläsaren
# utan att blanda in analyslogik eller visualisering här.
app = FastAPI()


@app.get("/")
def root():
    # En enkel root-endpoint används för att snabbt kunna verifiera
    # att API:t är igång och fungerar.
    return {"status": "ok"}


@app.get("/tables")
def list_tables():
    # Denna endpoint finns för att ge en överblick över datakällan.
    # Det gör API:t självdokumenterande och underlättar vidare analys.
    con = get_connection()
    try:
        rows = run_query(
            con,
            "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;"
        )
        return [row["name"] for row in rows]
    finally:
        con.close()


@app.get("/preview/{table}")
def preview_table(table: str, limit: int = 5):
    # Förhandsvisning används för att kunna utforska datan
    # utan att läsa in hela tabeller i onödan.
    # En begränsad whitelist används för att minska risken
    # för felaktiga eller oavsiktliga frågor.
    allowed_tables = {"movies", "directors"}
    if table not in allowed_tables:
        raise HTTPException(
            status_code=400,
            detail=f"Table must be one of: {sorted(allowed_tables)}"
        )

    con = get_connection()
    try:
        return run_query(
            con,
            f"SELECT * FROM {table} LIMIT ?;",
            (limit,)
        )
    finally:
        con.close()
