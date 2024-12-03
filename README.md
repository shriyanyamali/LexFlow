![Maintenance](https://img.shields.io/maintenance/no/2024)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# Setup and Installation Guide

Lexflow is a program that uses user selected principles and determines there effect on an act type. The principle may change a legal conclusion or idea (act type) position on a chart, either moving it towards or against a side. 

## Differences Between lexflow-weighted.py and lexflow-styled.py.ipynb

1. **File Format and Purpose:** <br>

- lexflow-styled.py.ipynb is a Jupyter Notebook that supports interactive code execution, user input, and dynamic visualization. <br>
- lexflow-weighted.py is a Python script for linear execution, without direct support for interactive inputs or step-by-step execution. <br>

2. **User Interaction:** <br>

- lexflow-styled.py.ipynb uses ipywidgets for interactive input, enabling a more dynamic user experience. <br>
- lexflow-weighted.py relies on console-based input (input()), offering less dynamic interaction. <br>

3. **Visualization and Styling:**

- lexflow-styled.py.ipynb uses matplotlib with custom settings for enhanced visual quality. <br>
- lexflow-weighted.py may use matplotlib but focuses on basic, straightforward outputs. <br>

4. **Handling of Weights and Importance of Legal Principles:** <br>

- lexflow-styled.py.ipynb does not handle the relative weights of legal principles. <br>
- lexflow-weighted.py allows input of weights and importance, influencing the program's computations. <br>

5. **Code Structure and Modularity:** <br>

- lexflow-styled.py.ipynb is modular, with code organized into cells for iterative development. <br>
- lexflow-weighted.py is a single script with linear execution, less suited for iterative development. <br>

6. **Use of Libraries:** <br>

- lexflow-styled.py.ipynb uses libraries like ipywidgets for interactivity and enhanced display options. <br>
- lexflow-weighted.py uses standard libraries (matplotlib, numpy) for core functionality. <br>

7. **Intended Use Case:** <br>

- lexflow-styled.py.ipynb is ideal for educational purposes, with interactive features and explanations. <br>
- lexflow-weighted.py is designed for practical applications with straightforward, quick computations. <br>

## Downloading and Installing Python

#### Downloading and installing Python is necessary for both lexflow-weighted.py and lexflow-styled.py.ipynb.

1. **Visit the Python website:** Go to the official Python website at [python.org](https://www.python.org/).
2. **Download Python:** Click on the "Downloads" tab and choose the latest version for Windows. An installer file will download.
3. **Run the Installer:** Open the downloaded installer file.
4. **Customize Installation:** Check the box that says "Add Python to PATH." This is important for running Python from the command line.
5. **Install Python:** Click "Install Now" and follow the prompts to complete the installation.

## lexflow-weighted.py - Continued Setup

1. **Open Command Prompt:** Press `Win + R`, type `cmd`, and press `Enter`.
2. **Run The Following Command To Install The Required Python Packages:** `pip install matplotlib numpy`
3. **Using The Program:** Run the program in the terminal and enter each input as prompted. Do not run the program using Command Prompt or Powershell as the diagram will not be visualized.

## lexflow-styled.ipynb - Continued Setup

1. **Open Command Prompt:** Press `Win + R`, type `cmd`, and press `Enter`.
2. **Run The Following Command To Install Jupyter Notebook:** `pip install notebook`
3. **Run The Following Command To Install The Required Python Packages:** `pip install matplotlib numpy ipywidgets screeninfo`
4. **Run The Following Command To Open Jupyter Notebook:** `jupyter notebook`
5. **Using The Program:** Click on each cell—from top to bottom—and press `Shift` + `Enter` and enter each input as prompted.

This code has been tested with Python 3.12.2. Compatibility with other versions cannot be guaranteed.

Contact me at <a href="https://mail.google.com/mail/?view=cm&fs=1&to=srujanshriyan@gmail.com">srujanshriyan@gmail.com</a>

Check out my website at <a href="https://shriyanyamali.github.io/">https://shriyanyamali.github.io/</a>

This file was last updated on 9/1/2024.

Made by Shriyan Yamali.
