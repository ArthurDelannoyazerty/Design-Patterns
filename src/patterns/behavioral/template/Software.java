package patterns.behavioral.template;

abstract class Software {
    abstract void initialize();

    abstract void start();

    abstract void end();

    //template method
    public final void play() {
        initialize();
        start();
        end();
    }
}
