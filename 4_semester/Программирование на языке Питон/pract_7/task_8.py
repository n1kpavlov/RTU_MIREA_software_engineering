import csv
import matplotlib.pyplot as plt
from collections import defaultdict

def load_csv(filename):
    with open(filename, encoding='utf8') as f:
        return list(csv.reader(f, delimiter=','))

statuses = load_csv('statuses.csv')[1:]
groups = load_csv('groups.csv')[1:]

# Словарь для подсчёта достижений: {group_id: total_achievements}
group_achievements = defaultdict(int)

for status in statuses:
    group_id = status[2]
    achievements = status[5]
    if achievements.strip():
        count = len(achievements.split(','))
        group_achievements[group_id] += count

# Сопоставляем ID групп с их названиями
group_names = {group[0]: group[1] for group in groups}

# Сортируем группы по убыванию достижений
sorted_groups = sorted(
    group_achievements.items(),
    key=lambda x: x[1],
    reverse=True
)

# Подготовка данных для графика (топ-10 групп)
top_groups = sorted_groups[:10]
labels = [group_names.get(g[0], f"Группа {g[0]}") for g in top_groups]
values = [g[1] for g in top_groups]

# Настройка графика
plt.figure(figsize=(12, 6))
plt.bar(labels, values, color='aqua')
plt.title('Топ групп по количеству достижений')
plt.xlabel('Группа')
plt.ylabel('Число достижений')
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()