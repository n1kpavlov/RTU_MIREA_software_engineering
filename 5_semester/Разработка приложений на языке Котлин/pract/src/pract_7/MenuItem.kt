package pract_7

import java.util.UUID

abstract class MenuItem {
    val id: String = UUID.randomUUID().toString()
    abstract val name: String
    abstract val basePrice: Double

    abstract fun calculateFinalPrice(): Double
}