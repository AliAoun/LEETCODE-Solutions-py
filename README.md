# LEETCODE-Solutions-py

![LeetCode](https://img.shields.io/badge/LeetCode-Solutions-orange?logo=leetcode)
![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)

[![LeetCode Stats](https://leetcard.jacoblin.cool/aliaoun?theme=catppuccinMocha&font=Fira%20Code&ext=activity)](https://leetcode.com/u/aliaoun/)

A collection of efficient and well-commented Python solutions for popular LeetCode problems. Each file is named after its corresponding LeetCode problem for easy reference.

---

## 📂 Repository Structure

- Each file is named as `<problem_number>_<Problem_Name>.py`
- Each file contains a single class-based solution, often with time and space complexity analysis in comments.
- Solutions cover a wide range of topics: arrays, strings, dynamic programming, trees, graphs, stacks, queues, and more.

---

## 📝 Example Solution

```python
# 53_Maximum_Subarray.py
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum = 0
        maxSub = nums[0]
        for n in nums:
            if curSum < 0:
                curSum = 0
            curSum += n
            maxSub = max(maxSub, curSum)
        return maxSub
    # time complexity: O(n)
    # space complexity: O(1)
```

---

## 🚀 How to Use

1. **Clone the repository:**
   ```sh
   git clone https://github.com/AliAoun/LEETCODE-Solutions-py.git
   cd LEETCODE-Solutions-py
   ```

2. **Browse solutions:**
   - Find the problem you want by its number or name.
   - Open the corresponding `.py` file for the solution and explanation.

3. **Run a solution:**
   - Copy the class into your local environment or LeetCode editor.
   - Add your own test cases as needed.

---

## 📊 Topics Covered

- Arrays & Strings
- Hashing & Sets
- Two Pointers & Sliding Window
- Binary Search
- Linked Lists
- Trees & Binary Trees
- Dynamic Programming
- Stacks & Queues
- Greedy Algorithms
- Backtracking

---

## 🏆 Progress

- Problems solved: **`[number of files]`**
- Language: **Python 3**

---

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests for improvements or new solutions.

---

## 📚 License

This repository is licensed under the [MIT License](LICENSE).

---

## ⭐️ Acknowledgements

- [LeetCode](https://leetcode.com/) for the problems and platform.
- Python community for helpful discussions and resources.

---

> _Happy Coding!_

---

**My LeetCode Profile:** [aliaoun](https://leetcode.com/u/aliaoun/)