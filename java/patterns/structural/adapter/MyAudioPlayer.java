package patterns.structural.adapter;

public class MyAudioPlayer implements AudioPlayer{
    @Override
    public void playAudio(String fileName) {
        System.out.println("Playing. Name : " + fileName);
    }
}

