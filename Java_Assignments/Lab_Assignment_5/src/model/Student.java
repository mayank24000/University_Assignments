package model;

import java.util.Scanner;

/**
 * Student class extending Person
 * Represents a student with additional attributes
 */
public class Student extends Person {
    private int rollNo;
    private String course;
    private double marks;
    private String grade;

    // Default constructor
    public Student() {
        super();
    }

    // Parameterized constructor
    public Student(int rollNo, String name, String email, String course, double marks) {
        super(name, email);
        this.rollNo = rollNo;
        this.course = course;
        this.marks = marks;
        this.grade = calculateGrade();
    }

    // Input student details
    public void inputDetails(Scanner scanner) throws Exception {
        System.out.print("Enter Roll No: ");
        this.rollNo = scanner.nextInt();
        scanner.nextLine(); // Consume newline

        System.out.print("Enter Name: ");
        this.name = scanner.nextLine().trim();
        
        if (this.name.isEmpty()) {
            throw new Exception("Name cannot be empty!");
        }

        System.out.print("Enter Email: ");
        this.email = scanner.nextLine().trim();
        
        if (this.email.isEmpty() || !this.email.contains("@")) {
            throw new Exception("Invalid email format!");
        }

        System.out.print("Enter Course: ");
        this.course = scanner.nextLine().trim();
        
        if (this.course.isEmpty()) {
            throw new Exception("Course cannot be empty!");
        }

        System.out.print("Enter Marks: ");
        this.marks = scanner.nextDouble();
        
        if (this.marks < 0 || this.marks > 100) {
            throw new Exception("Marks must be between 0 and 100!");
        }

        this.grade = calculateGrade();
    }

    // Calculate grade based on marks
    public String calculateGrade() {
        if (marks >= 90) {
            return "A+";
        } else if (marks >= 80) {
            return "A";
        } else if (marks >= 70) {
            return "B+";
        } else if (marks >= 60) {
            return "B";
        } else if (marks >= 50) {
            return "C";
        } else if (marks >= 40) {
            return "D";
        } else {
            return "F";
        }
    }

    // Display student details
    public void displayDetails() {
        System.out.println("Roll No: " + rollNo);
        System.out.println("Name: " + name);
        System.out.println("Email: " + email);
        System.out.println("Course: " + course);
        System.out.println("Marks: " + marks);
        System.out.println("Grade: " + grade);
    }

    @Override
    public void displayInfo() {
        displayDetails();
    }

    // Convert student to file format
    public String toFileString() {
        return rollNo + "," + name + "," + email + "," + course + "," + marks + "," + grade;
    }

    // Create student from file string
    public static Student fromFileString(String line) throws Exception {
        String[] parts = line.split(",");
        if (parts.length != 6) {
            throw new Exception("Invalid data format in file");
        }
        
        int rollNo = Integer.parseInt(parts[0].trim());
        String name = parts[1].trim();
        String email = parts[2].trim();
        String course = parts[3].trim();
        double marks = Double.parseDouble(parts[4].trim());
        
        return new Student(rollNo, name, email, course, marks);
    }

    // Getters and Setters
    public int getRollNo() {
        return rollNo;
    }

    public void setRollNo(int rollNo) {
        this.rollNo = rollNo;
    }

    public String getCourse() {
        return course;
    }

    public void setCourse(String course) {
        this.course = course;
    }

    public double getMarks() {
        return marks;
    }

    public void setMarks(double marks) {
        this.marks = marks;
        this.grade = calculateGrade();
    }

    public String getGrade() {
        return grade;
    }

    @Override
    public String toString() {
        return "Student{" +
                "rollNo=" + rollNo +
                ", name='" + name + '\'' +
                ", email='" + email + '\'' +
                ", course='" + course + '\'' +
                ", marks=" + marks +
                ", grade='" + grade + '\'' +
                '}';
    }
}