# 🎓 Student Record Management System - Project Report

> **Project:** Capstone Assignment | **Language:** Java | **Version:** 1.0

## 📋 Executive Summary
A robust console-based Java application designed to manage student data. The system leverages **Object-Oriented Programming**, **Collection Frameworks**, and **File I/O** for persistence, ensuring data integrity and efficient retrieval.

---

## 🏗 System Architecture

### Package Structure
```
Lab_Assignment_5/
├── src/
│   ├── model/        # Data entities (Person, Student)
│   ├── service/      # Business logic (Manager, Interface)
│   ├── util/         # Helpers (Loader, Custom Exceptions)
│   └── Main.java     # Application entry point
└── students.txt      # Persistent data storage (CSV)
```

### Class Hierarchy
- **Abstraction:** `Person` (Abstract Base Class) → `Student` (Concrete Class)
- **Interface:** `RecordActions` (CRUD Contract) → `StudentManager` (Implementation)
- **Multithreading:** `Runnable` → `Loader` (Simulated loading tasks)

## 💻 Technical Implementation

### 1. Data Management (Collections)

| Component | Implementation | Purpose |
|-----------|---|---|
| Primary Storage | `ArrayList<Student>` | Order preservation and sorting |
| Fast Lookup | `HashMap<Integer, Student>` | O(1) access time for duplicate checks |
| Sorting | Comparator Interface | Custom sorting logic (Desc. by Marks) |

### 2. File Persistence (I/O)
- **Format:** CSV (`rollNo,name,email,course,marks,grade`)
- **Reading:** BufferedReader loads data into collections at startup
- **Writing:** BufferedWriter saves memory state to `students.txt` on exit

### 3. Exception Handling
Robust error management using custom exceptions:
- `StudentNotFoundException`: Handles operations on non-existent IDs
- `InvalidMarksException`: Ensures marks stay within the 0-100 range
- **Validation:** Prevents empty fields, invalid emails, and duplicate IDs

### 4. Multithreading
- **Implementation:** `Loader` class implements `Runnable`
- **Function:** Provides visual feedback (loading bars) during File I/O and saving operations
- **Synchronization:** Uses `thread.join()` to ensure critical tasks complete before UI interaction

## ⚙️ Core Logic

### Grade Calculation Algorithm

| Marks Range | Grade |
|---|---|
| 90 - 100 | A+ |
| 80 - 89 | A |
| 70 - 79 | B+ |
| 60 - 69 | B |
| 50 - 59 | C |
| < 50 | D/F |

### Complexity Analysis

| Operation | Time Complexity | Notes |
|---|---|---|
| Add Student | O(1) | HashMap insertion |
| Search (ID) | O(1) | HashMap lookup |
| Sort | O(N log N) | Timsort (via Collections.sort) |
| File Load | O(N) | Linear read of text file |