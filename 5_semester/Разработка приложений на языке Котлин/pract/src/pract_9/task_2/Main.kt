package pract_9.task_2

fun canRepair(device: ElectronicDevice): Boolean {
    return when (device) {
        is Computer -> {
            println("Мастерская может починить компьютер: ${device.brand} ${device.model}")
            true
        }
        is Phone -> {
            println("Мастерская может починить телефон: ${device.brand} ${device.model}")
            true
        }
        else -> {
            println("Мастерская НЕ может починить ${device::class.simpleName}: ${device.brand} ${device.model}")
            false
        }
    }
}


fun main() {
    val devices = listOf(
        Computer("HUAWEI", "Matebook D16", "Intel i5"),
        Phone("Samsung", "Galaxy S24", "Android"),
        Computer("Apple", "MacBook Pro", "M3"),
        Phone("Apple", "iPhone 17", "iOS"),
        Tablet("Apple", "iPad Air", 10.9),
        TV("Sony", "Bravia X90J", "4K"),
        Phone("Xiaomi", "Redmi Note 15", "Android"),
        Computer("HP", "Pavilion", "AMD Ryzen 5")
    )

    devices.forEach { device ->
        println("Устройство: $device")
        val canRepair = canRepair(device)
        println("Результат проверки: $canRepair")
        println("---")
    }
}