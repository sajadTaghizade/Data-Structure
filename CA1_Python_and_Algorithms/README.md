<div align="center">
  <h1>
    📚 Data Structures - Computer Assignment 1 🐍
  </h1>
  <h2>
    Introduction to Python and Algorithmic Problems
  </h2>
  <p>
    This project is the first assignment for the Data Structures course, designed to introduce fundamental concepts of Python programming and algorithmic problem-solving.
  </p>
</div>

<hr>

## 🚀 Problems Overview

<table>
  <tr>
    <td valign="top" width="50%">
      <h3>
        Problem 1: Library Management (String to Integer)
      </h3>
      <p>
        The goal is to implement a function that mimics the behavior of the <code>atoi</code> function. It parses a string containing various characters and extracts the first valid signed 32-bit integer.
      </p>
      <details>
        <summary>
          <strong>Implementation Rules</strong>
        </summary>
        <ul>
          <li>Ignore leading whitespace.</li>
          <li>Handle optional leading '+' or '-' signs.</li>
          <li>Stop parsing upon encountering a non-digit character.</li>
          <li>Return 0 if no digits are found.</li>
          <li>Clamp the result to the 32-bit signed integer range if it overflows.</li>
        </ul>
      </details>
    </td>
    <td valign="top" width="50%">
      <h3>
        Problem 2: Hamzeh's Intelligence (Sudoku Validator)
      </h3>
      <p>
        This problem requires writing a program to validate a partially filled 9x9 Sudoku board. The program checks if the board is valid according to Sudoku rules, without necessarily being solvable.
      </p>
      <details>
        <summary>
          <strong>Validation Rules</strong>
        </summary>
        <ul>
          <li>Each row must contain the digits 1-9 without repetition.</li>
          <li>Each column must contain the digits 1-9 without repetition.</li>
          <li>Each of the nine 3x3 sub-boxes must contain the digits 1-9 without repetition.</li>
          <li>Only the filled cells need to be validated.</li>
        </ul>
      </details>
    </td>
  </tr>
  <tr>
    <td valign="top" width="50%">
      <h3>
        Problem 3: Ross and the Lettuce (Spiral Matrix Traversal)
      </h3>
      <p>
        The task is to traverse a given m x n matrix in a spiral order, starting from the top-left corner, and return a list of all elements in the order they were visited.
      </p>
    </td>
    <td valign="top" width="50%">
      <h3>
        Problem 4: Danger Zone (Exception Handling)
      </h3>
      <p>
        This problem involves writing a program that handles specific runtime errors based on user commands. The program must catch and report errors without crashing.
      </p>
      <details>
        <summary>
          <strong>Errors to Handle</strong>
        </summary>
        <ul>
          <li>
            <strong><code>sefre</code></strong>: For division by zero.
          </li>
          <li>
            <strong><code>nulle</code></strong>: For operations on a null/None object.
          </li>
          <li>
            <strong><code>oute</code></strong>: For accessing an out-of-bounds list index.
          </li>
        </ul>
      </details>
    </td>
  </tr>
</table>

<hr>

