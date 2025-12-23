package pract_9.task_1

class GoldFish : Fish("Золотая рыбка"), Swimming {
    override fun move() {
        swim()
    }

    override fun swim() {
        println("Золотая рыбка плавает медленно")
        energy = maxOf(0, energy - 10)
    }
}