package pract_13.task_2

class SalesAnalyzer(private val sales: List<Sale>) {

    fun getTotalRevenue(): Double {
        return sales.sumOf { it.totalPrice }
    }

    fun getSalesByProduct(): Map<String, Int> {
        return sales.groupBy { it.product } .mapValues { (_, sales) -> sales.sumOf { it.quantity } }
    }

    fun getSalesByMonth(month: Int, year: Int): List<Sale> {
        return sales.filter {
            it.date.monthValue == month && it.date.year == year
        }
    }

    fun getTopProductByRevenue(): String {
        return sales.groupBy { it.product }
            .mapValues { (_, sales) -> sales.sumOf { it.totalPrice } }
            .maxByOrNull { it.value }
            ?.key ?: "Нет данных"
    }

    fun displayAllSales() {
        println("\nВсе продажи:")
        sales.forEach { sale ->
            println("${sale.date}: ${sale.product} x${sale.quantity} " +
                    "по ${sale.pricePerUnit} руб. = ${sale.totalPrice} руб.")
        }
    }
}