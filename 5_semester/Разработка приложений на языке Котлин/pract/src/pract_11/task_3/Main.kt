package pract_11.task_3

fun main() {
    val intValidator = Validator<Int>()
    println("Целочисленное положительное число: ${intValidator.validate(10)}")

    val doubleValidator = Validator<Double>()
    println("Положительное число: ${doubleValidator.validate(34.75)}")

    println("Отрицательное число: ${doubleValidator.validate(-3.52)}")

    val stringValidator = Validator<String>()
    println("Строка (больше 5 элементов): ${stringValidator.validate("HelloWorld")}")

    println("Строка (меньше 5 элементов): ${stringValidator.validate("Hi")}")

    val testValidator = Validator<Char>()
    try {
        println("Буква: ${testValidator.validate('F')}")
    } catch (e: IllegalArgumentException) {
        println("Ошибка: ${e.message}")
    }
}