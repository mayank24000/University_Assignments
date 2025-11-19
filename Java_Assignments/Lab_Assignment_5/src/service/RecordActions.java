package service;

import model.Student;
import util.StudentNotFoundException;

/**
 * Interface defining contract for student record operations
 * Demonstrates interface usage
 */
public interface RecordActions {
    void addStudent(Student student) throws Exception;
    void deleteStudent(String name) throws StudentNotFoundException;
    void updateStudent(int rollNo, Student updatedStudent) throws StudentNotFoundException;
    Student searchStudent(String name) throws StudentNotFoundException;
    void viewAllStudents();
    void sortByMarks();
    void saveToFile() throws Exception;
    void loadFromFile() throws Exception;
}