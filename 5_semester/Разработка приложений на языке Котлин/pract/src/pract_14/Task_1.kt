package pract_14

fun main() {
    val listA = listOf(1, 2, 5, 7, 8, 10, 12, 15, 20)
    val listB = listOf(2, 3, 5, 6, 8, 9, 11, 15, 18)

    val intersection = listA.intersect(listB)
    println("1. Товары, которые покупались и есть на складе: $intersection")

    val onlyInA = listA.subtract(listB)
    println("2. Товары, которые покупались, но отсутствуют на складе: $onlyInA")

    val union = listA.union(listB)
    println("3. Все уникальные товары (объединение): $union")
}