import java.util.Scanner;

public class Test {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        try {
            System.out.println("Введите стороны треугольника:");
            System.out.print("Сторона 1: ");
            double side1 = scanner.nextDouble();
            System.out.print("Сторона 2: ");
            double side2 = scanner.nextDouble();
            System.out.print("Сторона 3: ");
            double side3 = scanner.nextDouble();
            scanner.nextLine();
            System.out.print("Введите цвет треугольника: ");
            String color = scanner.nextLine();
            System.out.print("Заливка (true/false): ");
            boolean filled = scanner.nextBoolean();

            Triangle triangle = new Triangle(side1, side2, side3, color, filled);
            System.out.println("Созданный треугольник:");
            System.out.println(triangle);
        } catch (IllegalTriangleException e) {
            System.out.println(e.getMessage());
        }

        Circle circle1 = new Circle(5, "Красный", true);
        Circle circle2 = new Circle(3, "Синий", false);
        Rectangle rectangle = new Rectangle(8, 12, "Черный", true);
        System.out.println("Наибольший круг: " + GeometricObject.max(circle1, circle2));
        System.out.println("Наибольшая фигура: " + GeometricObject.max(circle1, rectangle));

        scanner.close();

        GeometricObject[] array = new GeometricObject[5];
        try {
            array[0] =  new Triangle(4, 3, 5, "White", true);
        } catch (IllegalTriangleException e) {
            System.out.println(e.getMessage());
        }
        array[1] = new Circle(5, "Red", true);
        array[2] = new Rectangle(23, 43, "Black", false);
        array[3] = new Square(4, "Blue", false);
        array[4] = new Square(7, "Green", true);
        for (int i = 0; i < 5; i++) {
            System.out.println("Object " + (i + 1) +
                    ": area = " + array[i].getArea());
            if (array[i].isFilled()) {
                array[i].howToColor();
            }
        }
    }
}