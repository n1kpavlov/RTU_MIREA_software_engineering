package app;

import vehicles.Car;
import vehicles.ElectricCar;
import vehicles.Vehicle;

public class TestCar {
    public static void main(String[] args) {

        Car toyota = new Car("Toyota Camry", "ABC-123", "Red", 2020, "John Doe", "123456789");
        ElectricCar tesla = new ElectricCar("Tesla Model S", "DEF-456", "Black", 2022, "Jane Doe", "987654321", 85);

        toyota.setColor("Black");
        toyota.setOwnerName("Jack Doe");
        tesla.setInsuranceNumber("999999999");
        System.out.println(tesla.getBatteryCapacity());

        System.out.println("Car: " + toyota);
        System.out.println("Electric Car: " + tesla);

        System.out.println("Vehicle Type: " + toyota.vehicleType());
        System.out.println("Vehicle Type: " + tesla.vehicleType());
    }
}
