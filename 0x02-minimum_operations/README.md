# 0x02. Minimum Operations

## Description

This project involves solving the problem of finding the minimum number of operations needed to achieve exactly `n` characters in a file starting with a single character `H`. The allowed operations are "Copy All" and "Paste". The challenge is to devise an efficient algorithm to calculate the minimum number of operations using these constraints.

## Learning Objectives

By the end of this project, you should be able to:

- Understand and apply dynamic programming principles to break down problems into simpler subproblems.
- Perform prime factorization to help in reducing the problem to a simpler form.
- Approach problems with code optimization techniques to find the most efficient solution.
- Use greedy algorithms to make optimal choices at each step of the problem-solving process.
- Implement solutions in Python, utilizing loops, conditionals, and functions effectively.

## Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.4.3)
- Each file should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- A `README.md` file at the root of the folder is mandatory
- Code should be documented
- Code should use the PEP 8 style (version 1.7.x)
- All files must be executable

## Tasks

### 0. Minimum Operations

#### Description

Write a method that calculates the fewest number of operations needed to result in exactly `n` `H` characters in the file.

#### Prototype

```python
def minOperations(n)`
