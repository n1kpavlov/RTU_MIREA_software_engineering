package pract_13.task_2

import java.time.LocalDate

fun main() {
    val sales = listOf(
        Sale(LocalDate.of(2025, 1, 15), "Ноутбук", 2, 50000.0),
        Sale(LocalDate.of(2025, 1, 20), "Смартфон", 5, 30000.0),
        Sale(LocalDate.of(2025, 2, 10), "Ноутбук", 1, 55000.0),
        Sale(LocalDate.of(2025, 2, 15), "Наушники", 10, 5000.0),
        Sale(LocalDate.of(2025, 2, 25), "Смартфон", 3, 32000.0),
        Sale(LocalDate.of(2025, 3, 5), "Планшет", 4, 25000.0)
    )

    val analyzer = SalesAnalyzer(sales)

    analyzer.displayAllSales()

    println("\nОбщая выручка: ${analyzer.getTotalRevenue()} руб.")

    println("\nПродажи по продуктам:")
    analyzer.getSalesByProduct().forEach { (product, quantity) ->
        println("$product: $quantity шт.")
    }

    println("\nПродажи за февраль 2025:")
    analyzer.getSalesByMonth(2, 2025).forEach { sale ->
        println("${sale.date}: ${sale.product} - ${sale.totalPrice} руб.")
    }

    println("\nПродукт с наибольшей выручкой: ${analyzer.getTopProductByRevenue()}")
}