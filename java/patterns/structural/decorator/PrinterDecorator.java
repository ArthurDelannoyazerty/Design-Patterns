package patterns.structural.decorator;

abstract public class PrinterDecorator implements Printer{

    protected Printer decoratedPrinter;

    public PrinterDecorator(Printer d){
        this.decoratedPrinter = d;
    }

    @Override
    public void print() {
        decoratedPrinter.print();
    }
}
