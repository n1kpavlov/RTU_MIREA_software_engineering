package pract_13.task_2

import java.time.LocalDate

data class Sale(
    val date: LocalDate,
    val product: String,
    val quantity: Int,
    val pricePerUnit: Double
) {
    val totalPrice: Double
        get() = quantity * pricePerUnit
}