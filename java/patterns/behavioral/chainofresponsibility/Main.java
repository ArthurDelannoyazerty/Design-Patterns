package patterns.behavioral.chainofresponsibility;

public class Main {
    private static Logger getChainOfLoggers(){
        Logger emailLogger = new EmailLogger();
        Logger fileLogger = new FileLogger();
        Logger consoleLogger = new ConsoleLogger();

        emailLogger.setNextLogger(fileLogger);
        fileLogger.setNextLogger(consoleLogger);

        return emailLogger;
    }
    public static void main(String[] args) {
        Logger loggerChain = getChainOfLoggers();
        loggerChain.logMessage("Null pointer");
        loggerChain.logMessage("Array Index Out of Bound");
        loggerChain.logMessage("Illegal Parameters");
    }
}
