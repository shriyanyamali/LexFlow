![Maintenance](https://img.shields.io/maintenance/no/2025)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

NOTICE:

May 2025

Starting this year, I will not be updating this repository. I might make sporadic updates to the README file but the Python code will not be updated.

# Setup and Installation Guide

Lexflow is a program that uses user-selected principles and determines their effect on an act type. The principle may change a legal conclusion or idea (act type) position on a chart, either moving it towards or against a side.

## Example Output

![Image failed to load](https://www.shriyanyamali.tech/projects/lexflow.png)

Here, we see that the act type (religious freedoms) is more not prohibited than prohibited based on the provided principles (secularism, first amendment, etc.). The larger the width of the arrow (compare Church-State to pluralism), the greater the weight (impact). Those values are user-inputted, and then calculated using a formula to determine the relative weight compared to the other principles. This moves the act type accordingly to represent the relative change based on the cause-and-effect relationship between the act type and each principle. This specific example shows that religious freedoms are "not prohibited" or in this context, preserved, after deducting the negative implications of a lack of separation of church and state and secularism from the freedoms provided through the first amendment and promoted through pluralism.

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

Questions? Contact me at <a href="https://mail.google.com/mail/?view=cm&fs=1&to=yamalishriyan@gmail.com">yamalishriyan@gmail.com</a>

Check out my website at <a href="https://shriyanyamali.github.io/">https://shriyanyamali.github.io/</a>

This file was last updated on 7/7/2025.

Made by Shriyan Yamali.
