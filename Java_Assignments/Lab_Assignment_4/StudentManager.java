import java.util.*;

public class StudentManager {
    private List<Student> studentList;

    public StudentManager() {
        // Initialize list and load from file immediately
        this.studentList = FileUtil.readStudentsFromFile();
    }

    public void addStudent(Student s) {
        studentList.add(s);
        System.out.println("Student added successfully.");
    }

    // Requirement: Use Iterator to display student data
    public void viewAllStudents() {
        if (studentList.isEmpty()) {
            System.out.println("No records found.");
            return;
        }
        
        System.out.println("\n--- All Students ---");
        Iterator<Student> iterator = studentList.iterator();
        while (iterator.hasNext()) {
            System.out.println(iterator.next());
        }
    }

    public void searchByName(String name) {
        boolean found = false;
        for (Student s : studentList) {
            if (s.getName().equalsIgnoreCase(name)) {
                System.out.println("Student Found:\n" + s);
                found = true;
            }
        }
        if (!found) System.out.println("Student with name " + name + " not found.");
    }

    public void deleteByName(String name) {
        Iterator<Student> iterator = studentList.iterator();
        boolean removed = false;
        while (iterator.hasNext()) {
            Student s = iterator.next();
            if (s.getName().equalsIgnoreCase(name)) {
                iterator.remove();
                System.out.println("Student " + name + " deleted.");
                removed = true;
                break;
            }
        }
        if (!removed) System.out.println("Student not found.");
    }

    // Requirement: Sort students by marks using Comparator
    public void sortByMarks() {
        Collections.sort(studentList, new MarksComparator());
        System.out.println("\nSorted Student List by Marks (Highest First):");
        viewAllStudents();
    }

    public void saveAndExit() {
        FileUtil.writeStudentsToFile(studentList);
    }

    // Optional: Show technical details required by assignment
    public void showTechDetails() {
        FileUtil.displayFileAttributes();
        FileUtil.demonstrateRandomAccess();
    }
}