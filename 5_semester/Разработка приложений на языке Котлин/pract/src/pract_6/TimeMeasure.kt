package pract_6

class TimeMeasure {
    private var hours: Int = 0
    private var minutes: Int = 0
    private var seconds: Int = 0


    constructor(hours: Int, minutes: Int, seconds: Int) {
        validateTime(hours, minutes, seconds)
        this.hours = hours
        this.minutes = minutes
        this.seconds = seconds
    }


    constructor(hours: Int, minutes: Int): this(hours, minutes, 0)
    constructor(hours: Int): this(hours, 0, 0)


    private fun validateTime(hours: Int, minutes: Int, seconds: Int) {
        if (hours < 0 || hours > 23) {
            throw IllegalArgumentException("Часы должны быть в диапазоне 0-23")
        }
        if (minutes < 0 || minutes > 59) {
            throw IllegalArgumentException("Минуты должны быть в диапазоне 0-59")
        }
        if (seconds < 0 || seconds > 59) {
            throw IllegalArgumentException("Секунды должны быть в диапазоне 0-59")
        }
    }


    fun display24HourFormat() {
        println(String.format("%02d:%02d:%02d", hours, minutes, seconds))
    }


    fun display12HourFormat() {
        val period = if (hours < 12) "am" else "pm"
        val newHours = when {
            hours == 0 -> 12
            hours > 12 -> hours - 12
            else -> hours
        }
        println(String.format("%02d:%02d:%02d %s", newHours, minutes, seconds, period))
    }


    fun addTime(hours: Int, minutes: Int, seconds: Int) {
        if (hours < 0 || minutes < 0 || seconds < 0) {
            throw IllegalArgumentException("Добавляемое время не может быть отрицательным")
        }
        var totalSeconds = this.seconds + seconds
        var totalMinutes = this.minutes + minutes + totalSeconds / 60
        var totalHours = this.hours + hours + totalMinutes / 60
        this.seconds = totalSeconds % 60
        this.minutes = totalMinutes % 60
        this.hours = totalHours % 24
    }

}