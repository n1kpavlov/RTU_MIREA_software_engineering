import java.util.InputMismatchException;
import java.util.Scanner;

public class Months {
    public static boolean isLeapYear(int year) {
        return ((year % 4 == 0) && (year % 100 != 0)) || (year % 400 == 0);
    }

    public static void main(String[] args) {
        String[] months = {"январь", "февраль", "март", "апрель", "май",
                "июнь", "июль", "август", "сентябрь", "октябрь", "ноябрь", "декабрь"};
        int[] days = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
        Scanner scanner = new Scanner(System.in);
        int number;
        while (true) {
            try {
                System.out.print("Введите номер месяца (от 1 до 12): ");
                number = scanner.nextInt();
                if (number < 1 || number > 12) {
                    throw new ArrayIndexOutOfBoundsException("Недопустимое число");
                }
                break;
            } catch (InputMismatchException e) {
                System.out.println("Ошибка: Введите целое число.");
                scanner.nextLine();

            } catch (ArrayIndexOutOfBoundsException exception) {
                System.out.println(exception.getMessage());
            }
        }
        int year = 0;
        if (number == 2) {
            try {
                System.out.print("Введите год: ");
                year = scanner.nextInt();
            } catch (InputMismatchException e) {
                System.out.println("Ошибка: Введите целое число.");
                scanner.nextLine();
            }
        }

        System.out.println("Месяц: " + months[number - 1]);
        if (number == 2) {
            System.out.println("Количество дней: " + (isLeapYear(year) ? 29 : 28));
        } else {
            System.out.println("Количество дней: " + days[number - 1]);
        }
        scanner.close();
    }
}