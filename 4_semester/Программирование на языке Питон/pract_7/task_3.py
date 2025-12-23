import csv
from collections import defaultdict
import matplotlib.pyplot as plt

def load_csv(filename):
    with open(filename, encoding='utf8') as f:
        return list(csv.reader(f, delimiter=','))

messages = load_csv('messages.csv')[1:]

# Считаем количество сообщений по каждой задаче
task_counts = defaultdict(int)
for msg in messages:
    task = msg[1]
    task_counts[task] += 1

# Выводим среднее количество сообщений на задачу
total_messages = sum(task_counts.values())
total_tasks = len(task_counts)
average_messages = total_messages / total_tasks

tasks = sorted(task_counts.keys(), key=lambda x: int(x))
counts = [task_counts[task] for task in tasks]

plt.figure(figsize=(12, 5))
plt.bar(tasks, counts, color='skyblue')
plt.title('Количество сообщений по задачам')
plt.xlabel('Номер задачи')
plt.ylabel('Количество сообщений')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()