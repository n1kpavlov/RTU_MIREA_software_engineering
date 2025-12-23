package pract_10.task_1


fun main() {
    val validator = FormValidator()

    val testForms = listOf(
        FormData("Иван", "15.05.1990", "MALE", "75.5"),
        FormData("иван", "15.05.1990", "MALE", "75.5"),
        FormData("И", "15.05.1990", "MALE", "75.5"),
        FormData("Иван", "15.05.1800", "MALE", "75.5"),
        FormData("Иван", "15.05.1990", "UNKNOWN", "75.5"),
        FormData("Иван", "15.05.1990", "MALE", "-5"),
        FormData("Иван", "15.05.1990", "MALE", "abc")
    )

    testForms.forEachIndexed { index, formData ->
        println("\nТест анкеты ${index + 1}:")
        println("Данные: $formData")
        validator.validateForm(formData)
    }
}