package patterns.behavioral.chainofresponsibility;

class ConsoleLogger extends Logger {
    @Override
    protected void log(String message) {
        System.out.println("Console::Logger: " + message);
    }
}
