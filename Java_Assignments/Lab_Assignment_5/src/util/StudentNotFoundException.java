package util;

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