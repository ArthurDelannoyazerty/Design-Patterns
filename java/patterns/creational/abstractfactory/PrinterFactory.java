package patterns.creational.abstractfactory;

public class PrinterFactory extends AbstractFactory{
    @Override
    Printer getPrinter(String type) {
        if(type == null){
            return null;
        }

        if(type.equalsIgnoreCase("paper")){
            return new PaperPrinter();
        } else if(type.equalsIgnoreCase("web")){
            return new WebPrinter();
        } else if(type.equalsIgnoreCase("Screen")){
            return new ScreenPrinter();
        }

        return null;
    }

    @Override
    Shape getShape(String shape) {
        return null;
    }
}
