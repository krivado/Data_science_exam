# I have collected all visualizations in this file to separate
# analysis and visualization logic from the Streamlit application.
#
# Each function in this file corresponds to a plot that was first created
# in the notebook. By defining them as functions, I can reuse the exact
# same logic in both the notebook and the Streamlit app without rewriting code.
#
# This file is therefore only responsible for:
# – how the plots are created
# – which calculations are needed for each plot
#
# It does not display anything on its own (no plt.show()),
# but instead returns figures that Streamlit can render.


import matplotlib.pyplot as plt
import seaborn as sns


def prep_top10_directors(df):
    # I remove rows that are missing a director or popularity value.
    df = df.dropna(subset=["director_name", "popularity"])

    # I select the top 10 directors based on the number of movies,
    # so the comparison is more meaningful.
    top_directors = df["director_name"].value_counts().head(10).index
    df_top = df[df["director_name"].isin(top_directors)].copy()
    return df_top


def fig_box_popularity_per_director(df_top):
    # I use a boxplot to show the distribution, median,
    # and extreme values for each director.
    fig, ax = plt.subplots()
    sns.boxplot(data=df_top, x="popularity", y="director_name", ax=ax)
    ax.set_xlabel("Popularitet")
    ax.set_ylabel("Regissör")
    ax.set_title("Popularitet per regissör (topp 10 efter antal filmer)")
    fig.tight_layout()
    return fig


def fig_count_movies_per_director(df_top):
    # I show the number of movies per director
    # to make it clear how large the data basis is for each director.
    fig, ax = plt.subplots()
    sns.countplot(data=df_top, y="director_name", ax=ax)
    ax.set_xlabel("Antal filmer")
    ax.set_ylabel("Regissör")
    ax.set_title("Antal filmer per regissör (topp 10)")
    fig.tight_layout()
    return fig


def fig_scatter_popularity_vs_rating(df_top):
    # I show whether popularity and ratings move together,
    # and whether this relationship looks different across directors.
    df_top = df_top.dropna(subset=["popularity", "vote_average"])

    fig, ax = plt.subplots()
    sns.scatterplot(
        data=df_top,
        x="popularity",
        y="vote_average",
        hue="director_name",
        alpha=0.6,
        ax=ax,
    )
    ax.set_xlabel("Popularitet")
    ax.set_ylabel("Betyg")
    ax.set_title("Popularitet och betyg för topp 10 regissörer")
    fig.tight_layout()
    return fig


def fig_median_popularity_per_director(df_top):
    # I use the median so that individual blockbuster movies
    # do not dominate the overall picture.
    summary = (
        df_top.groupby("director_name")["popularity"]
        .median()
        .sort_values(ascending=False)
        .reset_index(name="median_popularity")
    )

    fig, ax = plt.subplots()
    sns.barplot(data=summary, x="median_popularity", y="director_name", ax=ax)
    ax.set_xlabel("Median popularitet")
    ax.set_ylabel("Regissör")
    ax.set_title("Typisk popularitet per regissör (median, topp 10)")
    fig.tight_layout()
    return fig


def fig_median_rating_per_director(df_top):
    # I use the median here as well to ensure a more stable comparison between directors.
    df_top = df_top.dropna(subset=["vote_average"])

    fig, ax = plt.subplots()
    sns.barplot(
        data=df_top,
        y="director_name",
        x="vote_average",
        estimator="median",
        errorbar=None,
        ax=ax,
    )
    ax.set_xlabel("Median betyg")
    ax.set_ylabel("Regissör")
    ax.set_title("Typiskt betyg per regissör (median, topp 10)")
    fig.tight_layout()
    return fig
