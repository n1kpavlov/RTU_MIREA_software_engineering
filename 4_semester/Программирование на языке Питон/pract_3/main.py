import random
from itertools import groupby
import sys

s = ["1", "2", "3", "4", "5", "5", "11"]

#3.1
print([int(i) for i in s])

#3.2
print(len(set(s)))

#3.3
print(s[::-1])

#3.4
x = "5"
print([i for i, val in enumerate(s) if val == x])

#3.5
print(sum(int(s[i]) for i in range(0, len(s), 2)))

#3.6
print(max(s, key=len))

#3.7
x = 330
print(x % sum(map(int, str(x))) == 0)

#3.8
x = "ABBCCCDEF"
print([(char, len(list(group))) for char, group in groupby(x)])

#4.1
A = [[0, 2], [3, 0]]
B = [[1, 4], [2, 0]]

def multiply(A, B):
    C = []
    for i in range(len(A)):
        new = []
        for j in range(len(A[i])):
            new.append(A[i][j] * B[i][j])
        C.append(new)
    return C

print(multiply(A, B))

#4.2
A = [[0, 2, 1], [1, 0, 3], [0, 1, 1]]

def transpose(A):
    C = []
    for i in range(len(A)):
        new = []
        for j in range(len(A[i])):
            new.append(A[j][i])
        C.append(new)
    return C

print(transpose(A))

#4.3
A = [[1, 2], [3, 4], [5, 6]]
B = [[1, 2, 3], [4, 5, 6]]

def dot(A, B):
    C = []
    for i in range(len(A)):
        new = []
        for j in range(len(B[0])):
            sum = 0
            for k in range(len(B)):
                sum += A[i][k] * B[k][j]
            new.append(sum)
        C.append(new)
    return C

print(dot(A, B))

#5.1
name = ["ИВБО", "ИКБО", "ИМБО", "ИНБО"]
for nazv in name:
    count = 0
    result = ""
    if nazv == "ИВБО":
        count = 2
    elif nazv == "ИКБО":
        count = 7
        result += nazv + "-10-22 "
    elif nazv == "ИМБО":
        count = 1
    else:
        count = 3
    print(nazv)
    for i in range(1, count + 1):
        if (count == 7 and i == 3):
            result += nazv + "-34-22 "
        cal = 0
        if (count == 1):
            cal = 2
        elif (count == 2 and i == 2 or count == 7 and i == 2 or count == 7 and i == 5):
            cal = 3
        elif (count == 2 and i == 1 or count == 3 or count == 7 and i == 4):
            cal = 4
        elif (i == 1):
            cal = 6
        elif (i == 7):
            cal = 7
        elif (i == 6):
            cal = 8
        for j in range (0, cal):
            result += nazv + "-" + str(i) + str(j) + "-" + "23 "
        if (count == 7 and i == 2):
            result += nazv + "-24-22 "
        result += "\n"
    print(result)

#5.2
def my_print(*args, sep=' ', end='\n', file=sys.stdout):
    output = sep.join(map(str, args)) + end
    file.write(output)

my_print("Hello, world!", 123)
file = open("test.txt", 'w')
my_print(123, file=file)
file.close()

#5.3
def decrypt(v, k):
    v0, v1 = v[0], v[1]
    sum = 0xC6EF3720
    delta = 0x9E3779B9
    k0, k1, k2, k3 = k[0], k[1], k[2], k[3]

    for _ in range(32):
        v1 -= ((v0 << 4) + k2) ^ (v0 + sum) ^ ((v0 >> 5) + k3)
        v1 &= 0xFFFFFFFF
        v0 -= ((v1 << 4) + k0) ^ (v1 + sum) ^ ((v1 >> 5) + k1)
        v0 &= 0xFFFFFFFF
        sum -= delta
        sum &= 0xFFFFFFFF

    return [v0, v1]

encrypted_message = [
    0xE3238557, 0x6204A1F8, 0xE6537611, 0x174E5747,
    0x5D954DA8, 0x8C2DFE97, 0x2911CB4C, 0x2CB7C66B,
    0xE7F185A0, 0xC7E3FA40, 0x42419867, 0x374044DF,
    0x2519F07D, 0x5A0C24D4, 0xF4A960C5, 0x31159418,
    0xF2768EC7, 0xAEAF14CF, 0x071B2C95, 0xC9F22699,
    0xFFB06F41, 0x2AC90051, 0xA53F035D, 0x830601A7,
    0xEB475702, 0x183BAA6F, 0x12626744, 0x9B75A72F,
    0x8DBFBFEC, 0x73C1A46E, 0xFFB06F41, 0x2AC90051,
    0x97C5E4E9, 0xB1C26A21, 0xDD4A3463, 0x6B71162F,
    0x8C075668, 0x7975D565, 0x6D95A700, 0x7272E637
]

