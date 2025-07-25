package patterns.structural.proxy;

public class Main {

    public static void main(String[] args) {
        Printer image = new ProxyPrinter("test");
        image.print();
    }
}
