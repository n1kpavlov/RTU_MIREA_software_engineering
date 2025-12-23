package pract_12.task_1

fun main() {
    val user1 = UserProfile(
        name = "Никита",
        age = 20,
        hobby = "Хобби-хорсинг",
        favoriteColor = "Застенчивый паук",
        favoriteMovie = "Зеленый слоник",
        favoriteBook = "Методичка по ОС"
    )

    val user2 = UserProfile(
        name = null,
        age = null,
        hobby = null,
        favoriteColor = null,
        favoriteMovie = null,
        favoriteBook = null
    )

    user1.printProfileInfo()
    user2.printProfileInfo()
}