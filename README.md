# 📂 Python Beginner Arcade: Calculator & Guessing Game

![Python](https://shields.io)
![License](https://shields.io)
![Level](https://shields.io)

Welcome to my first official Python programming repository! This project serves as a showcase of my foundational coding journey, putting key programming paradigms into action through two classic terminal applications: an **Interactive Number Guessing Game** and a **Robust Terminal Calculator**.

---

## 🚀 Projects Included

### 🎮 1. Number Guessing Game
A logical game where the computer selects a pseudo-random integer, and the player gets dynamic hints (`Too High` / `Too Low`) until the correct number is guessed.
* **Core Mechanisms Used:** `random` module, tracking counters (`tries`), interactive `while` loops, and localized `if/elif/else` conditioning syntax.

### 🧮 2. Production-Grade Terminal Calculator
A powerful multi-operator calculator built to simulate industrial software input practices. It safely conducts mathematical routing with a zero-crash guarantee.
* **Core Mechanisms Used:** `try/except` exception blocks, continuous error isolation loops, math handling (`+`, `-`, `*`, `%`, `**`, `/`), explicit zero-division guards, and string data mutations (`.strip().lower()`).

---

## 🛠️ Key Architectural Technical Highlights
Instead of writing standard raw script sheets, these programs deliberately deploy technical implementations typically missing in standard beginner code:
* **Defensive Input Exception Handling:** Completely isolates input parsing (`ValueError`), preventing terminal crashes if an invalid string or symbol character is inputted by the user.
* **Clean Terminal Loop Lifecycles:** Implements automated loop states allowing infinite calculations or games to run sequentially without needing script termination and re-initialization.
* **DRY Code Structuring (Don't Repeat Yourself):** Demonstrates proper application of structural Python functions (`def`) to encapsulate repeated parameter loops into single, easily readable logic components.

---

## 💻 How To Run the Applications

### Prerequisites
Make sure you have [Python 3](https://python.org "Python Downloads") installed on your machine.

### Installation
Clone this repository directly using your command line (replace with your actual GitHub username and repo name):
```bash
git clone https://github.com
cd YOUR_REPOSITORY_NAME
```

### Execution
Run either program directly inside your system terminal window:
```bash
# To play the Guessing Game
python guessing_game.py

# To use the Calculator
python calculator.py
```

---
⭐ *Feel free to star this repository if you find my learning journey tracking framework structured and helpful!*
