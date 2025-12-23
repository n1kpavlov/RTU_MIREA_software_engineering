package pract_12.task_1

class UserProfile(
    val name: String?,
    val age: Int?,
    val hobby: String?,
    val favoriteColor: String?,
    val favoriteMovie: String?,
    val favoriteBook: String?
) {
    fun printProfileInfo() {
        println("Профиль пользователя:")
        println("Имя: ${name ?: "Не указано"}")
        println("Возраст: ${age ?: "Не указан"}")
        println("Хобби: ${hobby ?: "Не указано"}")
        println("Любимый цвет: ${favoriteColor ?: "Не указан"}")
        println("Любимый фильм: ${favoriteMovie ?: "Не указан"}")
        println("Любимая книга: ${favoriteBook ?: "Не указана"}")
        println()
    }
}