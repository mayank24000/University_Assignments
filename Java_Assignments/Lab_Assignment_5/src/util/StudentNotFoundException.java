package util;

/**
 * Custom exception for student not found scenarios
 * Demonstrates custom exception handling
 */
public class StudentNotFoundException extends Exception {
    
    public StudentNotFoundException() {
        super("Student not found!");
    }

    public StudentNotFoundException(String message) {
        super(message);
    }

    public StudentNotFoundException(String message, Throwable cause) {
        super(message, cause);
    }
}