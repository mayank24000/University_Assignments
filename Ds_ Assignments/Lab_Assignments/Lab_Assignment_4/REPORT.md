# Campus Navigation and Utility Planner -- Brief Project Report

**Course:**  Bsc. (H) Cybersecurity
**Subject:** Data Structures and Algorithms 
**Student Name:** Mayank Rawat  
**Student ID:** 2401830005

------------------------------------------------------------------------

## **1. Project Overview**

A compact system built in C++ to model campus buildings, navigate paths,
and plan utility routes using efficient data structures.

**Core Features** - Building management using BST & AVL Trees\
- Graph-based campus navigation\
- Dijkstra's shortest path algorithm\
- Kruskal's MST for utility planning\
- Expression tree for billing calculations

------------------------------------------------------------------------

## **2. Building Data ADT**

    class Building {
        int buildingID;
        string buildingName;
        string locationDetails;
    };

Used across BST, AVL, and Graph nodes.

------------------------------------------------------------------------

## **3. Implementation Strategy**

### Trees

-   **BST:** Basic hierarchical storage\
-   **AVL:** Balanced tree ensuring O(log n) operations

### Graphs

-   **Adjacency List:** For sparse graphs\
-   **Adjacency Matrix:** For dense graphs

### Expression Tree

-   Built from postfix expressions\
-   Supports +, -, \*, /

------------------------------------------------------------------------

## **4. Algorithms**

-   **Dijkstra's Algorithm:** Optimal pathfinding\
-   **Kruskal's MST:** Minimum cost utility layout\
-   **Tree Traversals:** Inorder, Preorder, Postorder

------------------------------------------------------------------------

## **5. Efficiency Summary**

  Operation   BST    AVL        Matrix   List
  ----------- ------ ---------- -------- ------
  Insert      O(h)   O(log n)   O(1)     O(1)
  Search      O(h)   O(log n)   O(V)     O(V)

------------------------------------------------------------------------

## **6. Learning Outcomes**

-   Implemented balanced trees and graph structures\
-   Understood shortest-path and MST algorithms\
-   Analyzed performance and complexity\
-   Applied DS & Algo concepts to real-world navigation

------------------------------------------------------------------------

## **7. Conclusion**

A complete, modular, and scalable campus navigation planner implementing
all major DSA concepts.

**Future Enhancements** - A\* Search\
- File I/O\
- GUI-based map\
- Dynamic graph support

