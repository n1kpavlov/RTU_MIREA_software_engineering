package pract_4

import kotlin.system.exitProcess

fun main() {
    println("=== ТЕКСТОВЫЙ КВЕСТ: ПОБЕГ ИЗ ЛАБИРИНТА ===")
    startGame()
}

fun startGame() {
    fun showMenu() {
        println("\n=== ГЛАВНОЕ МЕНЮ ===")
        println("1. Начать игру")
        println("2. Правила игры")
        println("3. Выход")
        print("Выберите вариант: ")
    }

    fun handleChoice(choice: Int) {
        when (choice) {
            1 -> beginAdventure()
            2 -> showRules()
            3 -> {
                println("До свидания!")
                exitProcess(0)
            }
            else -> println("Неверный выбор. Попробуйте снова.")
        }
    }

    while (true) {
        showMenu()
        val choice = readln().toInt()
        handleChoice(choice)
    }
}

fun showRules() {
    println("\n=== ПРАВИЛА ИГРЫ ===")
    println("• Выбирайте варианты действий, вводя соответствующие цифры")
    println("• Принимайте решения осторожно - они влияют на концовку")
    println("• Цель: найти выход из лабиринта")
    println("\nНажмите Enter чтобы продолжить...")
    readln()
}

fun beginAdventure() {
    println("\n" + "=".repeat(50))
    println("Вы просыпаетесь в темном каменном помещении.")
    println("Вокруг тишина, лишь капает вода где-то вдалеке.")
    println("Перед вами три прохода...")

    firstChoice()
}

fun firstChoice() {
    val options = listOf(
        "Пойти в левый проход",
        "Пойти в центральный проход",
        "Пойти в правый проход"
    )

    val handleFirstChoice: (Int) -> Unit = { choice ->
        when (choice) {
            1 -> leftPath()
            2 -> centerPath()
            3 -> rightPath()
            else -> {
                println("Неверный выбор.")
                firstChoice()
            }
        }
    }

    showOptions(options, handleFirstChoice)
}

fun leftPath() {
    println("\nВы идете по левому проходу.")
    println("Туннель становится уже, воздух спертый.")
    println("Впереди замечаете слабый свет...")

    val options = listOf(
        "Ускорить шаг и двигаться к свету",
        "Вернуться назад",
        "Осмотреться внимательнее"
    )

    val handleLeftChoice: (Int) -> Unit = { choice ->
        when (choice) {
            1 -> {
                println("\nВы вышли к выходу! Это был правильный путь!")
                println("Поздравляем с успешным побегом!")
                showEndMenu()
            }
            2 -> {
                println("\nВы возвращаетесь к началу.")
                firstChoice()
            }
            3 -> {
                println("\nПри внимательном осмотре вы замечаете скрытую дверь.")
                println("Она ведет к сокровищнице! Альтернативная победа!")
                showEndMenu()
            }
            else -> leftPath()
        }
    }

    showOptions(options, handleLeftChoice)
}

fun centerPath() {
    println("\nЦентральный проход ведет в большой зал.")
    println("В центре зала стоит древний каменный стол.")
    println("На столе лежит старая книга и загадочный ключ...")

    val options = listOf(
        "Взять ключ и продолжить путь",
        "Прочитать книгу",
        "Вернуться назад"
    )

    val handleCenterChoice: (Int) -> Unit = { choice ->
        when (choice) {
            1 -> {
                println("\nС ключом в руке вы находите запертую дверь.")
                println("Ключ подходит! Вы на свободе!")
                showEndMenu()
            }
            2 -> {
                println("\nВ книге написаны древние заклинания.")
                println("Вы случайно активируете магический портал!")
                println("Вас затягивает в неизвестность...")
                showEndMenu()
            }
            3 -> {
                println("\nВы возвращаетесь к началу.")
                firstChoice()
            }
            else -> centerPath()
        }
    }

    showOptions(options, handleCenterChoice)
}

fun rightPath() {
    println("\nПравый проход ведет вниз по крутой лестнице.")
    println("Внизу слышатся странные звуки...")
    println("Лестница заканчивается перед подземной рекой.")

    val options = listOf(
        "Попытаться перейти реку вброд",
        "Поискать другой путь",
        "Вернуться назад"
    )

    val handleRightChoice: (Int) -> Unit = { choice ->
        when (choice) {
            1 -> {
                println("\nТечение слишком сильное! Вас сносит водой...")
                println("К сожалению, это конец вашего путешествия.")
                showEndMenu()
            }
            2 -> {
                println("\nВы находите старую лодку и переплываете реку.")
                println("На другом берегу - выход на свободу!")
                showEndMenu()
            }
            3 -> {
                println("\nВы возвращаетесь к началу.")
                firstChoice()
            }
            else -> rightPath()
        }
    }

    showOptions(options, handleRightChoice)
}

fun showOptions(options: List<String>, handler: (Int) -> Unit) {
    println("\nВаши варианты:")
    options.forEachIndexed { index, option ->
        println("${index + 1}. $option")
    }
    print("Выберите действие (1-${options.size}): ")

    val choice = readln().toInt()
    if (choice in 1..options.size) {
        handler(choice)
    } else {
        println("Неверный выбор. Попробуйте снова.")
        showOptions(options, handler)
    }
}

fun showEndMenu() {
    val options = listOf(
        "Начать заново",
        "В главное меню",
        "Выйти из игры"
    )

    val handleEndChoice: (Int) -> Unit = { choice ->
        when (choice) {
            1 -> beginAdventure()
            2 -> startGame()
            3 -> {
                println("Спасибо за игру!")
                exitProcess(0)
            }
            else -> showEndMenu()
        }
    }

    println("\n" + "=".repeat(30))
    println("ИГРА ЗАВЕРШЕНА")
    showOptions(options, handleEndChoice)
}