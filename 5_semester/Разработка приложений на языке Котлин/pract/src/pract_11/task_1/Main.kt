package pract_11.task_1

fun main() {
    val order = Order().apply {
        products = listOf(
            Product("Specialized S-Works Tarmac SL8", 17999.25),
            Product("RockShox Sid SL Ultimate", 850.50)
        )
        total = products.sumOf { it.price }
        status = "В сборке"
    }

    order.also {
        println("Заказ создан:\n$it")
    }

    val discount = order.let {
        if (it.total > 1000) it.total * 0.9 else it.total
    }

    println("\tСтоимость с учетом скидки: $discount")
}