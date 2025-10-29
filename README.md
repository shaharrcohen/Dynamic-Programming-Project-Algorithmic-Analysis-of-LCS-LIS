# 🧮 Dynamic Programming Algorithms — LCS & LIS

> **Implementation and analysis of dynamic programming algorithms for the Longest Common Subsequence (LCS) and Longest Increasing Subsequence (LIS) problems — including correctness proofs, complexity analysis, and user-interactive testing.**

---

### 📊 Project Summary
| Category | Details |
|-----------|----------|
| 🎓 **Course** | Algorithmic Design — Dynamic Programming |
| 🧩 **Focus** | LCS (Longest Common Subsequence) & LIS (Longest Increasing Subsequence) |
| 💡 **Goal** | Apply dynamic programming principles to demonstrate optimal substructure and overlapping subproblems |
| ⚙️ **Tech Stack** | Python 3.10+, standard library only (`bisect`, `ast`) |
| 🧠 **Core Concepts** | Dynamic programming, recursion, optimal substructure, memoization, combinatorial enumeration |
| 📈 **Outputs** | Length, count, and all unique sequences for both LCS & LIS problems |
| 👩‍💻 **Author** | Shahar Cohen |

---

## 📖 Overview
This project focuses on **algorithmic design and dynamic programming techniques** applied to two classical problems:

1. **LCS — Longest Common Subsequence**  
   Computes and analyzes the *Longest Common Subsequence* between two input sequences, using DP table construction and sequence backtracking.

2. **LIS — Longest Increasing Subsequence**  
   Finds the *Longest Increasing Subsequence* in a given list with binary constraints, applying efficient DP-based reconstruction.

The project highlights **optimal substructure**, **overlapping subproblems**, and **correctness validation** of both algorithms.

---

## 🧩 Implemented Functions

| Function | Description |
|-----------|--------------|
| `build_lcs_matrix(A, B)` | Builds the dynamic programming table for LCS. |
| `number_of_lcs(A, B)` | Returns the number of distinct longest common subsequences. |
| `all_lcs(A, B, limit)` | Lists all LCS variants up to a user-defined limit. |
| `all_unique_lcs(A, B, limit)` | Extracts all unique LCS sequences (sorted). |
| `length_of_lis(A, C)` | Returns the length of the LIS under binary mask constraints. |
| `number_of_lis(A, C)` | Counts all possible LIS sequences. |
| `all_lis(A, C, teta)` | Reconstructs all LIS sequences up to a limit. |
| `all_unique_lis(A, C, teta)` | Returns unique LIS sequences only. |
| `safe_input(prompt)` | Safely reads and validates list input from the user. |
| `main()` | Interactive test environment to execute all functionalities. |

---

## 🧠 Key Features 🧩

| Feature | Description |
|----------|-------------|
| 🧮 **Dynamic Programming Design** | Implements both top-down reasoning and bottom-up table computation. |
| 🧩 **LCS & LIS Integration** | Unified implementation demonstrating two cornerstone DP problems. |
| 🔁 **Subproblem Reuse** | Optimized by reusing computed states for efficiency. |
| 🧪 **Self-Testing Console** | Interactive interface via `main()` with safe user input. |
| 🧠 **Optimal Substructure Validation** | Each algorithm verified for correctness and determinism. |
| 📊 **Complexity Analysis** | Includes formal analysis of both time and space requirements. |

---

## 🧮 Complexity Analysis 📈

| Algorithm | Description | Time Complexity | Space Complexity |
|------------|--------------|----------------|------------------|
| **LCS Table Construction** | Builds full DP table of subsequence lengths | **O(n × m)** | **O(n × m)** |
| **LCS Enumeration** | Recursively extracts sequences from DP matrix | **O(k × n × m)** | **O(n × m)** |
| **LIS (binary mask)** | Computes increasing subsequences from masked input | **O(n²)** | **O(n)** |
| **Optimized LIS (bisect)** | Binary search improvement for length only | **O(n log n)** | **O(n)** |

---

## 💻 Requirements 💽

| Requirement | Details |
|--------------|----------|
| 🐍 **Python** | Version 3.10 or higher |
| 📦 **Libraries** | Only uses built-in modules: `bisect`, `ast` |
| 🎯 **Input Safety** | Uses a custom `safe_input()` parser for validation |

---

## 🧾 Example Use Case 📘

| Scenario | Explanation |
|-----------|--------------|
| 🔢 **LCS Comparison** | Find the common structure between two sequences (e.g., genetic strings, code diffs). |
| 📈 **LIS Analysis** | Detect growth patterns in constrained numeric data. |
| 🧮 **Educational Purpose** | Demonstrate dynamic programming design patterns in algorithmic problem solving. |

---

## 🧭 How to Run
```bash
python LongestSubsequence.py
