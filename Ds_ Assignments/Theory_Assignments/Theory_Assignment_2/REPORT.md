# Hospital Patient Record Management System (Friend’s Version)

Course Code: ENCS205 / ENCA201  
Subject: Data Structures  
Semester: 3rd  
Department: CSE  
Session: 2025–26

---

## Aim
To design and implement a hospital management system using Linked List, Stack, Queue, and other linear data structures.

---

## Description

### Patient Linked List
Stores patient info dynamically (ID, name, date, treatment).  
Functions: add, remove, and display patients.

### Undo Stack
Stores the last added patient info and helps undo the last admission.

### Priority Queue
Handles emergency cases by giving higher priority (smaller number = more urgent).

### Circular Queue
Simulates patient rotation for round-robin handling.

### Polynomial (Billing)
Represents billing as polynomial expressions and compares them.

### Postfix Evaluation
Evaluates inventory expressions using stacks.

---

## Sample Output

```
Admitted patient Karan Singh with ID 1
Admitted patient Sneha Roy with ID 2
Admitted patient Rohit Jain with ID 3

All admitted patients:
ID: 1 | Name: Karan Singh | Date: 02/09/2025
Treatment: Fever observation
ID: 2 | Name: Sneha Roy | Date: 03/09/2025
Treatment: Minor fracture
ID: 3 | Name: Rohit Jain | Date: 04/09/2025
Treatment: Appendix surgery

Undoing last admission:
Undo successful: removed patient ID 3

After undo:
ID: 1 | Name: Karan Singh | Date: 02/09/2025
Treatment: Fever observation
ID: 2 | Name: Sneha Roy | Date: 03/09/2025
Treatment: Minor fracture

Emergency Queue by priority:
Emergency Handling by Priority:
ID 3 (Rohit Jain) - Priority 1
ID 1 (Karan Singh) - Priority 2
ID 2 (Sneha Roy) - Priority 4

Round robin process demo:
Patients in round-robin queue: 1 2 3 
Round-robin emergency simulation:
Cycle 1: Handling patient ID 1
Cycle 2: Handling patient ID 2

Billing comparison:
100x^2 + 50x^1
100x^2 + 50x^1
Bills are same.

Postfix Expression: 5 3 + 2 *
Result: 16

```