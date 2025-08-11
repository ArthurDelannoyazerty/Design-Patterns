package patterns.behavioral.visitor;

public class Main {

    public static void main(String[] args) {
        TreeNode computer = new TreeNode("Java2s.com");
        computer.accept(new ConsoleVisitor());
        computer.accept(new EmailVisitor());
    }
}