package pract_7

fun main() {
    val coffee = Drink("Капучино", 150.0, Size.MEDIUM)
    println("Напиток: ${coffee.name}, Цена: ${coffee.calculateFinalPrice()} руб.")

    val salad = Food(
        "Цезарь",
        300.0,
        listOf(
            Ingredient("Салат", false),
            Ingredient("Курица", false),
            Ingredient("Соус", true)
        )
    )
    println("Блюдо: ${salad.name}, Вегетарианское: ${salad.isVegetarian}, Цена: ${salad.calculateFinalPrice()} руб.")
}