package bikeproject;

public class Bike implements BikeParts{
    private String handleBars;
    private String frame;
    private String tyres;
    private String seatType;
    private int NumGears;

    public Bike(){}

    public Bike(String handleBars, String frame, String tyres, String seatType, int numGears) {
        this.handleBars = handleBars;
        this.frame = frame;
        this.tyres = tyres;
        this.seatType = seatType;
        this.NumGears = numGears;
    }

    protected void printDescription() {
        System.out.println("\n" + this.make + "\n" + "This bike has " + this.handleBars + " handlebars on a " + this.frame + " frame with " + this.NumGears + " gears." + "\nIt has a " + this.seatType + " seat with " + this.tyres + " tyres.");
    }

    @Override
    public String getHandleBars() {
        return handleBars;
    }

    @Override
    public void setHandleBars(String handleBars) {
        this.handleBars = handleBars;
    }

    @Override
    public String getFrame() {
        return frame;
    }

    @Override
    public void setFrame(String frame) {
        this.frame = frame;
    }

    @Override
    public String getTyres() {
        return tyres;
    }

    @Override
    public void setTyres(String tyres) {
        this.tyres = tyres;
    }

    @Override
    public String getSeatType() {
        return seatType;
    }

    @Override
    public void setSeatType(String seatType) {
        this.seatType = seatType;
    }

    @Override
    public int getNumGears() {
        return NumGears;
    }

    @Override
    public void setNumGears(int numGears) {
        NumGears = numGears;
    }
}
