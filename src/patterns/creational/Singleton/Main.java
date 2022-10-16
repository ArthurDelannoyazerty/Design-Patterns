package patterns.creational.Singleton;

public class Main {

    public static void main(String[] args) {
        Singleton s = Singleton.getInstance();
        System.out.println(s.getName());
        s.setName("playground.Singleton.Singleton 2");
        System.out.println(s.getName());
        SecundCall secundCall = new SecundCall();
    }

}
