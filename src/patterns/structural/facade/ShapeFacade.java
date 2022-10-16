package patterns.structural.facade;

public class ShapeFacade {

    private Shape circle = new Circle();
    private Shape rectangle = new Rectangle();
    private Shape square = new Square();

    public void drawCircle() {
        circle.draw();
    }
    public void drawRectangle() {
        rectangle.draw();
    }
    public void drawSquare() {
        square.draw();
    }
}
