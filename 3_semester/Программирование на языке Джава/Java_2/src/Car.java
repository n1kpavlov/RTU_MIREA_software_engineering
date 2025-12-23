import java.time.Year;
public class Car {

    String model;
    String license;
    String color;
    int year;

    Car() {
        this("M5", "A777AA 77", "black", 2024);
    }
    Car(String model, String license, String color, int year) {
        Set_model(model);
        Set_license(license);
        Set_color(color);
        Set_year(year);
    }
    Car(String model, int year) {
        this(model, "not specified", "not specified", year);
    }

    void To_String() {
        System.out.printf("Model: %s \t\tLicense: %s \t\tColor: %s \t\tYear: %d\n", Get_model(), Get_license(), Get_color(), Get_year());
    }
    void Set_model(String model) {
        this.model = model;
    }
    void Set_license(String license) {
        this.license = license;
    }
    void Set_color(String color) {
        this.color = color;
    }
    void Set_year(int year) {
        this.year = year;
    }
    String Get_model() {
        return model;
    }
    String Get_license() {
        return license;
    }
    String Get_color() {
        return color;
    }
    int Get_year() {
        return year;
    }
    int age() {
        return Year.now().getValue() - Get_year();
    }
}
