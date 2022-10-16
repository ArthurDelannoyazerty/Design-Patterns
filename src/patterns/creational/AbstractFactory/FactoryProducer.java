package patterns.creational.AbstractFactory;

public class FactoryProducer {
    public static AbstractFactory getFactory(String choice){
        if(choice.equalsIgnoreCase("SHAPE")){
            return new ShapeFactory();
        } else if(choice.equalsIgnoreCase("Printer")){
            return new PrinterFactory();
        }
        return null;
    }
}
