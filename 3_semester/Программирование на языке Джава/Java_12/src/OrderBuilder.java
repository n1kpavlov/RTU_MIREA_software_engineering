public class OrderBuilder {
    private Order order = new Order();

    public OrderBuilder setMainDish(String mainDish) {
        order.setMainDish(mainDish);
        return this;
    }

    public OrderBuilder setGarnish(String garnish) {
        order.setGarnish(garnish);
        return this;
    }

    public OrderBuilder setDrink(String drink) {
        order.setDrink(drink);
        return this;
    }

    public OrderBuilder setDessert(String dessert) {
        order.setDessert(dessert);
        return this;
    }

    public Order build() {
        return order;
    }
}
