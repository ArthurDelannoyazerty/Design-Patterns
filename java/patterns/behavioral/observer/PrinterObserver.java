package patterns.behavioral.observer;

class PrinterObserver extends Observer {
    public PrinterObserver(MyValue subject) {
        this.subject = subject;
        this.subject.attach(this);
    }

    @Override
    public void update() {
        System.out.println("Printer: " + subject.getState());
    }
}
