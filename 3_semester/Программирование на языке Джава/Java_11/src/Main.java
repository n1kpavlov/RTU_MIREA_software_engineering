 public class Main {
    public static void main(String[] args) {
        StackOnQueue stack = new StackOnQueue();
        stack.push(1);
        stack.push("second");
        System.out.println("Стек: " + stack); // Стек: [second, 1]
        System.out.println("Верхний элемент: " + stack.top()); // Верхний элемент: second
        System.out.println("Удаленный элемент: " + stack.pop()); // Удаленный элемент: second
        System.out.println("Стек пуст? " + stack.empty()); // Стек пуст? false
        System.out.println("Стек после удаления: " + stack); // Стек после удаления: [1]+
    }
}