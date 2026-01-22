# This file is the main user interface of the application.
# Here I decide how the visualizations are presented, in what order,
# and how the user can interact with them.
#
# I have intentionally chosen not to place any analysis or
# visualization logic in this file. Instead, it only:
# – loads the data
# – calls prepared visualization functions
# – displays them using tabs and layout
#
# This makes the code clearer, easier to read, and simpler to modify.
# It also ensures that the Streamlit part focuses on presentation,
# while the analysis is kept separate.


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
    # I use caching so the data does not have to be reloaded and joined
    # every time I interact with the app.
    df = get_movies_with_directors()

    # I convert numeric values early so that seaborn and sorting work correctly.
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

