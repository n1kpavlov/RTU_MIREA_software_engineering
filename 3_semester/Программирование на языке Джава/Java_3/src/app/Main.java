package app;

import vehicle.Car;
import vehicle.ElectricCar;

public class Main {
    public static void main(String[] args) {

        Car bmw = new Car();
        ElectricCar tesla = new ElectricCar();

        bmw.setEngineType("Pistol");
        bmw.setInsuranseNumber(777);
        bmw.setOwnerName("Artem");

        tesla.setBatteryCapacity(1000);
        tesla.setInsuranseNumber(666);
        tesla.setOwnerName("Anton");

        System.out.println(bmw.getEngineType() + " " + bmw.getInsuranseNumber() + " " + bmw.getOwnerName());
        System.out.println(tesla.getEngineType() + " " + tesla.getInsuranseNumber() + " " + tesla.getOwnerName());
    }
}