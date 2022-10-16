package patterns.behavioral.template;

class Editor extends Software {

    @Override
    void end() {
        System.out.println("Editor Finished!");
    }

    @Override
    void initialize() {
        System.out.println("Editor Initialized!");
    }

    @Override
    void start() {
        System.out.println("Editor Started!");
    }
}
