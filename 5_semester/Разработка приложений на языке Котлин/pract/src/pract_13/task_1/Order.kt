package pract_13.task_1

data class Order(
    val orderId: Int,
    val customerId: Int,
    val products: List<String>,
    val totalPrice: Double
)