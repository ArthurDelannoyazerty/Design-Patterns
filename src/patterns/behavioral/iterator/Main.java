package patterns.behavioral.iterator;

public class Main {
    public static void main(String[] args) {
        LetterBag bag = new LetterBag();
        for(Iterator iter = bag.getIterator(); iter.hasNext();){
            String name = (String)iter.next();
            System.out.println("Name : " + name);
        }
    }
}
