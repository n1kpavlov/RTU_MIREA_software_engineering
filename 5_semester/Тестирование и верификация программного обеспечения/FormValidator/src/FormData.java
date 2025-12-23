public class FormData {
    private String name;
    private String birthDate;
    private String gender;
    private String weight;

    public FormData(String name, String birthDate, String gender, String weight) {
        this.name = name;
        this.birthDate = birthDate;
        this.gender = gender;
        this.weight = weight;
    }

    public String getName() { return name; }
    public String getBirthDate() { return birthDate; }
    public String getGender() { return gender; }
    public String getWeight() { return weight; }

    @Override
    public String toString() {
        return String.format("FormData{name='%s', birthDate='%s', gender='%s', weight='%s'}",
                name, birthDate, gender, weight);
    }
}