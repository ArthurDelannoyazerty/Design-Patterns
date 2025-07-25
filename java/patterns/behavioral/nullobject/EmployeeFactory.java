package patterns.behavioral.nullobject;

class EmployeeFactory {
    public static final String[] names = {"Rob", "Joe", "Jack"};

    public static AbstractEmployee getCustomer(String name) {
        for (int i = 0; i < names.length; i++) {
            if (names[i].equalsIgnoreCase(name)) {
                return new Programmer(name);
            }
        }
        return new NullCustomer();
    }
}
