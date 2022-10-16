package patterns.creational.Singleton;

public class Singleton {
    private static Singleton instance = new Singleton("playground.Singleton.Singleton 1 unique");
    private String name;
    private Singleton(String name) {
        this.name = name;
    }
    public static Singleton getInstance() {
        return instance;
    }
    public String getName() {return name;}
    public void setName(String name) {
        this.name = name;
    }

}
