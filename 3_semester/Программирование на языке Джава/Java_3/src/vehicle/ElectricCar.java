package vehicle;

public class ElectricCar extends Car{

    private int BatteryCapacity;

    public ElectricCar() {
        EngineType = "Electric";
    }

    public int getBatteryCapacity() {
        return BatteryCapacity;
    }

    public void setBatteryCapacity(int batteryCapacity) {
        BatteryCapacity = batteryCapacity;
    }
}
