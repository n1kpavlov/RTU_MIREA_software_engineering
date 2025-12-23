import curses
import time
import signal
import os
import random
import threading


snake = []
direction_y, direction_x = 0, 0
apple_y, apple_x = -1, -1
running = True

def save_state_and_exit(signum, frame):
    """Сохраняет состояние игры и завершает программу."""
    global running
    running = False
    with open("state.txt", "w") as f:
        f.write(f"{direction_y} {direction_x}\n")
        for segment in snake:
            f.write(f"{segment[0]} {segment[1]}\n")
        f.write(f"{apple_y} {apple_x}\n")

def load_state():
    """Загружает состояние игры из файла."""
    global snake, direction_y, direction_x, apple_y, apple_x
    if os.path.exists("state.txt"):
        with open("state.txt", "r") as f:
            lines = f.readlines()
            if len(lines) > 0:
                direction_y, direction_x = map(int, lines[0].split())
                snake = [tuple(map(int, line.split())) for line in lines[1:-1]]
                apple_y, apple_x = map(int, lines[-1].split())

def place_apple(height, width):
    """Размещает яблоко в случайной позиции на экране."""
    global apple_y, apple_x
    while True:
        apple_y = random.randint(0, height - 1)
        apple_x = random.randint(0, width - 1)
        if (apple_y, apple_x) not in snake:
            break

def reset_snake(height, width):
    """Сбрасывает змейку в центр экрана с начальной длиной."""
    global snake
    snake = [(height // 2, width // 2)]

def input_thread(stdscr):
    """Поток для обработки ввода."""
    global direction_y, direction_x, running
    while running:
        key = stdscr.getch()
        if key == curses.KEY_DOWN and direction_y != -1:
            direction_y, direction_x = 1, 0
        elif key == curses.KEY_UP and direction_y != 1:
            direction_y, direction_x = -1, 0
        elif key == curses.KEY_RIGHT and direction_x != -1:
            direction_y, direction_x = 0, 1
        elif key == curses.KEY_LEFT and direction_x != 1:
            direction_y, direction_x = 0, -1
        elif key == ord('q'):
            save_state_and_exit(None, None)

def game_thread(stdscr):
    """Поток для обновления игры."""
    global snake, direction_y, direction_x, apple_y, apple_x, running
    height, width = stdscr.getmaxyx()

    if not snake:
        reset_snake(height, width)

    if apple_y == -1 or apple_x == -1:
        place_apple(height, width)

    while running:
        stdscr.clear()
        stdscr.addch(apple_y, apple_x, '@')
        for segment in snake:
            stdscr.addch(segment[0], segment[1], '*')
        stdscr.refresh()

        new_head = (
            (snake[0][0] + direction_y) % height,
            (snake[0][1] + direction_x) % width
        )

        if new_head in snake:
            reset_snake(height, width)
            place_apple(height, width)
            continue

        snake.insert(0, new_head)

        if new_head == (apple_y, apple_x):
            place_apple(height, width)
        else:
            snake.pop()

        if direction_x != 0:
            time.sleep(0.05)
        else:
            time.sleep(0.1)

def main(stdscr):
    """Основная функция."""
    global running

    load_state()

    signal.signal(signal.SIGINT, save_state_and_exit)

    curses.curs_set(0)
    stdscr.keypad(True)
    stdscr.nodelay(True)
    stdscr.timeout(100)

    input_handler = threading.Thread(target=input_thread, args=(stdscr,))
    game_updater = threading.Thread(target=game_thread, args=(stdscr,))

    input_handler.start()
    game_updater.start()

    while running:
        time.sleep(0.1)

    input_handler.join()
    game_updater.join()

if __name__ == "__main__":
    curses.wrapper(main)