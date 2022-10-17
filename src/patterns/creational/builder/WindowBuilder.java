package patterns.creational.builder;

public class WindowBuilder {

    public static MainWindow createWindow() {
        MainWindow window = new MainWindow();

        Menu menu = new Menu();
        window.setMenu(menu);

        ToolBar toolBar = new ToolBar();
        window.setToolBar(toolBar);

        return window;
    }
}
