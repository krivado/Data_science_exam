### English

# Data_science_exam
Streamlit app and analysis based on movie data
# Movie Analysis Dashboard (Streamlit)

This project is based on an exploratory data analysis of movie data, originally developed in a Jupyter Notebook and later turned into an interactive Streamlit application.

The goal of the project is to analyze how movie popularity and ratings vary across different directors, and to present the results in a clear and interactive way.

## Project structure

- `visualizations.py`  
  Contains all visualization logic. Each function creates one specific plot and returns a figure.  
  This makes it easy to reuse the same analysis logic both in a notebook and in Streamlit.

- `Streamlit.py`  
  The main Streamlit application.  
  Handles data loading, layout, tabs, and user interaction, while keeping visualization logic separate.

- `module.py`  
  Contains data access logic, including joining movie and director data from the SQLite database.

- `visualize.ipynb`  
  The original notebook used for exploratory analysis and initial visualizations.

- `movies.sqlite`  
  SQLite database containing the movie data.

## Why this structure

The code is intentionally split into separate files to keep responsibilities clear:
- Analysis and visualization logic are separated from presentation.
- Streamlit focuses only on displaying results and interaction.
- Visualizations can be reused or extended without changing the app structure.

This makes the project easier to read, maintain, and build upon.

## Technologies used

- Python
- pandas
- matplotlib
- seaborn
- Streamlit
- SQLite


--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Svenska

# Filmanalys – Streamlit Dashboard

Detta projekt bygger på en explorativ dataanalys av filmdata som först togs fram i en Jupyter Notebook och därefter gjordes om till en interaktiv Streamlit-applikation.

Syftet med projektet är att analysera hur popularitet och betyg varierar mellan olika regissörer och att presentera resultaten på ett tydligt och interaktivt sätt.

## Projektstruktur

- `visualizations.py`  
  Innehåller all visualiseringslogik. Varje funktion skapar en specifik graf och returnerar en figur.  
  Detta gör att samma analys kan återanvändas både i notebooken och i Streamlit.

- `Streamlit.py`  
  Själva Streamlit-applikationen.  
  Ansvarar för dataladdning, layout, flikar och användarinteraktion, medan visualiseringarna hålls separata.

- `module.py`  
  Innehåller logik för att hämta och sammanfoga data från SQLite-databasen.

- `visualize.ipynb`  
  Notebooken som användes för den första analysen och visualiseringarna.

- `movies.sqlite`  
  SQLite-databas med filmdata.

## Varför denna struktur

Koden är uppdelad för att tydligt separera ansvar:
- Analys och visualisering hålls åtskilda från presentation.
- Streamlit används enbart för att visa resultat och skapa interaktivitet.
- Visualiseringarna kan enkelt återanvändas eller vidareutvecklas.

Detta gör projektet mer lättläst, strukturerat och enklare att underhålla.

## Tekniker som används

- Python
- pandas
- matplotlib
- seaborn
- Streamlit
- SQLite

