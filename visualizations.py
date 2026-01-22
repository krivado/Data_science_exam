# Jag har samlat alla visualiseringar i den här filen för att skilja
# analys och visualisering från själva Streamlit-appen.
#
# Varje funktion här motsvarar en graf som jag först tog fram i min notebook.
# Genom att lägga dem som funktioner kan jag återanvända exakt samma logik
# både i notebooken och i Streamlit, utan att skriva om koden.
#
# Den här filen ansvarar alltså bara för:
# – hur graferna skapas
# – vilka beräkningar som behövs för varje graf
#
# Den visar inget själv (ingen plt.show()), utan returnerar figurer
# som Streamlit kan rendera.


import matplotlib.pyplot as plt
import seaborn as sns


def prep_top10_directors(df):
    # Jag tar bort rader som saknar regissör eller popularity
    df = df.dropna(subset=["director_name", "popularity"])

    # Jag väljer topp 10 regissörer baserat på antal filmer, så jämförelsen känns rimlig
    top_directors = df["director_name"].value_counts().head(10).index
    df_top = df[df["director_name"].isin(top_directors)].copy()
    return df_top


def fig_box_popularity_per_director(df_top):
    # Jag använder boxplot för att visa spridning, median och extrema filmer per regissör
    fig, ax = plt.subplots()
    sns.boxplot(data=df_top, x="popularity", y="director_name", ax=ax)
    ax.set_xlabel("Popularitet")
    ax.set_ylabel("Regissör")
    ax.set_title("Popularitet per regissör (topp 10 efter antal filmer)")
    fig.tight_layout()
    return fig


def fig_count_movies_per_director(df_top):
    # Jag visar antal filmer per regissör för att man ska se hur stort underlag varje regissör har
    fig, ax = plt.subplots()
    sns.countplot(data=df_top, y="director_name", ax=ax)
    ax.set_xlabel("Antal filmer")
    ax.set_ylabel("Regissör")
    ax.set_title("Antal filmer per regissör (topp 10)")
    fig.tight_layout()
    return fig


def fig_scatter_popularity_vs_rating(df_top):
    # Jag visar om popularitet och betyg rör sig tillsammans, och om det ser olika ut för olika regissörer
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
    # Jag använder median för att enstaka succéfilmer inte ska styra hela bilden
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
    # Jag använder median även här för att få en stabil jämförelse mellan regissörer
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
