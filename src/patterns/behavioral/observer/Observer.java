package patterns.behavioral.observer;

abstract class Observer {
    protected MyValue subject;

    public abstract void update();
}
