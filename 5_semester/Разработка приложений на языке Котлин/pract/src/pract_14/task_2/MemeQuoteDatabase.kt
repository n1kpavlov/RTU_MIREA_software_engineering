package pract_14.task_2

class MemeQuoteDatabase {
    private val entries = mutableListOf<Map<String, Any>>()

    fun addNewEntry(newEntry : Map<String, Any>) {
        entries.add(newEntry)
    }

    fun filterByType(type: String): List<Map<String, Any>> {
        return entries.filter { it["type"] == type }
    }

    fun findByAuthor(author: String): List<Map<String, Any>> {
        return entries.filter { (it["author"] as String).equals(author, ignoreCase = true) }
    }

    fun findByTag(tag: String): List<Map<String, Any>> {
        return entries.filter { entry ->
            val tags = entry["tags"] as List<String>
            tags.any { it.equals(tag, ignoreCase = true) }
        }
    }

    fun getAllUniqueAuthors(): Set<String> {
        return entries.map { it["author"] as String }.toSet()
    }

    fun getAllUniqueTags(): Set<String> {
        return entries.flatMap { it["tags"] as List<String> }.toSet()
    }

    fun groupByType(): Map<String, List<Map<String, Any>>> {
        return entries.groupBy { it["type"] as String }
    }

    fun printEntry(entry: Map<String, Any>, index: Int = -1) {
        val prefix = if (index > 0) "$index. " else "  "
        println("${prefix}Текст: ${entry["text"]}")
        println("${" ".repeat(prefix.length)}Автор: ${entry["author"]}")
        println("${" ".repeat(prefix.length)}Тип: ${entry["type"]}")
        println("${" ".repeat(prefix.length)}Теги: ${(entry["tags"] as List<String>).joinToString(", ")}\n")
    }

    fun printAllEntries() {
        println("Все записи в БД:")
        entries.forEachIndexed { i, entry ->
            println("\nЗапись ${i + 1}:")
            printEntry(entry)
        }
    }
}