k = [0, 4, 5, 1]

decrypted_data = []
for i in range(0, len(encrypted_message), 2):
    v = [encrypted_message[i], encrypted_message[i + 1]]
    decrypted_pair = decrypt(v, k)
    decrypted_data.extend(chr(decrypted_pair[0]))
    decrypted_data.extend(chr(decrypted_pair[1]))

result = ''.join(decrypted_data)

print("Расшифрованное сообщение:")
print(result)

#6.1
data = {
        "begin": ["Коллеги,", "В то же время,", "Однако,", "Тем не менее,", "Следовательно,", "Соответственно,",
                   "Вместе с тем,", "С другой стороны,"],
        "themes": ["парадигма цифровой экономики", "контекст цифровой трансформации", "диджитализация бизнес-процессов",
                 "прамматичный подход к цифровым платформам", "совокупность сквозных технологий",
                 "программа прорывных исследований", "ускорение блокчейн-транзакций", "экспонентационный рост Big Data"],
        "move": ["открывает новые возможности для", "выдвигает новые требования", "несёт в себе риски", "расширяет горизонты",
                     "заставляет искать варианты", "не оставляет шанса для", "повышает вероятность", "обостряет проблему"],
        "move2": ["дальнейшего углубления", "бюджетного финансирования", "синергетического эффекта",
                    "компроментации конфиденциальных", "универсальной коммодитизации", "несанкционированной кастомизации",
                    "нормативного регулирования", "практического применения"],
        "objects": ["знаний и компетенций.", "непроверенных гипотез.", "волатильных активов.", "опасных экспериментов.",
                    "государственно-частных партнёрств.", "цифровых следов граждан.", "нежелательных последствий.", "внезапных открытий."]
    }

def generate_sentence(x):
    begin = random.choice(data["begin"])
    theme = random.choice(data["themes"])
    move = random.choice(data["move"])
    move2 = random.choice(data["move2"])
    object = random.choice(data["objects"])
    if (x == 0):
        return f"{data["begin"][0]} {theme} {move} {move2} {object}"
    else:
        return f"{begin} {theme} {move} {move2} {object}"

def generate_report(num_paragraphs=3):
    report = []
    report.append(generate_sentence(0))
    for _ in range(num_paragraphs):
        paragraph = " ".join([generate_sentence(1) for _ in range(3)])
        report.append(paragraph)
    return "\n".join(report)

print(generate_report())

#6.2
first_names = [
    "Александр", "Дмитрий", "Максим", "Сергей", "Андрей", "Алексей", "Иван", "Артем", "Никита", "Михаил",
    "Егор", "Кирилл", "Илья", "Даниил", "Матвей", "Тимофей", "Роман", "Владимир", "Ярослав", "Олег"
]
middle_names = [
    "А.", "Б.", "В.", "Г.", "Д.", "Е.", "Ж.", "З.", "И.", "К.", "Л.", "М.", "Н.", "О.", "П.", "Р.", "С.",
    "Т.", "У.", "Ф.", "Х.", "Ц.", "Ч.", "Ш.", "Щ.", "Э.", "Ю.", "Я."
]
surname_roots = [
    "Иван", "Петр", "Сидор", "Смирн", "Кузнец", "Поп", "Василь", "Михайл", "Новик", "Федор",
    "Мороз", "Волк", "Алекс", "Лебед", "Семен", "Егор", "Павл", "Козл", "Степан", "Никола",
    "Орл", "Андре", "Макар", "Никит", "Захар", "Борис", "Григор", "Дмитр", "Констан", "Лавр",
    "Роман", "Тихон", "Филип", "Яков", "Артем", "Геннад", "Евген", "Игор", "Клим", "Лев"
]
surname_endings = [
    "ов", "ев", "ин", "ский", "цкий", "енко", "ич", "ук", "юк", "овский", "евич", "ович", "енков", "овец", "инов"
]

def generate_surname():
    root = random.choice(surname_roots)
    ending = random.choice(surname_endings)
    surname = root + ending
    return surname

