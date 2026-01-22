# Den här filen är själva användargränssnittet.
# Här bestämmer jag hur visualiseringarna presenteras, i vilken ordning
# och hur användaren kan interagera med dem.
#
# Jag har medvetet valt att inte lägga någon analys eller
# visualiseringslogik här, utan bara:
# – ladda data
# – anropa färdiga visualiseringsfunktioner
# – visa dem i flikar och layout
#
# På så sätt blir koden tydligare, lättare att läsa och enklare att ändra.
# Det gör också att Streamlit-delen fokuserar på presentation,
# medan analysen ligger separat.


import streamlit as st
import pandas as pd

from module import get_movies_with_directors
from visualizations import (
    prep_top10_directors,
    fig_box_popularity_per_director,
    fig_count_movies_per_director,
    fig_scatter_popularity_vs_rating,
    fig_median_popularity_per_director,
    fig_median_rating_per_director,
)

st.set_page_config(page_title="Movies dashboard", layout="wide")
st.title("Movies dashboard")


@st.cache_data
def load_data():
    # Jag cachar för att jag inte vill läsa om och joina datan varje gång jag klickar runt i appen
    df = get_movies_with_directors()

    # Jag gör om siffror direkt så att seaborn och sortering funkar utan strul
    for col in ["popularity", "vote_average", "vote_count", "year"]:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")
    return df


df = load_data()
df_top = prep_top10_directors(df)

st.caption(f"Rader totalt: {len(df)}")
st.caption(f"Rader i topp 10 regissörer: {len(df_top)}")

if st.checkbox("Visa data"):
    st.dataframe(df_top.head(200), use_container_width=True)

tab1, tab2, tab3 = st.tabs(["Regissörer", "Popularitet", "Betyg"])

with tab1:
    st.subheader("Regissörer")
    st.pyplot(fig_count_movies_per_director(df_top))
    st.pyplot(fig_box_popularity_per_director(df_top))

with tab2:
    st.subheader("Popularitet")
    st.pyplot(fig_median_popularity_per_director(df_top))
    st.pyplot(fig_scatter_popularity_vs_rating(df_top))

with tab3:
    st.subheader("Betyg")
    st.pyplot(fig_median_rating_per_director(df_top))
