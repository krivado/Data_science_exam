# The API is used as a simple presentation layer on top of the data.
# It was not strictly necessary for this assignment.
# The goal is not to build a full-scale system,
# but to demonstrate how data can be exposed in a structured way via endpoints.

from fastapi import FastAPI, HTTPException
from module import get_connection, run_query

# FastAPI is used to quickly expose the data in the browser
# without mixing in analysis or visualization logic here.
app = FastAPI()


@app.get("/")
def root():
    # A simple root endpoint is used to quickly verify
    # that the API is running and working correctly.
    return {"status": "ok"}


@app.get("/tables")
def list_tables():
# This endpoint exists to provide an overview of the data source.
# It makes the API more self-documenting and easier to work with in further analysis.
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
# A preview is used to explore the data
# without unnecessarily loading entire tables.
# A limited whitelist is applied to reduce the risk
# of incorrect or unintended queries.
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

