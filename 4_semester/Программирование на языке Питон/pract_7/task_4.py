import csv
import matplotlib.pyplot as plt
import datetime
from collections import defaultdict

def load_csv(filename):
    with open(filename, encoding='utf8') as f:
        return list(csv.reader(f, delimiter=','))

def parse_time(text):
    return datetime.datetime.strptime(text, '%Y-%m-%d %H:%M:%S.%f')

# Загружаем данные
messages = load_csv('messages.csv')

# Словарь для хранения активности по задачам по времени
task_activity = defaultdict(lambda: defaultdict(int))

# Обрабатываем данные
for row in messages[1:]:
    task = row[1]
    timestamp = parse_time(row[4])
    date = timestamp.date()
    task_activity[task][date] += 1

# Визуализация
plt.figure(figsize=(12, 6))
for task, activity in task_activity.items():
    dates = sorted(activity.keys())
    counts = [activity[date] for date in dates]
    plt.plot(dates, counts, marker='o', label=f'Задача {task}')

plt.xlabel('Дата')
plt.ylabel('Количество сообщений')
plt.title('Изменение активности студентов по задачам с начала семестра')
plt.legend()
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
