package patterns.creational.abstractfactory;

public abstract class AbstractFactory implements Shape, Printer {
    abstract Printer getPrinter(String type);
    abstract Shape getShape(String shape);
}
