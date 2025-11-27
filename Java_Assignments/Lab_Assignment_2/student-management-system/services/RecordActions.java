package services;

import model.Student;
public interface RecordActions {
    boolean addStudent(Student student);
    boolean deleteStudent(int rollNo);
    boolean updateStudent(int rollNo, Student updatedStudent);
    Student searchStudent(int rollNo);
    void viewAllStudents();
    void sortStudentsByMarks();
    void sortStudentsByName();
}