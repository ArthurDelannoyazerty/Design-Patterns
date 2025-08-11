package patterns.structural.composite;

import java.util.ArrayList;
import java.util.List;

public class Employee {

    private String name;
    private String title;
    private List<Employee> subordinates;

    public Employee(String name,String title) {
        this.name = name;
        this.title = title;
        subordinates = new ArrayList<Employee>();
    }

    public void add(Employee e) {
        subordinates.add(e);
    }

    public void remove(Employee e) {
        subordinates.remove(e);
    }

    public List<Employee> getSubordinates(){
        return subordinates;
    }

    public String toString(){
        return "Employee :[ Name : "+ name
                +", dept : "+ title +subordinates +" ]";
    }
}
