public class Main {
    public static void main(String[] args) {
        ChatMediator mediator = new ChatMediator();

        User user1 = new User(mediator, "User 1");
        User user2 = new User(mediator, "User 2");
        User user3 = new User(mediator, "User 3");

        mediator.addUser(user1);
        mediator.addUser(user2);
        mediator.addUser(user3);

        user1.sendMessage("Hello everyone!");
        user2.sendMessage("Hi User 1!");
        user3.sendMessage("Hello from User 3!");
    }
}