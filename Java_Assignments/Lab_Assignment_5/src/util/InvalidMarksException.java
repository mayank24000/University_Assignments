package util;

/**
 * Custom exception for invalid marks
 */
public class InvalidMarksException extends Exception {
    
    public InvalidMarksException() {
        super("Invalid marks entered!");
    }

    public InvalidMarksException(String message) {
        super(message);
    }

    public InvalidMarksException(String message, Throwable cause) {
        super(message, cause);
    }
}