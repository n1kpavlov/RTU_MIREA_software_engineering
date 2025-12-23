package pract_9.task_1

abstract class Fish(name: String) : Animal(name) {
    override fun wayOfBirth() {
        println("$name - рыба, мечет икру")
    }
}