package service;

import model.Student;
import util.Loader;
import util.StudentNotFoundException;
import java.io.*;
import java.util.*;

public class StudentManager implements RecordActions {
    private List<Student> studentList;
    private Map<Integer, Student> studentMap;
    private static final String FILE_NAME = "students.txt";

    public StudentManager() {
        studentList = new ArrayList<>();
        studentMap = new HashMap<>();
    }

    @Override
    public void addStudent(Student student) throws Exception {
        // Show loading animation
        System.out.println("\nAdding student...");
        Loader loader = new Loader();
        Thread loaderThread = new Thread(loader);
        loaderThread.start();
        
        try {
            // Check for duplicate roll number
            if (studentMap.containsKey(student.getRollNo())) {
                loader.stop();
                loaderThread.join();
                throw new Exception("Student with Roll No " + student.getRollNo() + " already exists!");
            }

            // Simulate processing time
            Thread.sleep(1000);
            
            studentList.add(student);
            studentMap.put(student.getRollNo(), student);
            
            loader.stop();
            loaderThread.join();
            
            System.out.println("\n✓ Student added successfully!");
        } catch (InterruptedException e) {
            loader.stop();
            throw new Exception("Error while adding student: " + e.getMessage());
        }
    }

    @Override
    public void deleteStudent(String name) throws StudentNotFoundException {
        System.out.println("\nDeleting student...");
        Loader loader = new Loader();
        Thread loaderThread = new Thread(loader);
        loaderThread.start();
        
        try {
            Thread.sleep(800);
            
            boolean found = false;
            Iterator<Student> iterator = studentList.iterator();
            
            while (iterator.hasNext()) {
                Student student = iterator.next();
                if (student.getName().equalsIgnoreCase(name)) {
                    studentMap.remove(student.getRollNo());
                    iterator.remove();
                    found = true;
                    break;
                }
            }
            
            loader.stop();
            loaderThread.join();
            
            if (!found) {
                throw new StudentNotFoundException("Student with name '" + name + "' not found!");
            }
            
            System.out.println("\n✓ Student record deleted successfully!");
        } catch (InterruptedException e) {
            loader.stop();
            System.err.println("Error during deletion: " + e.getMessage());
        }
    }

    @Override
    public void updateStudent(int rollNo, Student updatedStudent) throws StudentNotFoundException {
        if (!studentMap.containsKey(rollNo)) {
            throw new StudentNotFoundException("Student with Roll No " + rollNo + " not found!");
        }
        
        Student existingStudent = studentMap.get(rollNo);
        
        // Update the student details
        existingStudent.setName(updatedStudent.getName());
        existingStudent.setEmail(updatedStudent.getEmail());
        existingStudent.setCourse(updatedStudent.getCourse());
        existingStudent.setMarks(updatedStudent.getMarks());
        
        System.out.println("\n✓ Student updated successfully!");
    }

    @Override
    public Student searchStudent(String name) throws StudentNotFoundException {
        System.out.println("\nSearching...");
        Loader loader = new Loader();
        Thread loaderThread = new Thread(loader);
        loaderThread.start();
        
        try {
            Thread.sleep(800);
            
            for (Student student : studentList) {
                if (student.getName().equalsIgnoreCase(name)) {
                    loader.stop();
                    loaderThread.join();
                    return student;
                }
            }
            
            loader.stop();
            loaderThread.join();
            
            throw new StudentNotFoundException("Student with name '" + name + "' not found!");
        } catch (InterruptedException e) {
            loader.stop();
            throw new StudentNotFoundException("Error during search: " + e.getMessage());
        }
    }

    @Override
    public void viewAllStudents() {
        if (studentList.isEmpty()) {
            System.out.println("\nNo student records available.");
            return;
        }
        
        System.out.println("\n========== All Student Records ==========");
        Iterator<Student> iterator = studentList.iterator();
        int count = 1;
        
        while (iterator.hasNext()) {
            System.out.println("\n--- Student " + count + " ---");
            iterator.next().displayDetails();
            count++;
        }
        System.out.println("\n=========================================");
    }

    @Override
    public void sortByMarks() {
        System.out.println("\nSorting students by marks...");
        Loader loader = new Loader();
        Thread loaderThread = new Thread(loader);
        loaderThread.start();
        
        try {
            Thread.sleep(1000);
            
            // Sort using Comparator (descending order)
            Collections.sort(studentList, new Comparator<Student>() {
                @Override
                public int compare(Student s1, Student s2) {
                    return Double.compare(s2.getMarks(), s1.getMarks());
                }
            });
            
            loader.stop();
            loaderThread.join();
            
            System.out.println("\n✓ Students sorted by marks (descending)!");
            System.out.println("\n========== Sorted Student List by Marks ==========");
            
            Iterator<Student> iterator = studentList.iterator();
            int rank = 1;
            
            while (iterator.hasNext()) {
                System.out.println("\n--- Rank " + rank + " ---");
                iterator.next().displayDetails();
                rank++;
            }
            System.out.println("\n==================================================");
        } catch (InterruptedException e) {
            loader.stop();
            System.err.println("Error during sorting: " + e.getMessage());
        }
    }

    @Override
    public void saveToFile() throws Exception {
        System.out.println("\nSaving records to file...");
        Loader loader = new Loader();
        Thread loaderThread = new Thread(loader);
        loaderThread.start();
        
        BufferedWriter writer = null;
        try {
            Thread.sleep(1000);
            
            writer = new BufferedWriter(new FileWriter(FILE_NAME));
            
            for (Student student : studentList) {
                writer.write(student.toFileString());
                writer.newLine();
            }
            
            loader.stop();
            loaderThread.join();
            
            System.out.println("\n✓ Records saved successfully to " + FILE_NAME);
        } catch (IOException e) {
            loader.stop();
            throw new Exception("Error saving to file: " + e.getMessage());
        } finally {
            if (writer != null) {
                try {
                    writer.close();
                } catch (IOException e) {
                    System.err.println("Error closing file: " + e.getMessage());
                }
            }
        }
    }

    @Override
    public void loadFromFile() throws Exception {
        File file = new File(FILE_NAME);
        
        if (!file.exists()) {
            System.out.println("No existing records found. Starting fresh.");
            return;
        }
        
        System.out.println("\nLoading records from file...");
        Loader loader = new Loader();
        Thread loaderThread = new Thread(loader);
        loaderThread.start();
        
        BufferedReader reader = null;
        try {
            Thread.sleep(1500);
            
            reader = new BufferedReader(new FileReader(FILE_NAME));
            String line;
            int count = 0;
            
            studentList.clear();
            studentMap.clear();
            
            while ((line = reader.readLine()) != null) {
                if (!line.trim().isEmpty()) {
                    Student student = Student.fromFileString(line);
                    studentList.add(student);
                    studentMap.put(student.getRollNo(), student);
                    count++;
                }
            }
            
            loader.stop();
            loaderThread.join();
            
            System.out.println("\n✓ Loaded " + count + " student record(s) successfully!");
        } catch (IOException e) {
            loader.stop();
            throw new Exception("Error loading from file: " + e.getMessage());
        } finally {
            if (reader != null) {
                try {
                    reader.close();
                } catch (IOException e) {
                    System.err.println("Error closing file: " + e.getMessage());
                }
            }
        }
    }

    public int getStudentCount() {
        return studentList.size();
    }
}