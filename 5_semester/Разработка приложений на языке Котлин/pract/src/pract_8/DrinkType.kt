enum class DrinkType(
    private val volume: Int,
    val temperature: Int
) {
    COFFEE(250, 85) {
        override fun getFormattedName(): String = "Кофе"
    },
    TEA(200, 75) {
        override fun getFormattedName(): String = "Чай"
    },
    JUICE(300, 5) {
        override fun getFormattedName(): String = "Сок"
    },
    WATER(500, 10) {
        override fun getFormattedName(): String = "Вода"
    };

    abstract fun getFormattedName(): String

    fun getVolume(): Int = this.volume

    fun isHot(): Boolean = this.temperature > 60

    fun getDrinkInfo(): String {
        val heatStatus = if (isHot()) "горячий" else "холодный"
        return "${getFormattedName()} - ${getVolume()} мл, $heatStatus ($temperature°C)"
    }
}