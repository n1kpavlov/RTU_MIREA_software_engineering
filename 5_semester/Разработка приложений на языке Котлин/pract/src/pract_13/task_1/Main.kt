package pract_13.task_1

fun main() {
    val orderManager = OrderManager()

    val order1 = Order(1, 1, listOf("Ноутбук", "Мышь"), 75000.0)
    val order2 = Order(2, 2, listOf("Смартфон"), 45000.0)
    val order3 = Order(3, 1, listOf("Наушники", "Чехол"), 12000.0)
    val order4 = Order(4, 3, listOf("Планшет", "Клавиатура"), 55000.0)
    val order5 = Order(5, 4, listOf("Монитор"), 30000.0)

    orderManager.addOrder(order1)
    orderManager.addOrder(order2)
    orderManager.addOrder(order3)
    orderManager.addOrder(order4)
    orderManager.addOrder(order5)

    orderManager.displayAllOrders()

    println("\nУникальные клиенты: ${orderManager.getUniqueCustomers()}")

    println("\nОбщая выручка: ${orderManager.getTotalRevenue()} руб.")

    println("\nТоп 3 самых дорогих заказа:")
    orderManager.getTop3MostExpensiveOrders().forEachIndexed { index, order ->
        println("${index + 1}. Заказ №${order.orderId} - ${order.totalPrice} руб.")
    }

    println("\nУдаление заказов до 40000 руб:")
    orderManager.removeOrdersBelowPrice(40000.0)

    orderManager.displayAllOrders()
}