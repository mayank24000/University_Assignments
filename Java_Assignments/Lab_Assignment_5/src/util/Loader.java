package util;

/**
 * Loader class implementing Runnable for multithreading
 * Simulates loading animation
 */
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
        
        System.out.print("\r"); // Clear the loading animation
    }

    public void stop() {
        running = false;
    }
}