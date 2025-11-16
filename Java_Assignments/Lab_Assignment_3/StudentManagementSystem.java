import java.util.*;
import java.util.concurrent.*;

public class StudentManagementSystem {
    
    public static void main(String[] args) {
        System.out.println("=== Student Management System ===\n");
        
        try {
            // Direct input approach for assignment requirement
            Scanner scanner = new Scanner(System.in);
            
            // Using wrapper classes with autoboxing
            System.out.print("Enter Roll No (Integer): ");
            Integer rollNo = Integer.valueOf(scanner.nextLine());
            
            System.out.print("Enter Name: ");
            String name = scanner.nextLine();
            
            System.out.print("Enter Email: ");
            String email = scanner.nextLine();
            
            System.out.print("Enter Course: ");
            String course = scanner.nextLine();
            
            System.out.print("Enter Marks: ");
            Double marks = Double.valueOf(scanner.nextLine());
            
            // Input validation
            validateStudentData(rollNo, name, email, course, marks);
            
            // Create and process student
            Student student = new Student(rollNo, name, email, course, marks);
            
            // Multithreading for loading simulation
            LoadingTask loadingTask = new LoadingTask();
            Thread loadingThread = new Thread(loadingTask);
            loadingThread.start();
            loadingThread.join();
            
            // Calculate and set grade
            student.setGrade(calculateGrade(marks));
            
            // Display student information
            displayStudent(student);
            
            System.out.println("Program execution completed.");
            scanner.close();
            
        } catch (NumberFormatException e) {
            System.err.println("Error: Invalid number format - " + e.getMessage());
        } catch (InvalidDataException e) {
            System.err.println("Validation Error: " + e.getMessage());
        } catch (InterruptedException e) {
            System.err.println("Thread Error: " + e.getMessage());
            Thread.currentThread().interrupt();
        } catch (Exception e) {
            System.err.println("Unexpected Error: " + e.getMessage());
        } finally {
            System.out.println("\n=== System Shutdown ===");
        }
    }
    
    // Validation method
    private static void validateStudentData(Integer rollNo, String name, String email, 
                                           String course, Double marks) throws InvalidDataException {
        try {
            if (rollNo == null || rollNo <= 0) {
                throw new InvalidDataException("Roll number must be positive!");
            }
            if (name == null || name.trim().isEmpty()) {
                throw new InvalidDataException("Name cannot be empty!");
            }
            if (email == null || !email.matches("^[A-Za-z0-9+_.-]+@(.+)$")) {
                throw new InvalidDataException("Invalid email format!");
            }
            if (course == null || course.trim().isEmpty()) {
                throw new InvalidDataException("Course cannot be empty!");
            }
            if (marks == null || marks < 0 || marks > 100) {
                throw new InvalidDataException("Marks must be between 0 and 100!");
            }
        } catch (Exception e) {
            throw new InvalidDataException("Validation failed: " + e.getMessage());
        }
    }
    
    // Grade calculation
    private static String calculateGrade(Double marks) {
        if (marks >= 90) return "A+";
        else if (marks >= 80) return "A";
        else if (marks >= 70) return "B";
        else if (marks >= 60) return "C";
        else if (marks >= 50) return "D";
        else if (marks >= 40) return "E";
        else return "F";
    }
    
    // Display method
    private static void displayStudent(Student student) {
        try {
            if (student == null) {
                throw new StudentNotFoundException("No student data to display!");
            }
            System.out.println("\n" + student);
        } catch (StudentNotFoundException e) {
            System.err.println("Display Error: " + e.getMessage());
        } finally {
            System.out.println("Display operation completed.\n");
        }
    }
    
    // Student class
    static class Student {
        private Integer rollNo;
        private String name;
        private String email;
        private String course;
        private Double marks;
        private String grade;
        
        public Student(Integer rollNo, String name, String email, String course, Double marks) {
            this.rollNo = rollNo;
            this.name = name;
            this.email = email;
            this.course = course;
            this.marks = marks;
        }
        
        public void setGrade(String grade) {
            this.grade = grade;
        }
        
        @Override
        public String toString() {
            return "Roll No: " + rollNo + "\n" +
                   "Name: " + name + "\n" +
                   "Email: " + email + "\n" +
                   "Course: " + course + "\n" +
                   "Marks: " + marks + "\n" +
                   "Grade: " + grade;
        }
    }
    
    // Loading task for multithreading
    static class LoadingTask implements Runnable {
        @Override
        public void run() {
            try {
                System.out.print("Loading");
                for (int i = 0; i < 5; i++) {
                    Thread.sleep(200);
                    System.out.print(".");
                }
                System.out.println();
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
        }
    }
    
    // Custom Exceptions
    static class StudentNotFoundException extends Exception {
        public StudentNotFoundException(String message) {
            super(message);
        }
    }
    
    static class InvalidDataException extends Exception {
        public InvalidDataException(String message) {
            super(message);
        }
    }
}