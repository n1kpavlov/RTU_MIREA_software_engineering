import csv
import matplotlib.pyplot as plt
from collections import defaultdict

def load_csv(filename):
    with open(filename, encoding='utf8') as f:
        return list(csv.reader(f, delimiter=','))

# Загружаем данные
messages = load_csv('messages.csv')[1:]
checks = load_csv('checks.csv')[1:]
statuses = load_csv('statuses.csv')[1:]
groups = load_csv('groups.csv')[1:]

# Словарь для связи message_id -> (variant, group)
message_to_student = {msg[0]: (msg[2], msg[3]) for msg in messages}

# Словарь названий групп
group_names = {g[0]: g[1] for g in groups}

# Считаем успешные решения по студентам
student_success = defaultdict(int)
success_statuses = {'OK', 'AC', 'AW'}

for check in checks:
    if check[3] in success_statuses:
        student_data = message_to_student.get(check[1])
        if student_data:
            student_success[student_data] += 1

# Считаем достижения по студентам
student_achievements = defaultdict(int)

for status in statuses:
    variant = status[1]
    group = status[2]
    achievements = status[5]
    if achievements.strip():
        count = len(achievements.split(','))
        student_achievements[(variant, group)] += count

# Вычисляем общий балл
student_scores = defaultdict(int)
all_students = set(student_success.keys()) | set(student_achievements.keys())

for student in all_students:
    variant, group = student
    solved = student_success.get(student, 0)
    achievements = student_achievements.get(student, 0)
    student_scores[student] = solved + achievements

# Сортируем студентов по убыванию баллов
top_students = sorted(
    student_scores.items(),
    key=lambda x: x[1],
    reverse=True
)[:10]

# Данные для графика
labels = [f"{group_names.get(gid, gid)}\nВариант {var}" for (var, gid), _ in top_students]
scores = [score for _, score in top_students]

plt.figure(figsize=(12, 6))
plt.bar(labels[::-1], scores[::-1], color='aqua')
plt.title('Топ-10 студентов по рейтингу', pad=20)
plt.xlabel('Студент')
plt.ylabel('Суммарный балл')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()