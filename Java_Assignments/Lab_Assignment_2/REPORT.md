# Student Management System - Project Report

- **Title:** Student Management System using OOP Concepts
- **Name:** `Mayank Rawat`
- **Roll No:** `240183005`
- **Course** : ``BSc Computer Science``
- **Semester** : ``3rd Semester``
- **Assignment** : ``Lab Assignment 2``

---

## Problem Statement
> To develop a comprehensive Student Management System that demonstrates core Object-Oriented Programming principles including inheritance, polymorphism, abstraction, and interfaces, all organized within a proper package structure.

---

## Implementation Details

### 1. Class Hierarchy

| Class/Interface  | Type             | Purpose                                                    |
|------------------|------------------|------------------------------------------------------------|
| **Person**       | Abstract Class   | A base class with common fields like `name` and `email`.   |
| **Student**      | Final Class      | Extends `Person` with fields: `rollNo`, `course`, `marks`, `grade`. |
| **RecordActions**| Interface        | Defines the contract for CRUD (Create, Read, Update, Delete) operations. |
| **StudentManager**| Concrete Class   | Implements the `RecordActions` interface for student management. |

### 2. Key Features Implemented

#### OOP Concepts Demonstrated
- **Inheritance:** `Student` extends `Person`, inheriting its properties and methods.
- **Abstraction:** The `Person` class is `abstract` with an `abstract displayInfo()` method, forcing subclasses to provide an implementation.
- **Polymorphism:**
  - **Method Overriding:** `displayInfo()` is overridden in the `Student` class.
  - **Method Overloading:** Multiple variants of the `displayInfo()` method are created.
  - **Runtime Polymorphism:** A `Person` reference is used to hold a `Student` object, demonstrating dynamic method dispatch.
- **Encapsulation:** All data fields are `private`, with access provided through public `getters` and `setters`.
- **Interface Implementation:** The `StudentManager` class `implements` the `RecordActions` interface.

#### Data Structures Used
- **`List<Student>`:** Provides sequential storage to maintain the order of student records.
- **`Map<Integer, Student>`:** Used for efficient O(1) average-time lookups by roll number.
- **`HashMap` & `ArrayList`:** The chosen concrete implementations for their performance characteristics.

### 3. Core Functionalities

| Feature          | Description                      | Time Complexity |
|------------------|----------------------------------|-----------------|
| **Add Student**    | Prevents duplicate roll numbers. | O(1)            |
| **Delete Student** | Removes a record by roll number. | O(1) for map    |
| **Update Student** | Modifies an existing record.     | O(1)            |
| **Search Student** | Finds a student by roll number.  | O(1)            |
| **View All**       | Displays all student records.    | O(n)            |
| **Sort Records**   | Orders students by marks or name.| O(n log n)      |

### 4. Special Features
- **Duplicate Prevention:** Validates that each student has a unique roll number.
- **Automatic Grade Calculation:** Assigns a grade based on marks (A: ≥90, B: ≥80, C: ≥70, D: ≥60, F: <60).
- **Statistics:** Calculates and displays average class marks and the total number of students.
- **Sorting Options:** Allows sorting by marks (descending) or by name (alphabetical).
- **Research Area Support:** A special overloaded display method for M.Tech students to show their research area.

---

## Sample Output

```text
Student Info:
Roll No: 101
Name: Ankit
Email: ankit@mail.com
Course: B.Tech
Grade: B

[Note] Overloaded display method for M.Tech student:
Student Info:
Roll No: 102
Name: Riya
Email: riya@mail.com
Course: M.Tech
Research Area: AI

This is a final method in a final class.
Finalize method called before object is garbage collected.
```

---

## Testing Scenarios

✅ **Positive Test Cases:**
- Successfully add multiple unique students.
- Search for existing students by roll number.
- Update information for an existing student.
- Sort the student list by both marks and name.
- Correctly display polymorphic behavior for different student types.

✅ **Negative Test Cases:**
- Prevent the addition of a student with a duplicate roll number.
- Handle searches for non-existent students gracefully.
- Validate that update/delete operations on non-existent students fail correctly.

---

## Technical Highlights
- **Package Organization:** A modular design using `model` and `service` packages.
- **Error Handling:** Graceful handling of invalid user inputs and operations.
- **Memory Efficiency:** A dual data structure approach (`List` + `Map`) for balanced performance.
- **Code Reusability:** Achieved through the use of an abstract base class and an interface.
- **Type Safety:** Strong typing enforced with Java generics (`List<Student>`, `Map<Integer, Student>`).

---

## Learning Outcomes Achieved

| # | Outcome                           | Implementation Detail                               |
|---|-----------------------------------|-----------------------------------------------------|
| 1 | **Inheritance & Method Overriding** | `Student` class extends `Person` and overrides `displayInfo()`. |
| 2 | **Abstract Classes & Interfaces**   | `Person` is an abstract class; `RecordActions` is an interface. |
| 3 | **Package Organization**            | Code is structured into `model` and `service` packages.     |
| 4 | **Polymorphism**                    | Both static (overloading) and dynamic (overriding) polymorphism demonstrated. |

---

## Compilation & Execution

```bash
# To compile all .java files from the root directory
javac model/*.java service/*.java Main.java

# To run the application
java Main
```

---

## Future Enhancements
- **Persistence:** Add file I/O or database connectivity (JDBC) to save and load student data.
- **GUI:** Implement a graphical user interface using JavaFX or Swing.
- **Validation:** Enhance input validation for fields like email format and marks range.
- **Reporting:** Generate reports in formats like PDF or Excel.
- **Authentication:** Add a user login system with different access levels.

---

## Conclusion

The Student Management System successfully demonstrates all required Object-Oriented Programming concepts while providing practical, real-world functionality. The modular design, organized into packages, ensures the code is maintainable, scalable, and reusable. This project showcases professional Java development practices, including efficient data structure usage, proper abstraction, and clean code principles.

### Performance Metrics
- **Space Complexity:** O(n), where `n` is the number of students.
- **Search Efficiency:** O(1) on average, using `HashMap`.
- **Sort Performance:** O(n log n), using `Collections.sort()`.