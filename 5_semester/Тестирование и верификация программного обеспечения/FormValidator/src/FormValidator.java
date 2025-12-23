import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.time.format.DateTimeParseException;
import java.util.ArrayList;
import java.util.List;

public class FormValidator {

    public void validateName(String name) throws FormValidationException {
        if (name == null || name.length() < 2 || name.length() > 20) {
            throw new FormValidationException("Имя должно содержать от 2 до 20 символов");
        }

        if (!Character.isUpperCase(name.charAt(0))) {
            throw new FormValidationException("Первая буква имени должна быть заглавной");
        }

        for (char c : name.toCharArray()) {
            if (!Character.isLetter(c) && c != ' ' && c != '-') {
                throw new FormValidationException("Имя может содержать только буквы, пробелы и дефисы");
            }
        }
    }

    public void validateBirthDate(String birthDate) throws FormValidationException {
        try {
            DateTimeFormatter formatter = DateTimeFormatter.ofPattern("dd.MM.yyyy");
            LocalDate date = LocalDate.parse(birthDate, formatter);
            LocalDate minDate = LocalDate.of(1900, 1, 1);
            LocalDate currentDate = LocalDate.now();

            if (date.isBefore(minDate)) {
                throw new FormValidationException("Дата рождения не может быть раньше 01.01.1900");
            }

            if (date.isAfter(currentDate)) {
                throw new FormValidationException("Дата рождения не может быть в будущем");
            }
        } catch (DateTimeParseException e) {
            throw new FormValidationException("Неверный формат даты. Используйте формат dd.MM.yyyy");
        }
    }

    public void validateGender(String gender) throws FormValidationException {
        try {
            Gender.valueOf(gender.toUpperCase());
        } catch (IllegalArgumentException e) {
            throw new FormValidationException("Пол должен быть 'MALE' или 'FEMALE'");
        }
    }

    public void validateWeight(String weight) throws FormValidationException {
        try {
            double weightValue = Double.parseDouble(weight);
            if (weightValue <= 0) {
                throw new FormValidationException("Вес должен быть положительным числом");
            }
        } catch (NumberFormatException e) {
            throw new FormValidationException("Вес должен быть числом");
        }
    }

    public boolean validateForm(FormData formData) {
        List<String> errors = new ArrayList<>();

        try {
            validateName(formData.getName());
        } catch (FormValidationException e) {
            errors.add("Ошибка в имени: " + e.getMessage());
        }

        try {
            validateBirthDate(formData.getBirthDate());
        } catch (FormValidationException e) {
            errors.add("Ошибка в дате рождения: " + e.getMessage());
        }

        try {
            validateGender(formData.getGender());
        } catch (FormValidationException e) {
            errors.add("Ошибка в поле: " + e.getMessage());
        }

        try {
            validateWeight(formData.getWeight());
        } catch (FormValidationException e) {
            errors.add("Ошибка в весе: " + e.getMessage());
        }

        if (!errors.isEmpty()) {
            System.out.println("Обнаружены ошибки валидации:");
            for (String error : errors) {
                System.out.println("- " + error);
            }
            return false;
        }

        System.out.println("Анкета прошла валидацию успешно!");
        return true;
    }
}