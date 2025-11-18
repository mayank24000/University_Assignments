import java.io.Serializable;

public class Student implements Serializable {
    private int rollNo;
    private String name;
    private String email;
    private String course;
    private double marks;

    public Student(int rollNo, String name, String email, String course, double marks) {
        this.rollNo = rollNo;
        this.name = name;
        this.email = email;
        this.course = course;
        this.marks = marks;
    }

    // Getters
    public int getRollNo() { return rollNo; }
    public String getName() { return name; }
    public String getEmail() { return email; }
    public String getCourse() { return course; }
    public double getMarks() { return marks; }

    // Helper to format data for File Writing (CSV format)
    public String toCSV() {
        return rollNo + "," + name + "," + email + "," + course + "," + marks;
    }

    @Override
    public String toString() {
        return "Roll No: " + rollNo + "\n" +
               "Name: " + name + "\n" +
               "Email: " + email + "\n" +
               "Course: " + course + "\n" +
               "Marks: " + marks + "\n";
    }
}