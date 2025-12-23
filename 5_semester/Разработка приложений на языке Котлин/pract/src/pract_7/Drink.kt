package pract_7

class Drink(
    override val name: String,
    override val basePrice: Double,
    val size: Size
): MenuItem() {
    final override fun calculateFinalPrice(): Double {
        return when (size) {
            Size.SMALL -> basePrice * 1.0
            Size.MEDIUM -> basePrice * 1.5
            Size.LARGE -> basePrice * 2.0
        }
    }
}