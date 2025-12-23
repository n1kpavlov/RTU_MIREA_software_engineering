package pract_9.task_1

class Eagle : Bird("Орел"), Flying {
    override fun move() {
        fly()
    }

    override fun fly() {
        println("Орел летает быстро")
        energy = maxOf(0, energy - 20)
    }
}