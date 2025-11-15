# Smart City Road Navigation System - Project Report

**Course:**  Bsc. (H) Cybersecurity
**Subject:** Data Structures and Algorithms 
**Student Name:** Mayank Rawat  
**Student ID:** 2401830005

---

## 📋 Project Overview

> The Smart City Road Navigation System is a comprehensive software solution for managing urban road networks, optimizing navigation routes, and planning cost-effective infrastructure. The system leverages advanced data structures and algorithms to address real-world transportation challenges.

### Key Objectives
- Efficient road network representation using graphs.
- Optimal path finding using multiple algorithms.
- Hierarchical city zone indexing with trees.
- Infrastructure planning with MST algorithms.
- Construction prioritization using topological sort.

---

## 🏗️ System Architecture

### 1. Road Network ADT

#### Core Attributes:
```cpp
- NodeID:       Unique intersection identifier
- NodeName:     Descriptive location name  
- Connections:  Adjacent roads with distances
- ZoneDetails:  Zone classification (Residential/Commercial/Industrial)
```

#### Key Methods:
- `insertNode()`: Add an intersection to the network.
- `findShortestPath()`: Compute optimal routes between nodes.
- `organizeZones()`: Manage hierarchical zone information.

### 2. Data Structure Implementation

| Structure          | Purpose                    | Complexity   |
|--------------------|----------------------------|--------------|
| **Adjacency Matrix** | Dense graph representation | O(V²) space  |
| **Adjacency List**   | Sparse graph representation| O(V+E) space |
| **Binary Search Tree** | Basic zone indexing        | O(log n) avg |
| **AVL Tree**         | Balanced zone indexing     | O(log n) guar|

---

## 🛣️ Graph Representations

### Adjacency Matrix
- A 2D array storing edge weights (distances).
- Provides direct O(1) access for edge queries.
- **Best for:** Dense road networks where most intersections are connected.
- **Memory:** O(V²)

### Adjacency List
- A vector of pairs, where each node stores a list of its neighbors and the distance to them.
- Space-efficient for sparse networks.
- Iteration-friendly for graph traversals (BFS, DFS).
- **Memory:** O(V + E)

---

## 🚀 Algorithm Implementations

### 1. Shortest Path Algorithms

#### Dijkstra's Algorithm
```text
Purpose: Single-source shortest path from a starting point to all other points.
Time Complexity: O((V + E) log V) with a priority queue.
Use Case: Real-time navigation from a user's current location.
```
**Implementation Features:**
- Priority queue for efficient extraction of the minimum distance node.
- Parent tracking array for simple path reconstruction.
- Distance array to store and update optimal distances.

#### Floyd-Warshall Algorithm
```text
Purpose: All-pairs shortest paths to find the optimal route between every pair of intersections.
Time Complexity: O(V³)
Use Case: Pre-computing a complete route table for the entire city.
```
**Implementation Features:**
- Dynamic programming approach.
- Generates a complete (V × V) distance matrix.
- Can handle negative edge weights (but not negative cycles).

### 2. Minimum Spanning Tree (MST) Algorithms

#### Prim's Algorithm
```text
Purpose: Designing a cost-effective road network by finding the minimum cost to connect all zones.
Time Complexity: O((V + E) log V)
Best For: Dense graphs, or when starting from a specific central node.
```
**Key Steps:**
1. Start from an arbitrary node.
2. Maintain a priority queue of edges connected to the MST.
3. Add the minimum weight edge to the MST.
4. Update distances of adjacent nodes.

#### Kruskal's Algorithm
```text
Purpose: Optimal infrastructure development with a global view of all possible connections.
Time Complexity: O(E log E)
Best For: Sparse graphs, as it focuses on the cheapest edges first.
```
**Key Steps:**
1. Sort all edges by weight in ascending order.
2. Use a **Union-Find** data structure for cycle detection.
3. Add edges to the MST if they don't form a cycle.
4. Stop when V-1 edges have been added.

### 3. Topological Sort
```text
Purpose: Prioritizing construction projects with dependencies (e.g., one-way roads).
Time Complexity: O(V + E)
Application: Determining a valid build order for a Directed Acyclic Graph (DAG).
```
**Implementation:**
- Kahn's algorithm, using in-degree calculation for each node.
- A queue-based approach for level-by-level processing.
- Includes cycle detection to ensure the graph is a valid DAG.

---

## 🌳 Tree Structures for Zone Management

### Binary Search Tree (BST)
- Provides standard hierarchical organization.
- An in-order traversal yields a sorted list of zones.
- Simple to implement but can become unbalanced, leading to O(n) search time.

### AVL Tree
- A self-balancing BST that guarantees logarithmic performance.
- Maintains a height constraint: `|left_height - right_height| ≤ 1`.
- **Guaranteed O(log n)** for insert, search, and delete operations.

