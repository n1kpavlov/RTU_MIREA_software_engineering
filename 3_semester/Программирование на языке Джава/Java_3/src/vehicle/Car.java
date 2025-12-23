package vehicle;

public class Car {

    private String OwnerName;
    private int InsuranseNumber;
    protected String EngineType;

    public String getOwnerName() {
        return OwnerName;
    }

    public void setOwnerName(String ownerName) {
        this.OwnerName = ownerName;
    }

    public int getInsuranseNumber() {
        return InsuranseNumber;
    }

    public void setInsuranseNumber(int insuranseNumber) {
        this.InsuranseNumber = insuranseNumber;
    }

    public String getEngineType() {
        return EngineType;
    }

    public void setEngineType(String engineType) {
        this.EngineType = engineType;
    }
}
