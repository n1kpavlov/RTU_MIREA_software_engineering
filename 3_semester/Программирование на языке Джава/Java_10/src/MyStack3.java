import java.util.ArrayList;

public class MyStack3 extends ArrayList<Object> {

    public MyStack3() {
        super();
    }

    public MyStack3(MyStack3 other) {
        for (Object obj : other) {
            if (obj instanceof ArrayList) {
                ArrayList<?> list = (ArrayList<?>) obj;
                ArrayList<Object> newList = new ArrayList<>(list.size());
                for (Object item : list) {
                    newList.add(item);
                }
                add(newList);
            } else {
                add(obj);
            }
        }
    }

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
