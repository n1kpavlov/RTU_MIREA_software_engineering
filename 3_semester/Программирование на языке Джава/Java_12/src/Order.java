public class Order {
    private String mainDish;
    private String garnish;
    private String drink;
    private String dessert;

    public void setMainDish(String mainDish) {
        this.mainDish = mainDish;
    }

    public void setGarnish(String garnish) {
        this.garnish = garnish;
    }

    public void setDrink(String drink) {
        this.drink = drink;
    }

    public void setDessert(String dessert) {
        this.dessert = dessert;
    }

    @Override
    public String toString() {
        return "Order{" +
                "mainDish='" + mainDish + '\'' +
                ", garnish='" + garnish + '\'' +
                ", drink='" + drink + '\'' +
                ", dessert='" + dessert + '\'' +
                '}';
    }
}
