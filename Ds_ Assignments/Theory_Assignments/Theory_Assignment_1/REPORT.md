# Weather Data Storage System - Report

## a. Description of the Weather Record ADT

The Weather Record ADT keeps the basic weather information for a city.  
Each record stores three pieces of data:
- *Date* – when the temperature was recorded  
- *City* – the name of the place  
- *Temperature* – the temperature value  

I used a simple struct called WeatherRecord to hold these values together.  
It helps in managing and organizing multiple entries easily.

---

## b. Strategy for Memory Representation (Row-Major vs Column-Major)

The data is stored using a *2D array*, where:
- Each row stands for a *year*.
- Each column stands for a *city*.

Two different ways are used to go through the data:

### Row-Major Order:
- Data is read row by row.
- It goes through all cities of one year, then moves to the next year.
- This way matches how arrays are stored in C++ memory, so it runs faster.

### Column-Major Order:
- Data is read column by column.
- It reads all years of one city first, then moves to the next city.
- Useful when comparing a single city across multiple years.

---

## c. Approach to Handling Sparse Data

In some cases, there might be no temperature data for a specific city or year.  
To handle that, I used the **sentinel value -1** in the 2D array.  
This value simply means that the data is missing.  

This is an easy method for small datasets and doesn’t require advanced data structures like linked lists or maps.

---

## d. Time and Space Complexity Analysis

### Time Complexity
| Operation | Time Complexity | Explanation |
|------------|----------------|--------------|
| Insert | O(1) | Directly adds the temperature in the array |
| Delete | O(1) | Replaces the value with -1 instantly |
| Retrieve | O(1) | Accessed directly using index |

### Space Complexity
| Aspect | Complexity | Description |
|---------|-------------|-------------|
| Storage | O(n × m) | For n years and m cities |

---

## Summary

The Weather Data Storage System can:-
- Store and access temperature data easily  
- Support both row-major and column-major representations  
- Manage missing entries using -1  
- Provide clear understanding of how 2D arrays and memory layout work in C++  

This project helped me practice arrays, loops, and class concepts in a simple and meaningful way.