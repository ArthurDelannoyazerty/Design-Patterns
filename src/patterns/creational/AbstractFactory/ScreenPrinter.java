package patterns.creational.AbstractFactory;

public class ScreenPrinter implements Printer{
    @Override
    public void print() {
        System.out.println("Screen");
    }
}