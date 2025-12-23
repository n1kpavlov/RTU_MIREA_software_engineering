package pract_9.task_2

class Computer(brand: String, model: String, val processor: String) : ElectronicDevice(brand, model) {
    override fun toString(): String {
        return "Компьютер $brand $model (Процессор: $processor)"
    }
}