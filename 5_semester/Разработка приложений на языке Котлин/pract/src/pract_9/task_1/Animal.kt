package pract_9.task_1

abstract class Animal(val name: String) {
    protected var hunger: Int = 0
    protected var energy: Int = 100
    protected var happiness: Int = 100

    abstract fun wayOfBirth()
    abstract fun move()

    open fun eat() {
        hunger = maxOf(0, hunger - 60)
        energy = minOf(100, energy + 40)
        println("$name ест. Голод уменьшен.")
    }

    open fun sleep() {
        energy = minOf(100, energy + 70)
        hunger = minOf(100, hunger + 20)
        println("$name спит. Энергия восстановлена.")
    }

    open fun play() {
        happiness = minOf(100, happiness + 60)
        energy = maxOf(0, energy - 20)
        hunger = minOf(100, hunger + 10)
        println("$name играет. Счастье увеличено.")
    }

    fun getStatus(): String {
        return """
            Состояние $name:
            Голод: $hunger%
            Энергия: $energy%
            Счастье: $happiness%
        """.trimIndent()
    }

    fun updateState() {
        hunger = minOf(100, hunger + 5)
        energy = maxOf(0, energy - 3)
        if (hunger > 70 || energy < 30) {
            happiness = maxOf(0, happiness - 5)
        }
    }
}