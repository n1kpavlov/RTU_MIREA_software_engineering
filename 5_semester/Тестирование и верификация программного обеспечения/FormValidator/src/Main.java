import java.util.List;


public class Main {
    public static void main(String[] args) {
        FormValidator validator = new FormValidator();

        List<FormData> testForms = List.of(
                new FormData("Иван", "15.05.1990", "MALE", "75.5"),
                new FormData("иван", "15.05.1990", "MALE", "75.5"),
                new FormData("И", "15.05.1990", "MALE", "75.5"),
                new FormData("Иван", "15.05.1800", "MALE", "75.5"),
                new FormData("Иван", "15.05.1990", "UNKNOWN", "75.5"),
                new FormData("Иван", "15.05.1990", "MALE", "-5"),
                new FormData("Иван", "15.05.1990", "MALE", "abc")
        );

        for (int i = 0; i < testForms.size(); i++) {
            FormData formData = testForms.get(i);
            System.out.println("\nТест анкеты " + (i + 1) + ":");
            System.out.println("Данные: " + formData);
            validator.validateForm(formData);
        }
    }
}