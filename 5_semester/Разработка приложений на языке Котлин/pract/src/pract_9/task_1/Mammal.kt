package pract_9.task_1

abstract class Mammal(name: String) : Animal(name) {
    override fun wayOfBirth() {
        println("$name - млекопитающее, рождает живых детенышей")
    }
}