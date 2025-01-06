import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load the dataset (adjust the file path as needed)
movies = pd.read_csv('tmdb_5000_movies.csv')
credits = pd.read_csv('tmdb_5000_credits.csv')

# Merge datasets
movies = movies.merge(credits, left_on='id', right_on='movie_id', suffixes=('_movies', '_credits'))

# Select features to use in the recommendation system
movies = movies[['id', 'title', 'genres', 'keywords', 'overview', 'cast', 'crew']]

# Preprocess genres and keywords (convert to string if necessary)
def preprocess_features(feature):
    return ' '.join([item['name'] for item in eval(feature)]) if isinstance(feature, str) else ''

movies['genres'] = movies['genres'].apply(preprocess_features)
movies['keywords'] = movies['keywords'].apply(preprocess_features)

# Extract the director's name from the crew data
def get_director(crew):
    crew = eval(crew) if isinstance(crew, str) else []
    for member in crew:
        if member['job'] == 'Director':
            return member['name']
    return ''

movies['director'] = movies['crew'].apply(get_director)

# Use the top 3 cast members
def get_top_cast(cast):
    cast = eval(cast) if isinstance(cast, str) else []
    return ' '.join([member['name'] for member in cast[:3]])

movies['cast'] = movies['cast'].apply(get_top_cast)

# Combine features into a single string
movies['combined_features'] = (
    movies['genres'] + ' ' +
    movies['keywords'] + ' ' +
    movies['overview'].fillna('') + ' ' +
    movies['cast'] + ' ' +
    movies['director']
)

# Vectorize the combined features using TF-IDF
vectorizer = TfidfVectorizer(stop_words='english')
feature_matrix = vectorizer.fit_transform(movies['combined_features'])

# Compute cosine similarity
cosine_sim = cosine_similarity(feature_matrix, feature_matrix)

# Function to get movie recommendations
def recommend_movies(title, cosine_sim=cosine_sim, movies=movies):
    # Get the index of the movie that matches the title
    idx = movies[movies['title'] == title].index[0]

    # Get the pairwise similarity scores of all movies with that movie
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Sort the movies based on similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the scores of the 10 most similar movies
    sim_scores = sim_scores[1:11]

    # Get the movie indices
    movie_indices = [i[0] for i in sim_scores]

    # Return the top 10 most similar movies
    return movies['title'].iloc[movie_indices]

# Example usage
movie_name = "The Dark Knight Rises"  # Replace with any movie title from the dataset
recommendations = recommend_movies(movie_name)
print(f"Recommendations for '{movie_name}':")
print(recommendations)
