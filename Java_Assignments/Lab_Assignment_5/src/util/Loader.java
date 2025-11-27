package util;

public class Loader implements Runnable {
    private volatile boolean running = true;
    private static final String[] ANIMATION = {"|", "/", "-", "\\"};

    @Override
    public void run() {
        int i = 0;
        System.out.print("Processing: ");
        
        while (running) {
            try {
                System.out.print("\rProcessing: " + ANIMATION[i % ANIMATION.length]);
                Thread.sleep(200);
                i++;
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
                break;
            }
        }
        
        System.out.print("\r");
    }

    public void stop() {
        running = false;
    }
}