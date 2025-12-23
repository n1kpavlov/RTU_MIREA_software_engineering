package pract_11.task_2

fun main() {
    val stringLogger = ErrorLogger<String>()
    stringLogger.logError("File not found")

    val numberLogger = ErrorLogger<Number>()
    numberLogger.logError(404)

    val unknownLogger = ErrorLogger<Any>()
    unknownLogger.logError(listOf(1, 2, 3))

    stringLogger.logAndSend("Network timeout")

    val logger = FileErrorLogger<String>("errors.txt")
    logger.logError("Запись ошибки в файл")
}