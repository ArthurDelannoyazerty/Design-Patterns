package patterns.creational.AbstractFactory;

public class PaperPrinter implements Printer{
    @Override
    public void print() {
        System.out.println("Paper");
    }
}
