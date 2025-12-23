package bikeproject;

public class RoadBike extends Bike implements RoadParts{
    private int tyreWidth;
    private int postHeight;

    public RoadBike() {
        this("drop", "racing", "tread less", "razor", 19, 20, 22);
    }

    public RoadBike(int postHeight) {
        this("drop", "racing", "tread less", "razor", 19, 20, postHeight);
    }

    public RoadBike(String handleBars, String frame, String tyres, String seatType, int numGears, int tyreWidth, int postHeight) {
        super(handleBars, frame, tyres, seatType, numGears);
        this.tyreWidth = tyreWidth;
        this.postHeight = postHeight;
    }

    public void printDescription() {
        super.printDescription();
        System.out.println("This Roadbike bike has " + this.tyreWidth + "mm tyres and a post height of " + this.postHeight + ".");
    }

    @Override
    public int getTyreWidth() {
        return tyreWidth;
    }

    public void setTyreWidth(int tyreWidth) {
        this.tyreWidth = tyreWidth;
    }

    @Override
    public int getPostHeight() {
        return postHeight;
    }

    public void setPostHeight(int postHeight) {
        this.postHeight = postHeight;
    }
}
