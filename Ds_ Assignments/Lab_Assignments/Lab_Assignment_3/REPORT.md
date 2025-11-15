# Student Performance Tracker System – Implementation Report  
**Course:**  Bsc. (H) Cybersecurity
**Subject:** Data Structures and Algorithms 
**Student Name:** Mayank Rawat  
**Student ID:** 2401830005

## Executive Summary

This report presents the implementation of a Student Performance Tracker
System in C++. The system efficiently manages academic records using
advanced data structures and algorithms including searching, sorting,
and hashing techniques. The implementation demonstrates practical
applications of theoretical concepts in real-world academic performance
tracking scenarios.

## 1. Description of the Student Record ADT

### 1.1 Structure Design

The Student Record Abstract Data Type (ADT) is implemented as a class
with the following attributes:

``` cpp
class Student {
    int studentID;      // Unique identifier
    string studentName; // Student's full name
    float grade;        // Academic score (0-100)
    string courseDetails; // Enrolled course information
};
```

### 1.2 Key Methods

-   **Constructor**: Initializes student records with default or
    specified values\
-   **display()**: Outputs formatted student information\
-   **Getter/Setter methods**: Provide controlled access to private data
    members

### 1.3 Design Rationale

The ADT encapsulates all student-related data into a single, cohesive
unit. This design promotes: - **Data Integrity**: Controlled access to
student information\
- **Reusability**: The Student class can be used across different
components\
- **Maintainability**: Changes to student structure require minimal code
modification

## 2. Strategy for Implementing Searching, Sorting, and Hashing Algorithms

### 2.1 Searching Algorithms

#### **Sequential Search**

-   Implementation: Linear traversal through the student array\
-   Use Case: Finding students by name (string matching)\
-   Time Complexity: **O(n)**\
-   Strategy: Iterate through all records comparing target name with
    each student

#### **Binary Search**

-   Implementation: Divide-and-conquer approach on sorted array\
-   Use Case: Finding students by ID\
-   Time Complexity: **O(log n)**\
-   Strategy: Pre-sort array → divide search space → compare mid-element

### 2.2 Sorting Algorithms

#### **Bubble Sort**

-   Strategy: Compare adjacent elements and swap if out of order\
-   Best for: Small or nearly sorted datasets

#### **Insertion Sort**

-   Strategy: Insert each element into its correct position\
-   Best for: Small or partially sorted arrays

#### **Merge Sort**

-   Strategy: Divide-and-conquer\
-   Best for: Large datasets requiring stable sorting

#### **Quick Sort**

-   Strategy: Pivot-based partitioning\
-   Best for: Large datasets (excellent average performance)

#### **Heap Sort**

-   Strategy: Build max-heap then extract repeatedly\
-   Best for: Guaranteed **O(n log n)**

### 2.3 Hashing Implementation

-   Hash Table Size: **10 buckets**\
-   Hash Function: `h(key) = key % TABLE_SIZE`\
-   Collision Handling: **Chaining (linked lists)**

Collision Strategy: 1. Compute index\
2. Insert if empty\
3. If collision → traverse chain → append node

## 3. Approach to Time Complexity Comparison

### 3.1 Measurement Methodology

Using C++ `chrono` for microsecond precision:

``` cpp
auto start = chrono::high_resolution_clock::now();
// code
auto end = chrono::high_resolution_clock::now();
```

### 3.2 Comparison Table

  Algorithm        Best Case    Average Case   Worst Case   Space
  ---------------- ------------ -------------- ------------ ----------
  Bubble Sort      O(n)         O(n²)          O(n²)        O(1)
  Insertion Sort   O(n)         O(n²)          O(n²)        O(1)
  Merge Sort       O(n log n)   O(n log n)     O(n log n)   O(n)
  Quick Sort       O(n log n)   O(n log n)     O(n²)        O(log n)
  Heap Sort        O(n log n)   O(n log n)     O(n log n)   O(1)

### 3.3 Testing Strategy

-   Same dataset for all algorithms\
-   Multiple runs\
-   Various array sizes\
-   Time measured in microseconds

## 4. Analysis of System's Efficiency and Functionality

### 4.1 System Efficiency

#### **Search Performance**

-   Hash Table: **O(1)** average\
-   Binary Search: **O(log n)**\
-   Sequential Search: **O(n)**

### 4.2 Sorting Performance (Sample Results)

    Algorithm         Time (µs)     Efficiency
    Bubble Sort       12–15         Poor
    Insertion Sort    10–12         Good
    Merge Sort        18–22         Excellent
    Quick Sort        15–18         Best average
    Heap Sort         20–25         Consistent

### 4.3 Memory Efficiency

-   Student Object: \~100 bytes\
-   Hash Table: O(n + m)\
-   Sorting Arrays: O(n)

### 4.4 Scalability

-   \< 50 records → all algorithms OK\

-   50--500 → O(n log n) preferred\

-   500 → hashing becomes essential

## 5. Testing Results

### 5.1 Sample Input/Output

**Add Student Example**

    ID: 109  
    Name: Jaggu  
    Grade: 87.5  
    Course: Computer Science

Output:

    Student inserted successfully!
    Index = 9

### 5.2 Sorted Output (By Grades)

    Rank 1: Bheem - 95.2
    Rank 2: Keechak - 92.3
    Rank 3: Kalia - 91.6
    Rank 4: Indumati - 88.7
    ...

## 6. Challenges and Solutions

  Challenge              Solution
  ---------------------- --------------------------------
  Hash collisions        Chaining
  Keeping array sorted   Auto-sort before binary search
  Timing accuracy        High-resolution clock
  Input validation       Error checking added

## 7. Conclusion

The system successfully demonstrates core DSA concepts: - Efficient
hashing\
- Flexible searching\
- Robust sorting\
- Time complexity analysis\
- Modular, scalable architecture

### **Future Enhancements**

-   File I/O persistence\
-   Better hash functions\
-   GUI dashboard\
-   Extended analytics