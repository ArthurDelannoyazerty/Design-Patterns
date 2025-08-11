package patterns.behavioral.template;

class Browser extends Software {
    @Override
    void end() {
        System.out.println("Browser Finished!");
    }

    @Override
    void initialize() {
        System.out.println("Browser Initialized!.");
    }

    @Override
    void start() {
        System.out.println("Browser Started.");
    }
}
