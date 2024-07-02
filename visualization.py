import matplotlib.pyplot as plt

def draw_diagram(principles, topic):
    fig, ax = plt.subplots(figsize=(12, 8))
    
    max_length = 0.3
    unit_height = 0.1
    
    ax.plot([0.5, 0.5], [0, 1], color='black', linewidth=1)
    ax.plot([0, 1], [0.9, 0.9], color='black', linewidth=1)
    
    total_force_not_prohibited = 0
    total_force_prohibited = 0
    
    y_positions = []
    y_step = 0.1
    base_y = 0.85

    for idx, principle in enumerate(principles):
        name, direction, weight, activation = principle
        length = max_length * activation
        height = unit_height * weight
        y = base_y - (y_step * idx)
        y_positions.append(y)
        
        if direction.lower() == 'not prohibited':
            x = 0.75  # Start from the right side
            dx = -length  # Point towards the center
        else:
            x = 0.25  # Start from the left side
            dx = length  # Point towards the center

        ax.arrow(x, y, dx, 0, head_width=height, head_length=0.05, fc='blue', ec='blue', length_includes_head=True, width=height/2)
        ax.text(x + dx / 2, y, name, fontsize=10, ha='center', va='center', color='white')
        
        if direction.lower() == 'not prohibited':
            total_force_not_prohibited += length * height
        else:
            total_force_prohibited += length * height

    net_force = total_force_not_prohibited - total_force_prohibited
    circle_x = 0.5 + (net_force / (2 * max_length))
    circle_y = (max(y_positions) + min(y_positions)) / 2

    # Adjust circle_x to prevent it from overlapping with any arrows
    for _, direction, _, activation in principles:
        length = max_length * activation
        if direction.lower() == 'not prohibited' and abs(circle_x - (0.75 - length)) < 0.05:
            circle_x -= 0.05
        elif direction.lower() == 'prohibited' and abs(circle_x - (0.25 + length)) < 0.05:
            circle_x += 0.05

    # Makes sure that the circle is inbetween the arrows
    if circle_x < 0.3:
        circle_x = 0.3
    if circle_x > 0.7:
        circle_x = 0.7

    circle = plt.Circle((circle_x, circle_y), 0.05, color='gray')
    ax.add_patch(circle)
    ax.text(circle_x, circle_y, topic, fontsize=14, ha='center', va='center', color='white')

    ax.text(0.25, 0.95, 'Not Prohibited', fontsize=12, ha='center')
    ax.text(0.75, 0.95, 'Prohibited', fontsize=12, ha='center')

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    plt.show()

def get_valid_input(prompt, valid_options):
    while True:
        value = input(prompt).strip().lower()
        if value in [opt.lower() for opt in valid_options]:
            return value
        print(f"Invalid input. Please enter one of the following: {', '.join(valid_options)}")

def get_valid_float(prompt, min_value=None, max_value=None):
    while True:
        try:
            value = float(input(prompt))
            if (min_value is None or value >= min_value) and (max_value is None or value <= max_value):
                return value
            if min_value is not None and max_value is not None:
                print(f"Invalid input. Please enter a value between {min_value} and {max_value}.")
            elif min_value is not None:
                print(f"Invalid input. Please enter a value greater than or equal to {min_value}.")
            elif max_value is not None:
                print(f"Invalid input. Please enter a value less than or equal to {max_value}.")
        except ValueError:
            print("Invalid input. Please enter a numerical value.")

def get_valid_int(prompt, min_value=None):
    while True:
        try:
            value = int(input(prompt))
            if min_value is None or value >= min_value:
                return value
            print(f"Invalid input. Please enter an integer greater than or equal to {min_value}.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

def get_user_input():
    principles = []
    topic = input("Enter the topic: ")
    n = get_valid_int("Enter the number of principles: ", min_value=1)
    for _ in range(n):
        name = input("Enter the name of the principle: ")
        direction = get_valid_input("Enter the direction (Prohibited or Not Prohibited): ", ["Prohibited", "Not Prohibited"])
        weight = get_valid_float("Enter the relative weight: ")
        activation = get_valid_float("Enter the percentage of activation (0 to 1): ", 0.0, 1.0)
        principles.append((name, direction.capitalize(), weight, activation))
    return principles, topic

principles, topic = get_user_input()
draw_diagram(principles, topic)
 