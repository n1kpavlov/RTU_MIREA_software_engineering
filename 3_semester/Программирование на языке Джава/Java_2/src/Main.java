import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        Car BMW = new Car();
        Car Toyota = new Car("Camry", 2008);
        Car Lada = new Car("2108", "В777ОР 76", "black", 2013);

        BMW.To_String();
        Toyota.To_String();
        Lada.To_String();
        System.out.print("Age of Lada: " + Lada.age());
    }
}