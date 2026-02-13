import streamlit as st
import pandas as pd

st.set_page_config(page_title="Movie Recommender", page_icon="⚡", layout="wide")

st.title("Movie Recommender")
st.info("IMDb Top 1000 Movies")

movies = pd.read_csv('imdb_top_1000.csv')
with st.expander("Click here to view the entire dataset", expanded=False):
    st.dataframe(movies)

# Select the number of movies you want to get recommended
number_of_movies = st.slider("Use the slider value to show only N movies you want to get recommended", 1, 1000)

'''
Plan for this page:
- Filters
- Main recommended movie (maybe highlighted)
- Similar movies below
- Model validation section
'''

rating = st.slider("Select minimum rating:", 0, 9)
# Sort movies by minimum rating
movies = movies[movies['IMDB_Rating'] >= rating]

# Show only the first N rows of the 'movies dataframe'
st.write(movies.head(number_of_movies))


# Get recommendations and put it into a list
recommendations_list = movies.head(number_of_movies)
# print(recommendations_list)

# Example - display image in streamlit
image = movies.iloc[0,0]
st.image(image, caption='Shawshank redemption poster', width=100)