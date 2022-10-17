package patterns.creational.abstractfactory;

public class Main {

    public static void main(String[] args) {
        ShapeFactory shapeFactory = new ShapeFactory();

        //get an object of Circle and call its draw method.
        Shape shape1 = shapeFactory.getShape("CIRCLE");
        shape1.draw();

        //get an object of Rectangle and call its draw method.
        Shape shape2 = shapeFactory.getShape("RECTANGLE");
        shape2.draw();

        //get an object of Square and call its draw method.
        Shape shape3 = shapeFactory.getShape("SQUARE");
        shape3.draw();

        //get printer factory
        AbstractFactory printerFactory = FactoryProducer.getFactory("printer");

        Printer printer1 = printerFactory.getPrinter("Paper");
        printer1.print();

        Printer printer2 = printerFactory.getPrinter("Web");
        printer2.print();

        Printer printer3 = printerFactory.getPrinter("Screen");
        printer3.print();


//        Inside Circle::draw() method.
//        Inside Rectangle::draw() method.
//        Inside Square::draw() method.
//        Paper
//        Web
//        Screen

    }
}
