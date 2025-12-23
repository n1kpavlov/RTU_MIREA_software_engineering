package pract_9.task_1

abstract class Bird(name: String) : Animal(name) {
    override fun wayOfBirth() {
        println("$name - птица, откладывает яйца")
    }
}