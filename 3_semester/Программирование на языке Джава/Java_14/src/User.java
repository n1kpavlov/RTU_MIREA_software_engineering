class User {
    private String name;
    private Mediator mediator;

    public User(Mediator mediator, String name) {
        this.mediator = mediator;
        this.name = name;
    }

    public void sendMessage(String message) {
        System.out.println(this.name + ": Sending message - " + message);
        mediator.sendMessage(message, this);
    }

    public void receiveMessage(String message, User sender) {
        System.out.println(this.name + ": Received message from " + sender.getName() + ": " + message);
    }

    public String getName() {
        return name;
    }
}