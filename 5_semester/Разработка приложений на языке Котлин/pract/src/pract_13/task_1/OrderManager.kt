package pract_13.task_1

class OrderManager {
    private val orders = mutableListOf<Order>()

    fun addOrder(order: Order) {
        orders.add(order)
    }

    fun removeOrdersBelowPrice(threshold: Double) {
        orders.removeAll { it.totalPrice < threshold }
    }

    fun getUniqueCustomers(): Set<Int> {
        return orders.map { it.customerId }.toSet()
    }

    fun getTotalRevenue(): Double {
        return orders.sumOf { it.totalPrice }
    }

    fun getTop3MostExpensiveOrders(): List<Order> {
        return orders.sortedByDescending { it.totalPrice }.take(3)
    }

    fun displayAllOrders() {
        println("\nВсе заказы:")
        orders.forEach { order ->
            println("Заказ №${order.orderId}, Клиент: ${order.customerId}, " +
                    "Товары: ${order.products}, Сумма: ${order.totalPrice}")
        }
    }
}