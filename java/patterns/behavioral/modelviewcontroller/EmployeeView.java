package patterns.behavioral.modelviewcontroller;

class EmployeeView {
    public void printEmployeeDetails(String name, String no) {
        System.out.println("Employee: ");
        System.out.println("Name: " + name);
        System.out.println("ID: " + no);
    }
}
