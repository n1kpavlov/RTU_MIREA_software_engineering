package pract_11.task_3

class Validator<T : Any> {
    fun validate(value: T): Boolean {
        return when (value) {
            is Number -> value.toDouble() > 0
            is String -> value.length > 5
            else -> throw IllegalArgumentException("Несоответствие типа")
        }
    }
}