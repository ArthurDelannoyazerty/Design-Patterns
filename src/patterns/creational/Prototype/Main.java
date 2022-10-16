package patterns.creational.Prototype;

public class Main {

    public static void main(String[] args) {
        ShapePrototype.loadCache();

        Shape clonedShape = (Shape) ShapePrototype.getShape("1");
        System.out.println("Shape : " + clonedShape.getType());

        Shape clonedShape2 = (Shape) ShapePrototype.getShape("2");
        System.out.println("Shape : " + clonedShape2.getType());

        Shape clonedShape3 = (Shape) ShapePrototype.getShape("3");
        System.out.println("Shape : " + clonedShape3.getType());
    }
}
