package patterns.structural.decorator;

public class PaperPrinter implements Printer{
    @Override
    public void print() {
        System.out.println("Paper Printer");
    }
}
