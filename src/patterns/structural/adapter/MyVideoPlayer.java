package patterns.structural.adapter;

public class MyVideoPlayer implements VideoPlayer {
    @Override
    public void playVideo(String fileName) {
        System.out.println("Playing. Name : " + fileName);
    }
}
