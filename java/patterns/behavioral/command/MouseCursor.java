package patterns.behavioral.command;

class MouseCursor {
    private int x = 10;
    private int y = 10;

    public void move() {
        System.out.println("Old Position:" + x + ":" + y);
        x++;
        y++;
        System.out.println("New Position:" + x + ":" + y);

    }

    public void reset() {
        System.out.println("reset");
        x = 10;
        y = 10;
    }
}
