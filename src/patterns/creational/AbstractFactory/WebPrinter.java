package patterns.creational.AbstractFactory;

public class WebPrinter implements Printer{
    @Override
    public void print() {
        System.out.println("Web");
    }
}