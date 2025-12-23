package pract_9.task_1

fun main() {
    val animals = mutableListOf<Animal>(
        Bat(),
        Dolphin(),
        GoldFish(),
        Eagle()
    )

    fun showAllAnimals() {
        println("\nВСЕ ЖИВОТНЫЕ:")
        animals.forEachIndexed { index, animal ->
            println("${index + 1}. ${animal.name}")
        }
    }

    fun showAnimalStatus(index: Int) {
        if (index in 1..animals.size) {
            val animal = animals[index - 1]
            println("\n${animal.name.uppercase()}:")
            println(animal.getStatus())
        } else {
            println("Некорректный номер животного")
        }
    }

    fun interactWithAnimal(index: Int) {
        if (index !in 1..animals.size) {
            println("Некорректный номер животного")
            return
        }

        val animal = animals[index - 1]

        while (true) {
            println("\nВЗАИМОДЕЙСТВИЕ С ${animal.name.uppercase()}:")
            println("1. Покормить")
            println("2. Уложить спать")
            println("3. Поиграть")
            println("4. Узнать способ рождения")
            println("5. Движение")
            println("6. Показать статус")
            println("0. Назад")

            print("Выберите действие: ")
            when (readLine()?.toIntOrNull()) {
                1 -> animal.eat()
                2 -> animal.sleep()
                3 -> animal.play()
                4 -> animal.wayOfBirth()
                5 -> animal.move()
                6 -> println(animal.getStatus())
                0 -> break
                else -> println("Некорректный выбор")
            }

            animal.updateState()
        }
    }

    fun updateAllAnimals() {
        animals.forEach { it.updateState() }
        println("Состояние всех животных обновлено")
    }

    fun showMainMenu() {
        while (true) {
            println("\nСИСТЕМА УПРАВЛЕНИЯ ЖИВОТНЫМИ:")
            println("1. Показать всех животных")
            println("2. Показать статус животного")
            println("3. Взаимодействовать с животным")
            println("4. Обновить состояние всех животных")
            println("5. Выйти")

            print("Выберите опцию: ")
            when (readLine()?.toIntOrNull()) {
                1 -> showAllAnimals()
                2 -> {
                    showAllAnimals()
                    print("Выберите животное: ")
                    val index = readLine()?.toIntOrNull() ?: 0
                    showAnimalStatus(index)
                }
                3 -> {
                    showAllAnimals()
                    print("Выберите животное: ")
                    val index = readLine()?.toIntOrNull() ?: 0
                    interactWithAnimal(index)
                }
                4 -> updateAllAnimals()
                5 -> {
                    println("До свидания!")
                    return
                }
                else -> println("Некорректный выбор")
            }
        }
    }

    println("Добро пожаловать в систему управления животными!")
    showMainMenu()
}