package pract_9.task_2

class Phone(brand: String, model: String, val os: String) : ElectronicDevice(brand, model) {
    override fun toString(): String {
        return "Телефон $brand $model (ОС: $os)"
    }
}