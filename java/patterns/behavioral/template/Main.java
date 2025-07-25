package patterns.behavioral.template;

public class Main {
    public static void main(String[] args) {
        Software s1 = new Browser();
        s1.play();
        s1 = new Editor();
        s1.play();
    }
}