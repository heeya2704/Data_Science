import matplotlib.pyplot as plt
import pandas as pd

# Mini BookMyShow Movies Dataset (12 movies across 4 genres)
movies_data = {
    'movie_title': [
        'Inception', 'Interstellar', 'Oppenheimer', 
        'The Dark Knight', 'Extraction', 'John Wick 4',
        'Superbad', 'The Hangover', 'Golmaal',
        'Stree 2', 'The Conjuring', 'It'
    ],
    'genre': [
        'Sci-Fi', 'Sci-Fi', 'Sci-Fi',
        'Action', 'Action', 'Action',
        'Comedy', 'Comedy', 'Comedy',
        'Horror', 'Horror', 'Horror'
    ]
}

df_movies = pd.DataFrame(movies_data)

# Count movies per genre
genre_counts = df_movies['genre'].value_counts()
print("--- Movies Count per Genre ---")
print(genre_counts)

# Plotting the bar chart
plt.figure(figsize=(8, 5))
colors = ['#4A90E2', '#50E3C2', '#F5A623', '#E74C3C']
bars = plt.bar(genre_counts.index, genre_counts.values, color=colors, width=0.5, edgecolor='black', linewidth=0.8)

# Chart styling
plt.title("BookMyShow: Number of Movies per Genre", fontsize=14, fontweight='bold', pad=15)
plt.xlabel("Movie Genre", fontsize=12, labelpad=10)
plt.ylabel("Number of Movies", fontsize=12, labelpad=10)
plt.ylim(0, max(genre_counts.values) + 1)
plt.grid(axis='y', linestyle='--', alpha=0.5)

# Adding value annotations on top of each bar
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2.0, yval + 0.1, int(yval), ha='center', va='bottom', fontsize=11, fontweight='bold')

plt.tight_layout()
plt.savefig('movies_per_genre.png', dpi=300)
print("Bar chart successfully saved as 'movies_per_genre.png'.")
