import csv
from collections import defaultdict
import matplotlib.pyplot as plt
import re

def load_games(filename):
    games = []
    with open(filename, encoding='utf8') as f:
        reader = csv.reader(f, delimiter=';')
        for row in reader:
            year_match = re.search(r'(\d{4})', row[3])
            if year_match:
                games.append({
                    'title': row[0].strip('"').strip(),
                    'genre': row[1].strip('"').strip(),
                    'url': row[2].strip('"').strip(),
                    'year': int(year_match.group(1))
                })
    return games

games = load_games('GAMES.csv')

# Подсчет количества игр по годам
year_counts = defaultdict(int)
for game in games:
    year_counts[game['year']] += 1

# Сортировка годов по возрастанию
sorted_years = sorted(year_counts.items())

# Подготовка данных для графика
years = [str(year) for year, count in sorted_years]
counts = [count for year, count in sorted_years]

# Создание графика
plt.figure(figsize=(12, 6))
plt.bar(years, counts, color='aqua')
plt.title('Количество выпущенных игр по годам')
plt.xlabel('Год выпуска')
plt.ylabel('Количество игр')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()