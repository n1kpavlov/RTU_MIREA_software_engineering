package pract_9.task_2

class TV(brand: String, model: String, val resolution: String) : ElectronicDevice(brand, model) {
    override fun toString(): String {
        return "Телевизор $brand $model (Разрешение: $resolution)"
    }
}