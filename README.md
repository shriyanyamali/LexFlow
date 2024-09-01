 ![Maintenance](https://img.shields.io/maintenance/no/2024)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# Setup and Installation Guide

## Differences Between `lexflow-weighted.py` and `lexflow-styled.py.ipynb`
1. File Format and Purpose
lexflow-styled.py.ipynb is a Jupyter Notebook file, which provides an interactive environment combining code, text, and multimedia. It allows for step-by-step execution of code cells, user inputs, and dynamic visualization.
lexflow-weighted.py is a standard Python script file meant for linear execution of code. It does not support interactive user inputs directly or allow step-by-step execution like a Jupyter Notebook.
2. User Interaction
lexflow-styled.py.ipynb contains code for user input through Python's input() function and uses widgets (such as sliders, buttons, etc.) for more interactive input via ipywidgets. The notebook uses interact and interact_manual to create a dynamic and user-friendly experience.
lexflow-weighted.py also accepts user input but relies solely on console-based input methods using input(). The interaction is less dynamic and is confined to a terminal or command-line environment.
3. Visualization and Styling
lexflow-styled.py.ipynb uses matplotlib for creating plots and diagrams, potentially with additional customization or styling options. It includes settings to adjust figure properties, such as mpl.rcParams['figure.dpi'] = 300, to enhance visual quality.
lexflow-weighted.py may also use matplotlib for plotting, but it appears to focus less on styling and visual presentation, producing basic outputs.
4. Handling of Weights and Importance of Legal Principles
lexflow-styled.py.ipynb does not explicitly handle the relative weights or importance of legal principles. It focuses on inputting contrasting legal statuses and acts but lacks functionality to manipulate their relative importance.
lexflow-weighted.py allows users to input the relative weight and importance of legal principles. This feature is likely implemented through functions or methods that capture these weights for computations or visualizations.
5. Code Structure and Modularity
lexflow-styled.py.ipynb is structured in cells, which promotes modularity and iterative development. Each cell can be executed independently, making it useful for debugging and incremental changes. It may also include rich text annotations, explanations, and instructions.
lexflow-weighted.py is likely organized as a single script where all code executes in a predefined order. The structure is linear and less flexible for iterative development compared to the notebook format.
6. Use of Libraries
lexflow-styled.py.ipynb utilizes additional libraries like ipywidgets for interactive widgets and possibly textwrap and screeninfo to manage text formatting and display properties, which are suited for a notebook setting.
lexflow-weighted.py primarily uses standard libraries like matplotlib and numpy without additional interactive libraries, focusing on core functionality.
7. Intended Use Case
lexflow-styled.py.ipynb is designed for an educational or demonstration setting where user interaction, visual clarity, and step-by-step explanations are crucial.
lexflow-weighted.py is intended for a more practical, programmatic application where users may want to compute outcomes quickly based on inputs without interactive explanations.


## Downloading and Installing Python
### This is necessary for both lexflow-weighted.py and lexflow-styled.py.ipynb.
1. **Visit the Python website:** Go to the official Python website at [python.org](https://www.python.org/).
2. **Download Python:** Click on the "Downloads" tab and choose the latest version for Windows. An installer file will download.
3. **Run the Installer:** Open the downloaded installer file.
4. **Customize Installation:** Check the box that says "Add Python to PATH." This is important for running Python from the command line.
5. **Install Python:** Click "Install Now" and follow the prompts to complete the installation.

## Weighted - Continued Setup
1. **Open Command Prompt:** Press `Win + R`, type `cmd`, and press `Enter`.
2. **Run The Following Command To Install The Required Python Packages:** `pip install matplotlib numpy`
3. **Using The Program:** Run the program in the terminal and enter each input as prompted. Do not run the program using Command Prompt or Powershell as the diagram will not be visualized. 

## Styled - Continued Setup
1. **Open Command Prompt:** Press `Win + R`, type `cmd`, and press `Enter`.
2. **Run The Following Command To Install Jupyter Notebook:** `pip install notebook`
3. **Run The Following Command To Install The Required Python Packages:** `pip install matplotlib numpy ipywidgets screeninfo`
4. **Run The Following Command To Open Jupyter Notebook:** `jupyter notebook`
5. **Using The Progam:** Click on each cell—from top to bottom—and press `Shift` + `Enter` and enter each input as prompted.

#### Made by Shriyan Yamali. 
#### A program that creates diagrams based on the relative weight and importance of legal principles and the effect of the principles on an act type.

Contact me at <a href="https://mail.google.com/mail/?view=cm&fs=1&to=srujanshriyan@gmail.com">srujanshriyan@gmail.com</a> or visit my website at <a href="https://shriyanyamali.github.io/">https://shriyanyamali.github.io/</a>

This file was last updated on 8/22/2024.

Copyright © 2024 Shriyan Yamali All rights reserved.
