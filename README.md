# Dynamic Programming Python

## Memoization Recipe
_Memoization is basically decomposing given problem into smaller instances of the same problem with an overlapping structure._
* **Make it work** (using recursive method).
  * Visualise the problem as a **Tree**.
  * Implement the tree using recursion (Brute-Force solution).
  * Test it.
* **Make it efficient**.
  * Add a **memo** object i.e. make use of hash map or dictionary. It should be shared object i.e. pass by reference.
  * Add a base case to return memo values.
  * Store return values into the memo.