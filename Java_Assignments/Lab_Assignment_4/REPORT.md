# Assignment Report: Student Record Management System

**Subject:** Java Programming Lab  
**Assignment:** File Handling and Collections Framework 
**Submitted By:** Mayank Rawat  

---

## 1. Objective
The objective of this assignment was to develop a **Student Record Management System** capable of persistent storage. The system utilizes Java's **File Handling** capabilities (`io` package) to read and write data to a text file and employs the **Collections Framework** to manage, sort, and traverse student records efficiently in memory.

## 2. System Architecture & Implementation
The solution is modularized into five classes to ensure separation of concerns:

### A. Class Hierarchy
1.  **`Student.java`**: A POJO (Plain Old Java Object) class representing the student entity with fields: `Roll No`, `Name`, `Email`, `Course`, and `Marks`. It includes a `toCSV()` helper method for file writing.
2.  **`MarksComparator.java`**: Implements the `Comparator<Student>` interface to define custom sorting logic based on marks in descending order.
3.  **`FileUtil.java`**: Handles all low-level file operations:
    *   Uses `BufferedReader` and `BufferedWriter` for reading/writing `students.txt`.
    *   Demonstrates `RandomAccessFile` for random byte reading.
    *   Uses the `File` class to display file attributes (size, path, permissions).
4.  **`StudentManager.java`**: Acts as the controller. It utilizes an `ArrayList` to store data in memory and an `Iterator` to traverse and display records.
5.  **`StudentManagementSystem.java`**: The main entry point containing the menu-driven interface (CLI).

## 3. Key Concepts Applied

### File Handling (Persistence)
*   **Data Persistence:** Records are stored in `students.txt` in CSV (Comma Separated Values) format.
*   **IO Streams:** `BufferedReader` is used for efficient character reading, and `BufferedWriter` is used for writing to ensure data is not lost upon program exit.
*   **Random Access:** `RandomAccessFile` is implemented to demonstrate non-sequential file reading capabilities.

### Collections Framework
*   **List Interface:** `ArrayList<Student>` is used to hold the student objects dynamically.
*   **Iterator:** Used to safely traverse the list for displaying and deleting records.
*   **Sorting:** `Collections.sort()` is paired with the `MarksComparator` to sort students by marks.

## 4. Code Highlights

**Sorting Logic (Comparator):**
```java
public class MarksComparator implements Comparator<Student> {
    @Override
    public int compare(Student s1, Student s2) {
        // Sort Descending
        if (s1.getMarks() < s2.getMarks()) return 1;
        if (s1.getMarks() > s2.getMarks()) return -1;
        return 0;
    }
}