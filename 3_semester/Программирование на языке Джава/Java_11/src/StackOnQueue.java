import java.util.LinkedList;
import java.util.Queue;

public class StackOnQueue <T>{

    private Queue<T> queue;

    public StackOnQueue() {
        queue = new LinkedList<>();
    }

    public void push(T x) {
        queue.offer(x);
        for (int i = 0; i < queue.size() - 1; i++) {
            queue.offer(queue.poll());
        }
    }

    public T pop() {
        if (empty()) {
            throw new java.util.NoSuchElementException("Stack is empty");
        }
        return queue.poll();
    }

    public T top() {
        if (empty()) {
            throw new java.util.NoSuchElementException("Stack is empty");
        }
        return queue.peek();
    }

    public boolean empty() {
        return queue.isEmpty();
    }

    @Override
    public String toString() {
        return queue.toString();
    }
}