def generate_fio():
    first_name = random.choice(first_names)
    middle_name = random.choice(middle_names)
    surname = generate_surname()
    return f"{first_name} {middle_name} {surname}"

for _ in range(10):
    print(generate_fio())

#7.1
# Определение комнат
rooms = {
    'start': {
        'name': 'Начало лабиринта',
        'description': 'Вы в начале лабиринта. Сможете ли из него выбраться?',
        'actions': [
            {'description': 'Проход на запад.', 'target': 'room1'},
            {'description': 'Проход на восток.', 'target': 'room2'}
        ]
    },
    'room1': {
        'name': 'Комната №1',
        'description': 'Вы находитесь в комнате №1. Здесь темно и сыро.',
        'actions': [
            {'description': 'Проход на восток.', 'target': 'start'},
            {'description': 'Проход на север.', 'target': 'room3'}
        ]
    },
    'room2': {
        'name': 'Комната №2',
        'description': 'Вы находитесь в комнате №2. Здесь слышен шум воды.',
        'actions': [
            {'description': 'Проход на запад.', 'target': 'start'},
            {'description': 'Проход на юг.', 'target': 'room4'}
        ]
    },
    'room3': {
        'name': 'Комната №3',
        'description': 'Вы находитесь в комнате №3. Здесь тупик.',
        'actions': []
    },
    'room4': {
        'name': 'Комната №4',
        'description': 'Вы находитесь в комнате №4. Здесь разветвление.',
        'actions': [
            {'description': 'Проход на север.', 'target': 'room2'},
            {'description': 'Проход на восток.', 'target': 'room5'},
            {'description': 'Проход на запад.', 'target': 'room6'}
        ]
    },
    'room5': {
        'name': 'Комната №5',
        'description': 'Вы находитесь в комнате №5. Здесь жарко.',
        'actions': [
            {'description': 'Проход на запад.', 'target': 'room4'},
            {'description': 'Проход на юг.', 'target': 'room7'}
        ]
    },
    'room6': {
        'name': 'Комната №6',
        'description': 'Вы находитесь в комнате №6. Здесь тупик.',
        'actions': []
    },
    'room7': {
        'name': 'Комната №7',
        'description': 'Вы находитесь в комнате №7. Здесь прохладно.',
        'actions': [
            {'description': 'Проход на север.', 'target': 'room5'},
            {'description': 'Проход на восток.', 'target': 'room8'}
        ]
    },
    'room8': {
        'name': 'Комната №8',
        'description': 'Вы находитесь в комнате №8. Здесь разветвление.',
        'actions': [
            {'description': 'Проход на запад.', 'target': 'room7'},
            {'description': 'Проход на юг.', 'target': 'room9'},
            {'description': 'Проход на восток.', 'target': 'room10'}
        ]
    },
    'room9': {
        'name': 'Комната №9',
        'description': 'Вы находитесь в комнате №9. Здесь тупик.',
        'actions': []
    },
    'room10': {
        'name': 'Комната №10',
        'description': 'Вы находитесь в комнате №10. Это конец лабиринта!',
        'actions': []
    }
}

current_room = 'start'

while True:
    room = rooms[current_room]
    print(room['name'])
    print(room['description'])

    if not room['actions']:
        print("Игра завершена.")
        break

    for i, action in enumerate(room['actions'], 1):
        print(f"{i}. {action['description']}")

    choice = int(input("> ")) - 1
    if 0 <= choice < len(room['actions']):
        current_room = room['actions'][choice]['target']
    else:
        print("Неверный выбор. Попробуйте снова.")

#7.2
def find_dead_ends(rooms, start_room, end_room):
    visited = set()

    def dfs(current_room):
        if current_room == end_room:
            return True  # Достигли конечной комнаты
        if current_room in visited:
            return False  # Уже посещали эту комнату
        visited.add(current_room)

        for action in rooms[current_room]['actions']:
            if dfs(action['target']):
                return True  # Нашли путь до конечной комнаты
        return False  # Пути до конечной комнаты нет

    dead_ends = []
    for room in rooms:
        visited.clear()
        if not dfs(room):
            dead_ends.append(room)
    return dead_ends

start_room = 'start'
end_room = 'room10'

dead_ends = find_dead_ends(rooms, start_room, end_room)

if dead_ends:
    print("Тупики найдены в следующих комнатах:")
    for room in dead_ends:
        print(f"- {room}: {rooms[room]['name']}")
else:
    print("Тупиков не найдено.")