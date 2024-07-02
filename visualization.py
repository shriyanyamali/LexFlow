import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Function to get valid integer input
def get_valid_integer(prompt, min_value=None, max_value=None):
    while True:
        try:
            value = int(input(prompt))
            if (min_value is None or value >= min_value) and (max_value is None or value <= max_value):
                return value
            else:
                print(f"Please enter a value between {min_value} and {max_value}.")
        except ValueError:
            print("Please enter a valid integer.")

# Function to get valid float input within a specified range
def get_valid_float(prompt, min_value, max_value):
    while True:
        try:
            value = float(input(prompt))
            if min_value <= value <= max_value:
                return value
            else:
                print(f"Please enter a value between {min_value} and {max_value}.")
        except ValueError:
            print(f"Please enter a valid number between {min_value} and {max_value}.")

# Function to get valid string input from a list of options
def get_valid_option(prompt, options):
    while True:
        value = input(prompt).lower()
        if value in options:
            return value
        else:
            print(f"Please enter one of the following: {', '.join(options)}")

# Function to calculate area of an arrow
def calculate_arrow_area(width, height):
    return width * height

# Main function to create the diagram
def create_diagram():
    # Getting user inputs
    act_type = input("Enter the Act-type: ")
    num_principles = get_valid_integer("Enter the number of principles: ", 1)

    arrows = []
    total_prohibited_area = 0
    total_not_prohibited_area = 0

    for i in range(num_principles):
        principle_name = input(f"Enter the name of principle {i+1}: ")
        legal_status = get_valid_option(f"Enter the legal status of principle {i+1} (prohibited/invalid/not immune/not prohibited/valid/immune): ",
                                        ["prohibited", "invalid", "not immune", "not prohibited", "valid", "immune"])
        relative_importance = get_valid_float(f"Enter the relative importance of principle {i+1} (0.5-3.0): ", 0.5, 3.0)
        activation_percentage = get_valid_integer(f"Enter the percentage of activation of principle {i+1} (0-100): ", 0, 100)

        width = relative_importance * 3  # Scaling up the arrow width
        height = activation_percentage / 100 * 30  # Scaling up the arrow height

        arrow = {
            "name": principle_name,
            "status": legal_status,
            "width": width,
            "height": height
        }

        if legal_status in ["prohibited", "invalid", "not immune"]:
            total_prohibited_area += calculate_arrow_area(width, height)
        else:
            total_not_prohibited_area += calculate_arrow_area(width, height)

        arrows.append(arrow)

    # Calculating the position of the circle
    position_shift = total_not_prohibited_area - total_prohibited_area

    # Plotting the diagram
    fig, ax = plt.subplots(figsize=(10, 10))  # Smaller window size

    # Drawing the T table structure
    ax.plot([-100, 100], [60, 60], color='black', linewidth=1)  # Moved x-axis further up
    ax.plot([0, 0], [-100, 100], color='black', linewidth=1)
    ax.text(-50, 90, 'Not Prohibited', fontsize=16, va='center', ha='center')
    ax.text(50, 90, 'Prohibited', fontsize=16, va='center', ha='center')

    # Drawing the circle
    circle_radius = 5
    circle = patches.Circle((position_shift, 40), circle_radius, edgecolor='black', facecolor='grey')
    ax.add_patch(circle)
    ax.text(position_shift, 40, act_type, fontsize=12, va='center', ha='center')

    # Drawing the arrows
    y_offset = 55  # Starting close to the new x-axis position and moving down
    for i, arrow in enumerate(arrows):
        if arrow['status'] in ["prohibited", "invalid", "not immune"]:
            x_start = -95
            x_end = x_start + arrow['height']
        else:
            x_start = 95
            x_end = x_start - arrow['height']
        
        y_position = y_offset - i * 12  # Increasing the distance between arrows

        if abs(position_shift - x_start) < circle_radius:
            y_position -= 5  # Adjust y position to avoid overlap

        ax.arrow(x_start, y_position, x_end - x_start, 0, head_width=3, head_length=3, fc='blue', ec='blue', width=arrow['width']/10)
        ax.text((x_start + x_end) / 2, y_position, arrow['name'], fontsize=12, va='center', ha='center')

    ax.set_xlim(-100, 100)
    ax.set_ylim(-100, 100)
    ax.set_aspect('equal', 'box')
    ax.axis('off')

    plt.show()

# Run the function
create_diagram()
