import csv
from collections import defaultdict
import matplotlib.pyplot as plt

def load_games(filename):
    games = []
    with open(filename, encoding='utf8') as f:
        reader = csv.reader(f, delimiter=';')
        for row in reader:
            cleaned_row = [field.strip('"').strip() for field in row]
            if len(cleaned_row) >= 4:
                games.append({
                    'title': cleaned_row[0],
                    'genre': cleaned_row[1],
                    'url': cleaned_row[2],
                    'year': cleaned_row[3]
                })
    return games

games = load_games('GAMES.csv')

# Подсчет количества игр по жанрам
genre_counts = defaultdict(int)
for game in games:
    genre = game['genre']
    genre_counts[genre] += 1

# Сортировка жанров по количеству игр (по убыванию)
sorted_genres = sorted(genre_counts.items(), key=lambda x: x[1], reverse=True)

# Подготовка данных для графика
genres = [genre for genre, count in sorted_genres]
counts = [count for genre, count in sorted_genres]

# Создание графика
plt.figure(figsize=(12, 6))
plt.bar(genres, counts, color='aqua')
plt.title('Количество игр по жанрам')
plt.xlabel('Жанр')
plt.ylabel('Количество игр')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()