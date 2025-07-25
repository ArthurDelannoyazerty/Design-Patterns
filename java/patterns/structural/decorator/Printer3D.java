package patterns.structural.decorator;

public class Printer3D extends PrinterDecorator{
    public Printer3D(Printer decoratedPrinter) {
        super(decoratedPrinter);
    }

    @Override
    public void print(){
        System.out.print("3D.");
        decoratedPrinter.print();
    }
}
