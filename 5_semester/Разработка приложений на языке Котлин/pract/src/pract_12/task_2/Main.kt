package pract_12.task_2

import kotlin.system.exitProcess

fun Double.celsiusToFahrenheit(): Double = this * 9 / 5 + 32
fun Double.fahrenheitToCelsius(): Double = (this - 32) * 5 / 9
fun Double.kilometersToMiles(): Double = this * 0.621371
fun Double.milesToKilometers(): Double = this / 0.621371
fun Double.kilogramsToPounds(): Double = this * 2.20462
fun Double.poundsToKilograms(): Double = this / 2.20462

fun convertTemperatureToFahrenheit() {
    print("Введите температуру в °C: ")
    val celsius = readLine()?.toDoubleOrNull()
    if (celsius != null) {
        println("$celsius °C = ${celsius.celsiusToFahrenheit()} °F\n")
    } else {
        println("Ошибка ввода.\n")
    }
}

fun convertTemperatureToCelsius() {
    print("Введите температуру в °F: ")
    val fahrenheit = readLine()?.toDoubleOrNull()
    if (fahrenheit != null) {
        println("$fahrenheit °F = ${fahrenheit.fahrenheitToCelsius()} °C\n")
    } else {
        println("Ошибка ввода.\n")
    }
}

fun convertKilometersToMiles() {
    print("Введите расстояние в км: ")
    val km = readLine()?.toDoubleOrNull()
    if (km != null) {
        println("$km км = ${km.kilometersToMiles()} миль\n")
    } else {
        println("Ошибка ввода.\n")
    }
}

fun convertMilesToKilometers() {
    print("Введите расстояние в милях: ")
    val miles = readLine()?.toDoubleOrNull()
    if (miles != null) {
        println("$miles миль = ${miles.milesToKilometers()} км\n")
    } else {
        println("Ошибка ввода.\n")
    }
}

fun convertKilogramsToPounds() {
    print("Введите вес в кг: ")
    val kg = readLine()?.toDoubleOrNull()
    if (kg != null) {
        println("$kg кг = ${kg.kilogramsToPounds()} фунтов\n")
    } else {
        println("Ошибка ввода.\n")
    }
}

fun convertPoundsToKilograms() {
    print("Введите вес в фунтах: ")
    val pounds = readLine()?.toDoubleOrNull()
    if (pounds != null) {
        println("$pounds фунтов = ${pounds.poundsToKilograms()} кг\n")
    } else {
        println("Ошибка ввода.\n")
    }
}

fun main() {
    while (true) {
        println("Конвертер единиц:")
        println("1. Температура: Цельсий → Фаренгейт")
        println("2. Температура: Фаренгейт → Цельсий")
        println("3. Расстояние: Километры → Мили")
        println("4. Расстояние: Мили → Километры")
        println("5. Вес: Килограммы → Фунты")
        println("6. Вес: Фунты → Килограммы")
        println("0. Выход")
        print("Выберите опцию: ")

        when (readLine()?.toIntOrNull()) {
            1 -> convertTemperatureToFahrenheit()
            2 -> convertTemperatureToCelsius()
            3 -> convertKilometersToMiles()
            4 -> convertMilesToKilometers()
            5 -> convertKilogramsToPounds()
            6 -> convertPoundsToKilograms()
            0 -> exitProcess(0)
            else -> println("Неверный ввод, попробуйте снова.\n")
        }
    }
}