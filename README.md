# Sudoku Solver with Selenium

![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)  
![Selenium](https://img.shields.io/badge/selenium-v3.141.0-green.svg)  
![License](https://img.shields.io/badge/license-MIT-blue.svg)

A powerful Sudoku solver built with Selenium. This tool automates the process of solving Sudoku puzzles directly on a webpage. It extracts the grid from the webpage, solves it using an efficient backtracking algorithm, and inputs the solution back into the webpage.

---

## 🚀 Features

- **Automated Grid Extraction**: Reads the Sudoku grid directly from the webpage.
- **Efficient Solving Algorithm**: Utilizes a backtracking algorithm to solve puzzles quickly.
- **Seamless Web Interaction**: Automatically fills the solved grid back into the webpage.

---

## 📋 Prerequisites

- Python 3.x
- Selenium
- ChromeDriver

---

## 🛠️ Installation

1. **Clone the repository**:  
    ```bash
    git clone https://github.com/yourusername/sudoku-solver.git
    cd sudoku-solver
    ```

2. **Install dependencies**:  
    ```bash
    pip install selenium
    ```

3. **Set up ChromeDriver**:  
   - Download ChromeDriver from [Google Chrome Labs](https://googlechromelabs.github.io/chrome-for-testing/).  
   - Place the `chromedriver` executable in the project directory. Ensure it is in the same location as your Python script.

---

## 📖 Usage

1. Open the script and confirm that the `executable_path` in the `Service` object points to your `chromedriver` file.

2. Run the script:  
    ```bash
    python sudoku.py
    ```

3. Watch as the script:
   - Launches a browser.
   - Navigates to the Sudoku puzzle webpage.
   - Extracts, solves, and fills in the solution.

---

## 🧠 How It Works

1. **Extract the Sudoku Grid**: Reads the grid structure from the webpage.  
2. **Solve the Sudoku**: Implements a backtracking algorithm to compute the solution.  
3. **Fill the Sudoku Grid**: Inputs the solved values back into the webpage.  

---

## 🤝 Contributing

Contributions are always welcome! If you have suggestions, encounter issues, or want to enhance the project, feel free to:  
- Open an issue  
- Submit a pull request  

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.



![Vidéo sans titre ‐ Réalisée avec Clipchamp (2)](https://github.com/user-attachments/assets/1d4855b4-c2e7-4fca-a820-ce26a998b47c)
