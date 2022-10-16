package patterns.structural.decorator;

public class Main {

    public static void main(String[] args) {
        Printer plasticPrinter = new PlasticPrinter();
        Printer paperPrinter = new PaperPrinter();
        Printer plastic3DPrinter = new Printer3D(new PlasticPrinter());
        Printer paper3DPrinter = new Printer3D(new PaperPrinter());

        plasticPrinter.print();
        paperPrinter.print();
        plastic3DPrinter.print();
        paper3DPrinter.print();
    }
}
