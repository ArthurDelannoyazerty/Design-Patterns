package patterns.structural.bridge;

public class Circle extends Shape {
    private int x, y, radius;

    public Circle(int x, int y, int radius, Printer draw) {
        super(draw);
        this.x = x;
        this.y = y;
        this.radius = radius;
    }

    public void draw() {
        print.print(radius, x, y);
    }
}
