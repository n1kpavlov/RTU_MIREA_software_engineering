import java.util.ArrayList;
import java.util.List;

public class Main {
    // Задание 1: Метод удаления дубликатов из ArrayList
    public static <T> List<T> removeDuplicates(List<T> list) {
        List<T> newList = new ArrayList<>();
        for (T element : list) {
            if (!newList.contains(element)) {
                newList.add(element);
            }
        }
        return newList;
    }

    // Задание 2: Метод линейного поиска элемента в массиве
    public static <T> int linearSearch(T[] array, T elementToFind) {
        for (int i = 0; i < array.length; i++) {
            if (array[i].equals(elementToFind)) {
                return i;
            }
        }
        return -1;
    }

    // Задание 3: Метод поиска наибольшего элемента в массиве
    public static <T extends Comparable<T>> T findLargest(T[] array) {
        if (array.length == 0) {
            return null;
        }
        T largest = array[0];
        for (int i = 1; i < array.length; i++) {
            if (array[i].compareTo(largest) > 0) {
                largest = array[i];
            }
        }
        return largest;
    }

    // Задание 4: Метод поиска наибольшего элемента в двумерном массиве
    public static <T extends Comparable<T>> T findLargest(T[][] array) {
        if (array.length == 0) {
            return null;
        }
        T largest = array[0][0];
        for (int i = 0; i < array.length; i++) {
            for (int j = 0; j < array[i].length; j++) {
                if (array[i][j].compareTo(largest) > 0) {
                    largest = array[i][j];
                }
            }
        }
        return largest;
    }

    public static void main(String[] args) {
        // Задание 1: Удаление дубликатов из ArrayList
        List<Integer> listWithDuplicates = new ArrayList<>(List.of(1, 2, 2, 3, 4, 4, 5));
        List<Integer> listWithoutDuplicates = removeDuplicates(listWithDuplicates);
        System.out.println("Список без дубликатов: " + listWithoutDuplicates);

        // Задание 2: Линейный поиск элемента в массиве
        Integer[] array = {1, 5, 3, 7, 9};
        Integer elementToFind = 7;
        int position = linearSearch(array, elementToFind);
        if (position != -1) {
            System.out.println("Элемент " + elementToFind + " найден на позиции " + position);
        } else {
            System.out.println("Элемент " + elementToFind + " не найден");
        }

        // Задание 3: Поиск наибольшего элемента в массиве с помощью compareTo()
        Circle[] circles = {new Circle(5), new Circle(3), new Circle(8)};
        Circle largestCircle = findLargest(circles);
        System.out.println("Наибольший круг: " + largestCircle);

        // Задание 4: Поиск наибольшего элемента в двумерном массиве с помощью compareTo()
        Circle[][] circles2D = {{new Circle(5), new Circle(3)}, {new Circle(8), new Circle(2)}};
        Circle largestCircle2D = findLargest(circles2D);
        System.out.println("Наибольший круг в двумерном массиве: " + largestCircle2D);
    }

}