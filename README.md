# Python Algorithm Templates

This repository contains a collection of Python implementations for classic algorithmic problems and data structures, organized by topic. Each folder focuses on a specific area, providing reusable templates and clear examples for common coding interview and competitive programming problems.

## Directory Structure

- **binary_search/**: Binary search variations and applications, including lower bound and searching in rotated arrays.
- **dp/**: Dynamic programming problems such as 0/1 knapsack, unbounded knapsack, coin change, and sum problems.
- **graphs/**: Graph traversal algorithms (BFS, DFS), topological sort, and union-find data structure.
- **linked_list/**: Singly and doubly linked list implementations, including LRU cache.
- **prefix_sum/**: 1D and 2D prefix sums, difference arrays, and suffix sums for range query problems.
- **trie/**: Trie (prefix tree) data structure for efficient string search and manipulation.
- **two_pointer/**: Two-pointer techniques for subarray, sliding window, and merging problems.

## Usage

Each Python file is self-contained and includes example usage or test cases at the bottom. You can run any file directly to see sample outputs, or import the functions into your own projects.

## Example: Unbounded Knapsack

```python
from dp.0nknapsack import unbounded_knapsack_1d
weights = [2, 3, 4]
values = [4, 5, 6]
capacity = 5
print(unbounded_knapsack_1d(weights, values, capacity))  # Output: 9
```

## Contributing

Feel free to open issues or submit pull requests for improvements, bug fixes, or additional algorithm templates.

## License

This repository is licensed under the MIT License.
