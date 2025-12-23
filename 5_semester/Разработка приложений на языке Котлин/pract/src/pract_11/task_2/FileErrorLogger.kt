package pract_11.task_2
import java.io.File

class FileErrorLogger<T>(val logFile: String) {
    fun logError(error: T) {
        val message = when (error) {
            is String -> "String error: $error"
            is Number -> "Numeric error: $error"
            else -> "Unknown error type"
        }
        println(message)
        File(logFile).appendText("$message\n")
    }
}