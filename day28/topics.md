---

## 📘 **Topic: Sorting Algorithms**

Sorting problems test your understanding of algorithmic thinking, data organization, and optimal approaches. Below are the top sorting-based patterns that commonly appear in interviews.

---

### ✅ **1. Basic Sorting Logic (Built-in / Custom Comparator / Manual Sorts)**

**Explanation:**
You are often required to sort arrays directly or based on specific keys using built-in or custom sorting.

**Techniques:**

* Use `sorted()` or `.sort()` for basic sorting.
* Use lambda/comparator for custom logic.
* Manual sorts like bubble/selection are mostly for learning.

**Example 1: Sort a list of integers**

```python
arr = [4, 2, 1, 3]
print(sorted(arr))  # Output: [1, 2, 3, 4]
```

**Example 2: Sort strings by length**

```python
words = ["apple", "kiwi", "banana"]
words.sort(key=lambda x: len(x))
print(words)  # Output: ['kiwi', 'apple', 'banana']
```

---

### ✅ **2. Counting Sort / Bucket Sort / Radix Sort**

These are **non-comparison-based sorting algorithms**, great for constrained inputs.

#### 📌 **Counting Sort**

Efficient for small ranges (e.g., 0–1000).

**Example:**

```python
def counting_sort(arr):
    count = [0] * (max(arr) + 1)
    for num in arr:
        count[num] += 1
    result = []
    for i, c in enumerate(count):
        result.extend([i] * c)
    return result

print(counting_sort([4, 2, 2, 8, 3, 3, 1]))
# Output: [1, 2, 2, 3, 3, 4, 8]
```

#### 📌 **Bucket Sort**

Divide elements into buckets and sort each.

**Example:**

```python
def bucket_sort(arr):
    buckets = [[] for _ in range(10)]
    for num in arr:
        index = int(num * 10)
        buckets[index].append(num)
    for bucket in buckets:
        bucket.sort()
    return [num for bucket in buckets for num in bucket]

print(bucket_sort([0.78, 0.17, 0.39, 0.26]))
# Output: [0.17, 0.26, 0.39, 0.78]
```

#### 📌 **Radix Sort**

Works well for fixed-length integers.

**Example:**

```python
def counting_sort_by_digit(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    for i in arr:
        index = (i // exp) % 10
        count[index] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    i = n - 1
    while i >= 0:
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1
    return output

def radix_sort(arr):
    max_val = max(arr)
    exp = 1
    while max_val // exp > 0:
        arr = counting_sort_by_digit(arr, exp)
        exp *= 10
    return arr

print(radix_sort([170, 45, 75, 90, 802, 24, 2, 66]))
# Output: [2, 24, 45, 66, 75, 90, 170, 802]
```

---

### ✅ **3. Custom Sorting with Comparator / Lambda Function**

**Explanation:**
You often need to sort based on multiple keys or reversed logic.

**Example 1: Sort tuples by second element**

```python
arr = [(1, 3), (2, 2), (4, 1)]
arr.sort(key=lambda x: x[1])
print(arr)  # Output: [(4, 1), (2, 2), (1, 3)]
```

**Example 2: Sort strings with custom alphabet order**

```python
order = "cba"
mapping = {ch: i for i, ch in enumerate(order)}

words = ["abc", "acb", "bca"]
words.sort(key=lambda word: [mapping[ch] for ch in word])
print(words)  # Output: ['bca', 'acb', 'abc']
```

---

### ✅ **4. Two Arrays or Sorting with Binary Search / Greedy**

**Explanation:**
Problems may involve **two-pointer** or **binary search** after sorting.

#### 📌 **Example: Two Sum with Two-Pointers**

```python
def two_sum_sorted(arr, target):
    arr.sort()
    l, r = 0, len(arr) - 1
    while l < r:
        if arr[l] + arr[r] == target:
            return [arr[l], arr[r]]
        elif arr[l] + arr[r] < target:
            l += 1
        else:
            r -= 1
    return []

print(two_sum_sorted([1, 4, 2, 3], 5))  # Output: [2, 3]
```

#### 📌 **Example: Minimize absolute difference (Greedy + Sort + Binary Search)**

```python
import bisect
def min_diff_sum(A, B):
    A.sort()
    total = 0
    for b in B:
        idx = bisect.bisect_left(A, b)
        min_diff = float('inf')
        if idx < len(A): min_diff = abs(A[idx] - b)
        if idx > 0: min_diff = min(min_diff, abs(A[idx - 1] - b))
        total += min_diff
    return total

print(min_diff_sum([1, 3, 5], [2, 4, 6]))  # Output: 3
```

---

### ✅ **5. Interval Sorting / Activity Selection Problems**

**Explanation:**
Sort intervals by **start** or **end time** to apply greedy techniques.

#### 📌 **Example: Activity Selection (Max Non-Overlapping Intervals)**

```python
def activity_selection(intervals):
    intervals.sort(key=lambda x: x[1])  # sort by end time
    count = 0
    end = -1
    for start, finish in intervals:
        if start >= end:
            count += 1
            end = finish
    return count

print(activity_selection([(1, 3), (2, 4), (3, 5), (0, 6)]))  # Output: 2
```

#### 📌 **Example: Merge Intervals**

```python
def merge_intervals(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = []
    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])
    return merged

print(merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]))
# Output: [[1, 6], [8, 10], [15, 18]]
```

---

## 🧠 Summary

| Pattern                       | Use Case                                         |
| ----------------------------- | ------------------------------------------------ |
| **Basic Sorting**             | Simple sort tasks, key-based sorting             |
| **Counting/Bucket/Radix**     | When constraints are suitable (integers, ranges) |
| **Custom Comparator**         | Multi-key sorting, prioritization                |
| **Two-pointer/Binary Search** | Pairing, difference minimization, efficiency     |
| **Interval-based Sorting**    | Schedules, greedy, overlapping intervals         |

---

