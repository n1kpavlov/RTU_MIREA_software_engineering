package pract_8

open class Animal {
    open fun speak() = "Some sound"  // Функция open для переопределения
}
class Cat : Animal() {
    override fun speak() = "Meow!"
}
fun main() {
    val cat = Cat()
    println(cat.speak())
}