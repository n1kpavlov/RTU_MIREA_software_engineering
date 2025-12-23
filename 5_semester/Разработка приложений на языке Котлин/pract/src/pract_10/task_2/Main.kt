package pract_10.task_2


fun main() {
    val userDatabase = object {
        val users = listOf(
            User("Алексей", 25, listOf("Мария", "Иван", "Елена")),
            User("Мария", 30, listOf("Алексей", "Дмитрий")),
            User("Иван", 35, listOf("Алексей", "Ольга", "Сергей")),
            User("Ольга", 28, listOf("Иван", "Елена")),
            User("Дмитрий", 42, listOf("Мария", "Сергей", "Анна")),
            User("Елена", 38, listOf("Алексей", "Ольга", "Анна")),
            User("Сергей", 45, listOf("Иван", "Дмитрий")),
            User("Анна", 29, listOf("Дмитрий", "Елена"))
        )

        fun findOldestUser(): User? {
            return users.maxByOrNull { it.age }
        }

        fun findMostSocialUsers(): List<User> {
            val maxFriends = users.maxOfOrNull { it.friends.size } ?: 0
            return users.filter { it.friends.size == maxFriends }
        }

        fun printStatistics() {
            println("\nОбщее количество пользователей: ${users.size}")
            println("Средний возраст: ${users.map { it.age }.average().toInt()} лет")
            println("Общее количество дружеских связей: ${users.sumOf { it.friends.size }}")
        }
    }

    val oldestUser = userDatabase.findOldestUser()
    println("\nСамый старший пользователь:")
    if (oldestUser != null) {
        println("Имя: ${oldestUser.name}, Возраст: ${oldestUser.age} лет")
        println("Друзья: ${oldestUser.friends.joinToString(", ")}")
    }

    val mostSocialUsers = userDatabase.findMostSocialUsers()
    println("\nСамые общительные пользователи (${mostSocialUsers.first().friends.size} друзей):")
    mostSocialUsers.forEach { user ->
        println("- ${user.name}, ${user.age} лет: ${user.friends.joinToString(", ")}")
    }

    userDatabase.printStatistics()
}