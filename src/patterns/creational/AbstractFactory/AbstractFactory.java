package patterns.creational.AbstractFactory;

public abstract class AbstractFactory {
    abstract Printer getPrinter(String type);
    abstract Shape getShape(String shape);
}
