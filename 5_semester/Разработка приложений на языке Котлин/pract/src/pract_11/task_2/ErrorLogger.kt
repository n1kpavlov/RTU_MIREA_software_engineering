package pract_11.task_2

class ErrorLogger<T> {
    fun logError(error: T) {
        when (error) {
            is String -> println("String error: $error")
            is Number -> println("Numeric error: $error")
            else -> println("Unknown error type")
        }
    }
}

fun <T> ErrorLogger<T>.logAndSend(error: T) {
    logError(error)
    println("Отправка ошибки на сервер: $error")
}