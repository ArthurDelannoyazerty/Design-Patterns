package patterns.behavioral.chainofresponsibility;

class FileLogger extends Logger {
    @Override
    protected void log(String message) {
        System.out.println("File::Logger: " + message);
    }
}
