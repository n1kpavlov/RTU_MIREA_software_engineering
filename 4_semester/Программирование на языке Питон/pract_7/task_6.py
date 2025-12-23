import csv
from collections import defaultdict
import matplotlib.pyplot as plt

def load_csv(filename):
    with open(filename, encoding='utf8') as f:
        return list(csv.reader(f, delimiter=','))

statuses = load_csv('statuses.csv')[1:]
groups = load_csv('groups.csv')[1:]

# Подсчет правильных решений по группам (статус '2')
group_correct = defaultdict(int)
for row in statuses:
    if row[4] == '2':
        group_id = row[2]
        group_correct[group_id] += 1

# Создаем список кортежей (group_id, correct_count) и сортируем по убыванию
sorted_groups = sorted(group_correct.items(), key=lambda x: x[1], reverse=True)[:10]

# Сопоставляем ID групп с их названиями
group_names = {group[0]: group[1] for group in groups}

# Подготовка данных для графика
group_titles = []
correct_counts = []
for group_id, count in sorted_groups:
    group_titles.append(group_names.get(group_id, group_id))
    correct_counts.append(count)

# Построение графика
plt.figure(figsize=(12, 6))
plt.bar(group_titles, correct_counts, color='aqua')
plt.title('Количество правильных решений по группам')
plt.xlabel('Группа')
plt.ylabel('Правильные решения')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()