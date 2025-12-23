package pract_9.task_1

class Dolphin : Mammal("Дельфин"), Swimming {
    override fun move() {
        swim()
    }

    override fun swim() {
        println("Дельфин плавает быстро")
        energy = maxOf(0, energy - 20)
    }
}