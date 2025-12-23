import java.util.ArrayList;

public class MyStack2 extends ArrayList<Object> {

    public Object peek() {
        if (isEmpty()) {
            throw new IllegalStateException("Стек пуст");
        }
        return get(size() - 1);
    }

    public Object pop() {
        if (isEmpty()) {
            throw new IllegalStateException("Стек пуст");
        }
        return remove(size() - 1);
    }

    public int getSize() {
        return size();
    }

    @Override
    public String toString() {
        return "Стек: " + super.toString();
    }
}