#### Rotation Types:
| Case       | Condition                              | Action                    |
|------------|----------------------------------------|---------------------------|
| **Left-Left**  | Left-heavy, left child is left-heavy   | Right rotation            |
| **Right-Right**| Right-heavy, right child is right-heavy| Left rotation             |
| **Left-Right** | Left-heavy, left child is right-heavy  | Left-Right rotation       |
| **Right-Left** | Right-heavy, right child is left-heavy   | Right-Left rotation       |

---

## 📊 Performance Analysis

### Time Complexity Comparison

| Operation      | Dijkstra        | Floyd-Warshall | Prim's          | Kruskal's |
|----------------|-----------------|----------------|-----------------|-----------|
| **Time**       | O((V+E)log V)   | O(V³)          | O((V+E)log V)   | O(E log E)|
| **Space**      | O(V)            | O(V²)          | O(V)            | O(V)      |
| **Best For**   | Single source   | All pairs      | Dense MST       | Sparse MST|

### Space Complexity

| Data Structure      | Space Required |
|---------------------|----------------|
| **Adjacency Matrix**  | O(V²)          |
| **Adjacency List**    | O(V + E)       |
| **BST/AVL Tree**      | O(V)           |
| **Algorithm Arrays**  | O(V) typical   |

---

## 🎯 Key Features

#### 1. Navigation Features
- Multi-algorithm shortest path computation.
- Real-time route calculation.
- All-pairs distance pre-computation for quick lookups.
- Path reconstruction with step-by-step directions.

#### 2. Infrastructure Planning
- Cost optimization using MST algorithms.
- Construction prioritization via topological sort.
- Comparative analysis of Prim's vs. Kruskal's approach.
- Total cost calculation for budget planning.

#### 3. Zone Management
- Hierarchical indexing of city zones.
- Quick lookup using balanced AVL trees.
- Sorted display of zones by name or ID.
- Zone classification (Residential/Commercial/Industrial).

---

## 🧪 Testing and Validation

### Sample Test Network
```text
Nodes (7): Central Station, Tech Park, City Mall, Residential Area, Hospital, University, Airport
Roads (11): Bidirectional connections with varying distances
Zone Types: Commercial, Industrial, Residential, Healthcare, Educational, Transportation
```

### Test Cases
- **Shortest Path Testing:**
  - Verify path optimality for single-source and all-pairs.
  - Compare results of Dijkstra vs. Floyd-Warshall.
- **MST Validation:**
  - Ensure the final graph is connected with minimum total cost.
  - Compare the MSTs generated by Prim's and Kruskal's.
- **Topological Sort:**
  - Test with a DAG to verify a valid ordering.
  - Test with a cyclic graph to confirm cycle detection.

---

## 💡 Real-World Applications

| Application          | Algorithm Used      | Benefit                        |
|----------------------|---------------------|--------------------------------|
| **GPS Navigation**     | Dijkstra's          | Real-time, on-demand routing   |
| **Traffic Planning**   | Floyd-Warshall      | Pre-computed complete route table |
| **Utility Lines**      | MST Algorithms      | Minimum installation cost      |
| **Road Construction**  | Topological Sort    | Logical and efficient build order |
| **Emergency Services** | Shortest Path       | Quickest possible response routes |

---

## 📈 Future Enhancements
- **Advanced Algorithms:** A* pathfinding, Bellman-Ford, Johnson's algorithm.
- **Dynamic Features:** Real-time traffic updates, dynamic edge weight adjustment.
- **Visualization:** A graphical map display with animated path finding.
- **Optimization:** Parallel processing, caching mechanisms, heuristic improvements.

---

## 📚 Learning Outcomes

#### Technical Skills
✅ Graph theory implementation  
✅ Tree data structure mastery  
✅ Algorithm complexity analysis  
✅ C++ STL proficiency  
✅ Problem decomposition  

#### Conceptual Understanding
✅ Trade-offs between different algorithms  
✅ Balancing space-time complexity  
✅ Modeling real-world problems with data structures  
✅ System design principles  

---

## 🎓 Conclusion

The Smart City Road Navigation System successfully demonstrates:
- **Complete Implementation:** All required algorithms and data structures.
- **Practical Application:** Solves real-world transportation problems.
- **Performance Optimization:** Offers multiple algorithm choices for different scenarios.
- **Scalability:** Designed to handle city-scale networks efficiently.

### Key Achievements
✅ Dual graph representation (Matrix & List)  
✅ Multiple shortest path algorithms (Dijkstra's, Floyd-Warshall)  
✅ Two MST implementations (Prim's, Kruskal's)  
✅ Balanced tree structures for efficient indexing (AVL)  
✅ Topological sorting for DAGs  
✅ A comprehensive testing suite  

---

## 📦 Compilation & Usage

#### Compilation
```bash
g++ -std=c++11 smart_city_navigation.cpp -o smart_city
```
#### Quick Start
```bash
./smart_city
```
1. Run the program.
2. Load sample data (Option 8).
3. Explore shortest paths (Option 4).
4. View infrastructure planning (Option 5).
5. Analyze the complete network (Option 6).