package pract_8

fun main() {
    val coffee = DrinkType.COFFEE
    println("Полная информация о напитке:")
    println(coffee.getDrinkInfo())

    println("\nИнформация об отдельных параметрах:")
    println("Название: ${coffee.getFormattedName()}")
    println("Объем: ${coffee.getVolume()} мл")
    println("Горячий: ${coffee.isHot()}")
    println("Температура: ${coffee.temperature}°C")


    val tea = DrinkType.TEA
    println("\n\nПолная информация о напитке:")
    println(tea.getDrinkInfo())

    println("\nИнформация об отдельных параметрах:")
    println("Название: ${tea.getFormattedName()}")
    println("Объем: ${tea.getVolume()} мл")
    println("Горячий: ${tea.isHot()}")
    println("Температура: ${tea.temperature}°C")


    val juice = DrinkType.JUICE
    println("\n\nПолная информация о напитке:")
    println(juice.getDrinkInfo())

    println("\nИнформация об отдельных параметрах:")
    println("Название: ${juice.getFormattedName()}")
    println("Объем: ${juice.getVolume()} мл")
    println("Горячий: ${juice.isHot()}")
    println("Температура: ${juice.temperature}°C")


    val water = DrinkType.WATER
    println("\n\nПолная информация о напитке:")
    println(water.getDrinkInfo())

    println("\nИнформация об отдельных параметрах:")
    println("Название: ${water.getFormattedName()}")
    println("Объем: ${water.getVolume()} мл")
    println("Горячий: ${water.isHot()}")
    println("Температура: ${water.temperature}°C")
}