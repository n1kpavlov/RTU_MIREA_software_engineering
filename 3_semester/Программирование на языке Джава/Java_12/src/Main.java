public class Main {
    public static void main(String[] args) {

        // Заказ 1: Полный
        Order order1 = new OrderBuilder().setMainDish("Steak").setGarnish("Potatoes").setDrink("Juice").setDessert("Ice cream").build();
        System.out.println("Order 1: " + order1);

        // Заказ 2: Напиток и десерта
        Order order2 = new OrderBuilder().setDrink("Coffe").setDessert("Cake").build();
        System.out.println("Order 2: " + order2);

        //Заказ 3: Только основное блюдо и напиток
        Order order3 = new OrderBuilder().setMainDish("Pizza").setDrink("Cola").build();
        System.out.println("Order 3: " + order3);
    }
}