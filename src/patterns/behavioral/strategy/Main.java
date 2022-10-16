package patterns.behavioral.strategy;

public class Main {
    public static void main(String[] args) {
        MathContext context = new MathContext(new MathAdd());
        System.out.println("10 + 5 = " + context.execute(10, 5));

        context = new MathContext(new MathSubstract());
        System.out.println("10 - 5 = " + context.execute(10, 5));

        context = new MathContext(new MathMultiply());
        System.out.println("10 * 5 = " + context.execute(10, 5));
    }
}