import streamlit as st
import pandas as pd
import plotly.express as px


st.set_page_config(page_title="Analyze", page_icon="⚡", layout="wide")

st.title("Analyze")
st.write("Explore the dataset: IMDb Top 1000 Movies")


# ---------------- Ratings Distribution Histogram (The Number of Movies Per Rating) ----------------

# Load + clean data
df = pd.read_csv('imdb_top_1000.csv')

df["Released_Year"] = pd.to_numeric(df["Released_Year"], errors="coerce")
df["IMDB_Rating"] = pd.to_numeric(df["IMDB_Rating"], errors="coerce")

df = df.dropna(subset=["Released_Year", "IMDB_Rating"])

# Slider - let user choose year range 
min_year = int(df["Released_Year"].min())
max_year = int(df["Released_Year"].max())

year_range_hist = st.slider(
    "Select Year Range",
    min_value=min_year,
    max_value=max_year,
    value=(1920, 2020)
)

# Filter data
filtered_df = df[
    (df["Released_Year"] >= year_range_hist[0]) &
    (df["Released_Year"] <= year_range_hist[1])
]

# Plot histogram
fig = px.histogram(
    filtered_df,
    x="IMDB_Rating",
    nbins=20,
    title=f"IMDB Ratings Distribution ({year_range_hist[0]} - {year_range_hist[1]})",
    labels={"IMDB_Rating": "IMDB Rating"},
)

fig.update_layout(
    xaxis_title="IMDB Rating",
    yaxis_title="Number of Movies",
    bargap=0.1
)

st.plotly_chart(fig, use_container_width=True)




# ---------------- Year vs Number of Movies Line Chart ----------------
year_range_line = st.slider(
    "Select Year",
    min_value=min_year,
    max_value=max_year,
    value=(1920, 2020)
)

# Filter data
filtered_line = df[
    (df["Released_Year"] >= year_range_line[0]) &
    (df["Released_Year"] <= year_range_line[1])
]

grouped = filtered_line.groupby("Released_Year").size()
summary_df = grouped.reset_index()
summary_df.columns = ["Released_Year", "Movie_Count"]

fig = px.line(
    summary_df,
    x="Released_Year",
    y="Movie_Count",
    title=f"Year v Number of Movies ({year_range_line[0]} - {year_range_line[1]})"
)

fig.update_layout(
    xaxis_title="Year",
    yaxis_title="Number of Movies Released",
    bargap=0.1
)

st.plotly_chart(fig, use_container_width=True)