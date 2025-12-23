import java.util.Scanner;

public class TestMyStack {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        MyStack stack = new MyStack();
        MyStack2 stack2 = new MyStack2();
        MyStack3 stack3 = new MyStack3();

        System.out.println("Введите 5 строк:");
        for (int i = 0; i < 5; i++) {
            String s = scanner.nextLine();
            stack.push(s);
            stack2.add(s);
            stack3.add(s);
        }

        System.out.println("Строки в обратном порядке:");
        while (!stack.isEmpty()) {
            System.out.println(stack.pop());
            System.out.println(stack2.pop());
            System.out.println(stack3.pop());
        }
    }
}
