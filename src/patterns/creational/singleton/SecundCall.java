package patterns.creational.singleton;

class SecundCall {

    SecundCall(){init();}

    private void init(){
        Singleton s = Singleton.getInstance();
        System.out.println(s.getName());
    }


}
