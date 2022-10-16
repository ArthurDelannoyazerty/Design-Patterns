package patterns.behavioral.chainofresponsibility;

class EmailLogger extends Logger {
    @Override
    protected void log(String message) {
        System.out.println("EMail::Logger: " + message);
    }
}
