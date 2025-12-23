package pract_11.task_1

class Order {
    var products: List<Product> = emptyList()
    var total: Double = 0.0
    var status: String = "Создан"

    override fun toString(): String {
        return "\tПродукты: $products\n\tCтоимость = $total\n\tCтатус = $status"
    }
}