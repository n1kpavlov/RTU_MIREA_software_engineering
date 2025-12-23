package pract_14.task_2

import kotlin.collections.chunked
import kotlin.collections.joinToString
import kotlin.system.exitProcess

fun addTestData(database: MemeQuoteDatabase) {
    database.addNewEntry(mapOf(
        "text" to "Быть или не быть, вот в чем вопрос",
        "author" to "Шекспир",
        "type" to "quote",
        "tags" to listOf("философия", "жизнь", "решение")
    ))

    database.addNewEntry(mapOf(
        "text" to "Я помню чудное мгновенье",
        "author" to "А.С. Пушкин",
        "type" to "poem",
        "tags" to listOf("любовь", "воспоминание", "красота")
    ))

    database.addNewEntry(mapOf(
        "text" to "Это просто бизнес, ничего личного",
        "author" to "Крестный отец",
        "type" to "quote",
        "tags" to listOf("бизнес", "кино", "серьезность")
    ))

    database.addNewEntry(mapOf(
        "text" to "Я к вам пишу — чего же боле?",
        "author" to "А.С. Пушкин",
        "type" to "poem",
        "tags" to listOf("любовь", "письмо", "эмоции")
    ))

    database.addNewEntry(mapOf(
        "text" to "Это СПАРТА!!!",
        "author" to "300 спартанцев",
        "type" to "meme",
        "tags" to listOf("кино", "мотивация", "эпично")
    ))

    database.addNewEntry(mapOf(
        "text" to "Даже не знаю, что сказать",
        "author" to "Internet Meme",
        "type" to "meme",
        "tags" to listOf("юмор", "растерянность", "интернет")
    ))
}

fun filterByType(database: MemeQuoteDatabase) {
    print("\nВведите тип для фильтрации: ")
    val type = readLine().toString()
    println("\nФильтрация по типу '${type}':")
    val search = database.filterByType(type)
    if (search.isEmpty()) {
        println("  Записей не найдено")
    } else {
        search.forEachIndexed { i, entry -> database.printEntry(entry, i + 1) }
    }
}

fun findByAuthor(database: MemeQuoteDatabase) {
    print("\nВведите искомого автора: ")
    val author = readLine().toString()
    println("\nПоиск по автору '${author}':")
    val search = database.findByAuthor(author)
    if (search.isEmpty()) {
        println("  Записей не найдено")
    } else {
        search.forEachIndexed { i, entry -> database.printEntry(entry, i + 1) }
    }
}

fun findByTag(database: MemeQuoteDatabase) {
    print("\nВведите искомый тег: ")
    val tag = readLine().toString()
    println("\nПоиск по тегу '${tag}':")
    val search = database.findByTag(tag)
    if (search.isEmpty()) {
        println("  Записей не найдено")
    } else {
        search.forEachIndexed { i, entry -> database.printEntry(entry, i + 1) }
    }
}

fun showStatistic(database: MemeQuoteDatabase) {
    println("\nСтатистика:")
    val uniqueAuthors = database.getAllUniqueAuthors()
    val uniqueTags = database.getAllUniqueTags()

    println("  Уникальные авторы (${uniqueAuthors.size}):")
    uniqueAuthors.forEachIndexed { i, author ->
        println("    ${i + 1}. $author")
    }

    println("\n  Уникальные теги (${uniqueTags.size}):")
    uniqueTags.chunked(4).forEachIndexed { i, chunk ->
        println("    ${chunk.joinToString(", ")}")
    }
    println()
}

fun groupByType(database: MemeQuoteDatabase) {
    println("\nГруппировка по типу:")
    val groupedByType = database.groupByType()

    groupedByType.forEach { (type, typeEntries) ->
        println("\n  Тип: '$type' (${typeEntries.size} записей)")
        typeEntries.forEachIndexed { i, entry ->
            println("    ${i + 1}. ${entry["text"]}")
            println("       Автор: ${entry["author"]}")
        }
    }
    println()
}

fun main() {
    val database = MemeQuoteDatabase()
    addTestData(database)

    while (true) {
        println("1. Фильтр по типу")
        println("2. Поиск по автору")
        println("3. Поиск по тегу")
        println("4. Показать статистику")
        println("5. Сгруппировать по типам")
        println("6. Вывести всю БД")
        println("0. Выход")
        print("Выберите опцию: ")

        when (readLine()?.toIntOrNull()) {
            1 -> filterByType(database)
            2 -> findByAuthor(database)
            3 -> findByTag(database)
            4 -> showStatistic(database)
            5 -> groupByType(database)
            6 -> database.printAllEntries()
            0 -> exitProcess(0)
            else -> println("Неверный ввод, попробуйте снова.\n")
        }
    }
}