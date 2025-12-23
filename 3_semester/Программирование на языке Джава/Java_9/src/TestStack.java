import java.util.Scanner;

public class TestStack {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        GenericStack<String> stack = new GenericStack<>();
        GenericStack2<String> stack2 = new GenericStack2<>();

        System.out.println("Введите 5 строк:");
        for (int i = 0; i < 5; i++) {
            String s = scanner.nextLine();
            stack.push(s);
            stack2.add(s);
        }

        System.out.println("Строки в обратном порядке:");
        while (!stack.isEmpty()) {
            System.out.println(stack.pop());
            System.out.println(stack2.pop());
        }
    }
}
