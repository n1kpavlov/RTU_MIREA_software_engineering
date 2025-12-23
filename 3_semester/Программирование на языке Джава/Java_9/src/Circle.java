public class Circle implements Comparable<Circle> {
    int radius;

    public Circle(int radius) {
        this.radius = radius;
    }

    @Override
    public int compareTo(Circle other) {
        return Integer.compare(this.radius, other.radius);
    }

    @Override
    public String toString() {
        return "Circle{" +
                "radius=" + radius +
                '}';
    }
}