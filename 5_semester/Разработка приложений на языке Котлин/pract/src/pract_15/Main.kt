package pract_15

fun main() {
    val cities = sequenceOf(
        CityAirQuality("Москва", "Россия", 65, 120, "2025-03-15"),
        CityAirQuality("Санкт-Петербург", "Россия", 40, 90, "2025-03-15"),
        CityAirQuality("Новосибирск", "Россия", 70, 130, "2025-03-15"),
        CityAirQuality("Лондон", "Великобритания", 30, 60, "2025-03-14"),
        CityAirQuality("Манчестер", "Великобритания", 55, 110, "2025-03-14"),
        CityAirQuality("Пекин", "Китай", 120, 200, "2025-03-13"),
        CityAirQuality("Шанхай", "Китай", 110, 190, "2025-03-13"),
        CityAirQuality("Берлин", "Германия", 25, 50, "2025-03-15"),
        CityAirQuality("Гамбург", "Германия", 35, 70, "2025-03-15"),
        CityAirQuality("Париж", "Франция", 45, 85, "2025-03-15"),
        CityAirQuality("Лион", "Франция", 60, 95, "2025-03-15")
    )


    println("1. Список всех городов:")
    cities.forEach { println(it) }
    println()


    val dangerousCities = cities.filter { it.pm25 > 50 }
    println("2. Города с опасным уровнем PM2.5 (>50):")
    dangerousCities.forEach { println("${it.city} (${it.country}): PM2.5 = ${it.pm25}") }
    println()


    val countryToCheck = "Россия"
    val allSafeInCountry = cities
        .filter { it.country == countryToCheck }
        .all { it.pm10 < 100 }
    println("3. Все ли города в $countryToCheck имеют PM10 < 100? $allSafeInCountry")
    println()


    println("4. Статистика по городам:")
    cities.map { city ->
        "Город: ${city.city}, PM2.5: ${city.pm25}, Статус: ${if (city.pm25 > 50) "Опасно" else "Нормально"}"
    }.forEach { println(it) }
    println()


    val groupedByCountry = cities.groupBy { it.country }
    println("5. Группировка по странам:")
    groupedByCountry.forEach { (country, list) ->
        println("$country: ${list.map { it.city }}")
    }
    println()


    val sortedByPm25 = cities.sortedByDescending { it.pm25 }
    println("6. Города, отсортированные по убыванию PM2.5:")
    sortedByPm25.forEach { println("${it.city}: PM2.5 = ${it.pm25}") }
    println()


    println("7. Средние показатели по странам:")
    groupedByCountry.forEach { (country, list) ->
        val avgPm25 = list.map { it.pm25 }.average()
        val avgPm10 = list.map { it.pm10 }.average()
        println("$country: средний PM2.5 = ${"%.2f".format(avgPm25)}, средний PM10 = ${"%.2f".format(avgPm10)}")
    }
}