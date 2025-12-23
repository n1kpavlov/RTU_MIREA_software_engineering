package pract_9.task_1

class Bat : Mammal("Летучая мышь"), Flying {
    override fun move() {
        fly()
    }

    override fun fly() {
        println("Летучая мышь летает медленно")
        energy = maxOf(0, energy - 10)
    }
}