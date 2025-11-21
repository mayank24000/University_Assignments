# Grocery Store Inventory Management System

## Overview
A C++ implementation of an inventory management system using array-based data structures, sparse matrices, and complexity analysis.

## Features
- ✓ Dynamic inventory management with insert/delete/search
- ✓ Multi-dimensional arrays for price-quantity tables
- ✓ Row-major and column-major ordering
- ✓ Sparse matrix representation for space optimization
- ✓ Low stock alerts
- ✓ Summary reports

## Compilation
```bash
g++ -o inventory inventory_system.cpp
./inventory
```

# Complexity Analysis Report

## 1. Insert Item Operation
- **Time Complexity**: O(1) - Direct insertion at end of array
- **Space Complexity**: O(1) - Only storing one item
- **Analysis**: Constant time insertion when capacity is available

## 2. Delete Item Operation
- **Time Complexity**: O(n) - Search O(n) + Shift elements O(n)
- **Space Complexity**: O(1) - In-place deletion
- **Analysis**: Linear search to find item, then shift remaining elements

## 3. Search by ID Operation
- **Time Complexity**: O(n) - Linear search through array
- **Space Complexity**: O(1) - No extra space needed
- **Analysis**: Worst case checks all n elements

## 4. Search by Name Operation
- **Time Complexity**: O(n) - Linear search through array
- **Space Complexity**: O(1) - No extra space needed
- **Analysis**: Worst case checks all n elements

## 5. Display All Items
- **Time Complexity**: O(n) - Iterate through all items
- **Space Complexity**: O(1) - No extra storage
- **Analysis**: Must visit each item once

## 6. Create Price-Quantity Table
- **Time Complexity**: O(n) - Create n rows with 2 columns
- **Space Complexity**: O(n*m) where m=2 - 2D array storage
- **Analysis**: Allocates and populates 2D array

## 7. Display Row-Major Order
- **Time Complexity**: O(n*m) - Access all elements row by row
- **Space Complexity**: O(1) - No extra storage
- **Analysis**: Standard row-major traversal

## 8. Display Column-Major Order
- **Time Complexity**: O(n*m) - Access all elements column by column
- **Space Complexity**: O(1) - No extra storage
- **Analysis**: Column-major traversal pattern

## 9. Sparse Representation
- **Time Complexity**: O(n) - Check all items once
- **Space Complexity**: O(k) where k = sparse elements
- **Analysis**: Only stores items below threshold, saves space when k << n

## 10. Display Sparse Matrix
- **Time Complexity**: O(k) where k = sparse elements
- **Space Complexity**: O(1) - Display only
- **Analysis**: Iterate only through sparse elements

## 11. Low Stock Alert
- **Time Complexity**: O(n) - Check all items
- **Space Complexity**: O(1) - No extra storage
- **Analysis**: Linear scan to find items below threshold

## 12. Summary Report
- **Time Complexity**: O(n) - Calculate statistics for all items
- **Space Complexity**: O(1) - Few variables for calculation
- **Analysis**: Single pass through array for aggregation

## Space Optimization Analysis

### Regular Storage vs Sparse Storage
- **Regular Array**: n items × sizeof(InventoryItem) bytes
- **Sparse Matrix**: k items × sizeof(SparseElement) bytes where k << n
- **Savings**: Significant when many items are rarely restocked (k is small)

### Row-Major vs Column-Major
- **Memory Layout**: Same total space, different access patterns
- **Row-Major**: Better cache performance for row-wise operations
- **Column-Major**: Better for column-wise aggregations