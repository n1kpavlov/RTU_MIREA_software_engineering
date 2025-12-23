import csv
import matplotlib.pyplot as plt
from collections import defaultdict


def load_csv(filename):
    with open(filename, encoding='utf8') as f:
        return list(csv.reader(f, delimiter=','))

messages = load_csv('messages.csv')[1:]
statuses = load_csv('statuses.csv')[1:]
groups = load_csv('groups.csv')[1:]

# Словарь для подсчёта уникальных вариантов
group_task_variants = defaultdict(lambda: defaultdict(set))

for msg in messages:
    group_id = msg[3]
    task = msg[1]
    variant = msg[2]
    group_task_variants[group_id][task].add(variant)

# Словарь для уникальных достижений
group_achievements = defaultdict(set)

for status in statuses:
    group_id = status[2]
    achievements = status[5].strip()
    if achievements:
        for ach in achievements.split(','):
            group_achievements[group_id].add(ach)

# Вычисляем метрики для групп
group_metrics = []
for group_id in set(group_task_variants.keys()) | set(group_achievements.keys()):
    tasks = group_task_variants[group_id]
    avg_variants = sum(len(variants) for variants in tasks.values()) / len(tasks) if tasks else 0

    unique_achievements = len(group_achievements.get(group_id, set()))

    group_metrics.append({
        'group_id': group_id,
        'avg_variants': round(avg_variants, 2),
        'unique_achievements': unique_achievements,
        'score': avg_variants + unique_achievements
    })

# Сортируем группы по убыванию общего показателя
sorted_groups = sorted(group_metrics, key=lambda x: x['score'], reverse=True)

top_groups = sorted_groups[:10]
labels = [next((g[1] for g in groups if g[0] == gr['group_id']), f"Группа {gr['group_id']}")
          for gr in top_groups]
variants = [gr['avg_variants'] for gr in top_groups]
achievements = [gr['unique_achievements'] for gr in top_groups]

plt.figure(figsize=(12, 6))
plt.bar(labels, variants, color='aqua', label='Уникальные варианты на задачу')
plt.bar(labels, achievements, bottom=variants, color='orange', label='Уникальные достижения')
plt.title('Разнообразие решений в топ-10 группах')
plt.xlabel('Группа')
plt.ylabel('Баллы разнообразия')
plt.xticks(rotation=45, ha='right')
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()