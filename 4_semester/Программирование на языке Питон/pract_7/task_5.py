import csv
import matplotlib.pyplot as plt
from collections import defaultdict

def load_csv(filename):
    with open(filename, encoding='utf8') as f:
        return list(csv.reader(f, delimiter=','))

messages = load_csv('messages.csv')[1:]
groups = load_csv('groups.csv')[1:]

# Создаём словарь {group_id: количество сообщений}
group_activity = defaultdict(int)
for msg in messages:
    group_id = msg[3]
    group_activity[group_id] += 1

# Сопоставляем ID групп с их названиями (если есть)
group_names = {group[0]: group[1] for group in groups}

# Сортируем группы по убыванию активности
sorted_groups = sorted(
    group_activity.items(),
    key=lambda x: x[1],
    reverse=True
)

# Подготовка данных для графика
top_groups = sorted_groups[:10]
labels = [group_names.get(g[0], f"Группа {g[0]}") for g in top_groups]
values = [g[1] for g in top_groups]

# Построение графика
plt.figure(figsize=(12, 6))
plt.bar(labels, values, color='aqua')
plt.title('Топ самых активных групп по количеству сообщений')
plt.xlabel('Группа')
plt.ylabel('Количество сообщений')
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()