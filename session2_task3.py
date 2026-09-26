import pandas as pd

# Load the Spotify dataset
df = pd.read_csv('spotify_mini.csv')

print("--- Mini Spotify Dataset ---")
print(df.head(13))
print("\n" + "="*40 + "\n")

# Display the number of songs in each genre
genre_counts = df['genre'].value_counts()
print("--- Number of Songs per Genre ---")
print(genre_counts)
