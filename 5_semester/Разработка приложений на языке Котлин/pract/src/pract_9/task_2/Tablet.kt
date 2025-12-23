package pract_9.task_2

class Tablet(brand: String, model: String, val screenSize: Double) : ElectronicDevice(brand, model) {
    override fun toString(): String {
        return "Планшет $brand $model (Экран: ${screenSize}\")"
    }
}