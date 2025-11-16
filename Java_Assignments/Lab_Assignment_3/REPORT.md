**Course:**  Bsc. (H) Cybersecurity
**Subject:** Fundamentals of java 
**Student Name:** Mayank Rawat  
**Student ID:** 2401830005

# Student Management System

A simple yet well-structured Java console application that demonstrates student data handling, validation, grade calculation, and multithreading. This program showcases core Java concepts such as OOP, wrapper classes, exception handling, and concurrency—all within a single file for easier academic submission and understanding.

---

## 📌 Features

### 🔹 1. Input Handling
- Accepts student details: Roll No, Name, Email, Course, and Marks.
- Uses `Scanner` for reading console input.
- Wrapper classes (`Integer`, `Double`) with autoboxing for seamless type conversion.

### 🔹 2. Data Validation
The program validates:
- Roll number must be positive.
- Name & course cannot be empty.
- Email must be in valid format.
- Marks must be between 0–100.

Invalid inputs are handled with a custom exception: `InvalidDataException`.

### 🔹 3. Student Management
- A `Student` class stores all details.
- Grade is assigned based on marks:
  - A+, A, B, C, D, E, F

### 🔹 4. Multithreading
A loading animation is generated using:
```java
LoadingTask implements Runnable
This simulates processing time and gives the application a more realistic feel.

🔹 5. Exception Handling
The program includes:

InvalidDataException

StudentNotFoundException

Handling for:

Number format errors

Thread interruptions

Unexpected runtime issues

🔹 6. Clean Output Display
The final student details are printed in a structured and readable format using the overridden toString() method.

🛠️ Technologies Used
Java (Core Java)

Object-Oriented Programming

Wrapper Classes

Custom Exceptions

Multithreading

Input/Output Handling

🚀 How to Run the Program
Save the file as:

Copy code
StudentManagementSystem.java
Compile the program:

nginx
Copy code
javac StudentManagementSystem.java
Run it:

nginx
Copy code
java StudentManagementSystem
Provide the requested inputs when prompted.

📥 Example Input
mathematica
Copy code
Enter Roll No (Integer): 101
Enter Name: John Doe
Enter Email: john@example.com
Enter Course: Java Programming
Enter Marks: 87
📤 Example Output
yaml
Copy code
Loading.....

Roll No: 101
Name: John Doe
Email: john@example.com
Course: Java Programming
Marks: 87.0
Grade: A

Display operation completed.

Program execution completed.

=== System Shutdown ===
📚 File Structure
python
Copy code
StudentManagementSystem.java
│
├── main()                         # Entry point of the program
├── validateStudentData()          # Input validation
├── calculateGrade()               # Grade logic
├── displayStudent()               # Structured student output
│
├── Student class                  # Model class for student data
│
├── LoadingTask (Runnable)         # Multithreading simulation
│
└── Custom Exceptions:
       ├── InvalidDataException
       └── StudentNotFoundException
🎯 Learning Outcomes
This project demonstrates:

How to structure programs using OOP.

Practical use of wrapper classes.

Exception handling with custom exceptions.

Implementing multithreading in Java.

Clean separation of logic using helper methods.

Good coding practices in Java.

