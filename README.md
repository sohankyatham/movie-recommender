# Top 1000 IMDB Movie Recommender

- Run code with: (`streamlit run app.py --server.port 8502`)

## Description
A movie recommendation engine that recommends users movies from a list of the 1000 highest rated movies on IMDb

- Content-based recommender using similarity 
- - (a recommendation system that suggests items to a user based on the similarity between the item's features and the user's past preferences or behavior)
- Add classification model predicting

### Tab 1 - Home
- Filter-based recommendation
- Similar movies
- Model + validation output

### Tab 2 - Analyze
- Interactive visualizations
- Movie history insights
- Exploratory analysis

## Technologies Used
- Python

## How It Works
- Interactive Streamlit interface for user input
- Displays movie data (title, release year, IMDB rating, actors, director, short overview) and lets user filter by minimum rating, genre, and year 
- Enhanced features: visualization of Bar chart/Histogram of IMDB ratings of recommended movies and Popularity bias (combine similarity + popularity) and also a random movie recommendation feature 