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

# Считаем активность по дням недели
daily_activity = defaultdict(int)
for msg in messages:
    dt = parse_time(msg[4])
    day = dt.weekday()
    daily_activity[day] += 1

# Названия дней недели
days = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
activity_counts = [daily_activity[i] for i in range(7)]

# Строим столбчатую диаграмму
plt.figure(figsize=(10, 5))
plt.bar(days, activity_counts, color='aqua')
plt.title('Активность студентов по дням недели')
plt.xlabel('День недели')
plt.ylabel('Количество сообщений')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()