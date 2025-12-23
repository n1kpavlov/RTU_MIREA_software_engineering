package app;

import vehicles.Car;
import vehicles.ElectricCar;
import vehicles.Vehicle;

public class TestCar {
    public static void main(String[] args) {

        Car toyota = new Car("Toyota Camry", "ABC-123", "Red", 2020, "John Doe", "123456789");
        ElectricCar tesla = new ElectricCar("Tesla Model S", "DEF-456", "Black", 2022, "Jane Doe", "987654321", 85);

        toyota.setColor("Black");
        tesla.setBatteryCapacity(100);

        System.out.println("Car: " + toyota);
        System.out.println("Electric Car: " + tesla);

        Vehicle vehicle1 = toyota;
        Vehicle vehicle2 = tesla;

        System.out.println("Vehicle Type: " + vehicle1.vehicleType());
        System.out.println("Vehicle Type: " + vehicle2.vehicleType());
    }
}
