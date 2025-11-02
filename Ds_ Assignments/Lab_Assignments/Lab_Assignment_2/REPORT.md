# Lab Assignment 2 – Customer Support Ticket System

##  Aim
To implement a simple *Customer Support Ticket System* in C++ using linked lists, stacks, queues, and polynomial linked lists.  
The system keeps track of customer tickets, allows undo operations, handles urgent tickets first, and manages round-robin processing for fairness.

---

## ⚙ Approach Used

### 1. Ticket Structure
Each ticket holds:
- Ticket ID
- Customer name
- Issue details
- Priority level (1 = urgent)

### 2. Singly Linked List
Used for storing all tickets dynamically.  
New tickets are added at the end, and deletion is done by ID.

### 3. Stack
Used to implement *undo* functionality.  
Whenever a ticket is added or deleted, the action is pushed onto the stack.  
Undo removes the last operation.

### 4. Priority Queue
Urgent tickets (with smaller priority numbers) are processed before others.  
It uses priority_queue with a comparison function to sort automatically.

### 5. Circular Queue
Handles *round-robin processing* of tickets, simulating how multiple agents take turns in a loop.

### 6. Polynomial Linked List
Used for comparing billing history between two records using linked list nodes.

---

##  Output Example
``` 
Ticket created with ID 1
Ticket created with ID 2
Ticket created with ID 3

All Tickets:
Tickets List:
ID: 1 | Name: Diana | Priority: 1
Issue: Login not working
ID: 2 | Name: Ethan | Priority: 2
Issue: App crashes
ID: 3 | Name: Frank | Priority: 3
Issue: Payment issue

Undo last ticket:
Undo: Ticket 3 removed.

Remaining Tickets:
Tickets List:
ID: 1 | Name: Diana | Priority: 1
Issue: Login not working
ID: 2 | Name: Ethan | Priority: 2
Issue: App crashes

Priority processing:
Processing urgent tickets:
ID 1 (Diana) done.
ID 2 (Ethan) done.
ID 3 (Frank) done.

Round robin demo:
Round robin IDs: 1 2 3 
Round robin start:

Billing comparison:
Billing Record 1: 40x^2 + 10x^1
Billing Record 2: 40x^2 + 10x^1
Records are same.

```