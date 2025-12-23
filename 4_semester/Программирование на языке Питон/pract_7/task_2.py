import csv
import datetime
import matplotlib.pyplot as plt
from collections import defaultdict

def parse_time(text):
    return datetime.datetime.strptime(text, '%Y-%m-%d %H:%M:%S.%f')

def load_csv(filename):
    with open(filename, encoding='utf8') as f:
        return list(csv.reader(f, delimiter=','))

messages = load_csv('messages.csv')[1:]

# Считаем активность по часам
hourly_activity = defaultdict(int)
for msg in messages:
    dt = parse_time(msg[4])
    hour = dt.hour
    hourly_activity[hour] += 1

hours = range(24)
activity_counts = [hourly_activity[hour] for hour in hours]

# Строим линейный график
plt.figure(figsize=(12, 5))
plt.bar(hours, activity_counts, color='aqua')
plt.title('Активность студентов по времени суток')
plt.xlabel('Час дня')
plt.ylabel('Количество сообщений')
plt.xticks(hours)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()