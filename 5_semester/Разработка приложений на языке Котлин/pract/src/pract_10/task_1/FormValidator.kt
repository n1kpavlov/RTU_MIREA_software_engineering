package pract_10.task_1

import java.time.LocalDate
import java.time.format.DateTimeFormatter
import java.time.format.DateTimeParseException


class FormValidator {
    fun validateName(name: String) {
        if (name.length < 2 || name.length > 20) {
            throw Exception("Имя должно содержать от 2 до 20 символов")
        }

        if (!name[0].isUpperCase()) {
            throw Exception("Первая буква имени должна быть заглавной")
        }
    }

    fun validateBirthDate(birthDate: String) {
        try {
            val formatter = DateTimeFormatter.ofPattern("dd.MM.yyyy")
            val date = LocalDate.parse(birthDate, formatter)
            val minDate = LocalDate.of(1900, 1, 1)
            val currentDate = LocalDate.now()

            if (date.isBefore(minDate)) {
                throw Exception("Дата рождения не может быть раньше 01.01.1900")
            }

            if (date.isAfter(currentDate)) {
                throw Exception("Дата рождения не может быть в будущем")
            }
        } catch (e: DateTimeParseException) {
            throw Exception("Неверный формат даты. Используйте формат dd.MM.yyyy")
        }
    }

    fun validateGender(gender: String) {
        try {
            Gender.valueOf(gender.uppercase())
        } catch (e: IllegalArgumentException) {
            throw Exception("Пол должен быть 'MALE' или 'FEMALE'")
        }
    }

    fun validateWeight(weight: String) {
        try {
            val weightValue = weight.toDouble()
            if (weightValue <= 0) {
                throw Exception("Вес должен быть положительным числом")
            }
        } catch (e: NumberFormatException) {
            throw Exception("Вес должен быть числом")
        }
    }

    fun validateForm(formData: FormData): Boolean {
        val errors = mutableListOf<String>()

        try {
            validateName(formData.name)
        } catch (e: Exception) {
            errors.add("Ошибка в имени: ${e.message}")
        }

        try {
            validateBirthDate(formData.birthDate)
        } catch (e: Exception) {
            errors.add("Ошибка в дате рождения: ${e.message}")
        }

        try {
            validateGender(formData.gender)
        } catch (e: Exception) {
            errors.add("Ошибка в поле: ${e.message}")
        }

        try {
            validateWeight(formData.weight)
        } catch (e: Exception) {
            errors.add("Ошибка в весе: ${e.message}")
        }

        if (errors.isNotEmpty()) {
            println("Обнаружены ошибки валидации:")
            errors.forEach { println("- $it") }
            return false
        }

        println("Анкета прошла валидацию успешно!")
        return true
    }
}