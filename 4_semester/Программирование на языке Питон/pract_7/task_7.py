import csv
from collections import defaultdict
import matplotlib.pyplot as plt


def load_csv(filename):
    with open(filename, encoding='utf8') as f:
        return list(csv.reader(f, delimiter=','))

statuses = load_csv('statuses.csv')[1:]

# Создаем словарь для хранения статистики по задачам
task_stats = defaultdict(lambda: {'count': 0, 'sum': 0})

# Собираем статистику
for row in statuses:
    task = row[0]
    try:
        status = int(row[4])
    except ValueError:
        continue

    task_stats[task]['count'] += 1
    task_stats[task]['sum'] += status

# Вычисляем средний статус для каждой задачи
tasks = []
means = []
for task in sorted(task_stats.keys()):
    stats = task_stats[task]
    mean = stats['sum'] / stats['count'] if stats['count'] > 0 else 0
    tasks.append(task)
    means.append(mean)

# Вычисляем общее среднее
total_mean = sum(mean * task_stats[task]['count'] for task, mean in zip(tasks, means)) / sum(
    task_stats[task]['count'] for task in tasks)

# Построение графика
plt.figure(figsize=(12, 6))
plt.bar(tasks, means, color='aqua')
plt.axhline(y=total_mean, color='r', linestyle='--')
plt.title('Сложность задач (средний статус решения)')
plt.xlabel('Задача')
plt.ylabel('Средний статус (2=правильно)')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()