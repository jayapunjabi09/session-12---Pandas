import pandas as pd

data = {
    'artist': ['Arijit Singh', 'Shreya Ghoshal', 'AP Dhillon',
               'Arijit Singh', 'Badshah', 'AP Dhillon'],
    'genre': ['Romantic', 'Romantic', 'Punjabi',
              'Romantic', 'Hip Hop', 'Punjabi'],
    'streams': [5000, 4000, 7000, 6000, 8000, 9000]
}

df = pd.DataFrame(data)

result = df.groupby('genre')['streams'].agg(['sum', 'mean'])

result = result.sort_values(
    by='sum',
    ascending=False
)

print("Spotify Streams by Genre:")
print(result)