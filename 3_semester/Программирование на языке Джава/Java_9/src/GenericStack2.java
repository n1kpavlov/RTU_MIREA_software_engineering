import java.util.ArrayList;

public class GenericStack2<E> extends ArrayList<E> {

    public E peek() {
        if (isEmpty()) {
            throw new IllegalStateException("Стек пуст");
        }
        return get(size() - 1);
    }

    public E pop() {
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
        return "стек: " + super.toString();
    }
}
