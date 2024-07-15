import matplotlib.pyplot as plt
import numpy as np

def get_user_input():
    # Prompt user to enter the Act-type
    act_type = input("Enter the Act-type: ")
    
    # Prompt user to enter heading 1
    heading1 = input("Enter heading 1: ")
    
    while True:
        # Prompt user to enter heading 2
        heading2 = input("Enter heading 2: ")
        if heading2 == heading1:
            # Ensure heading 2 is not the same as heading 1
            print("The headings cannot be the same. Please enter different text for heading 2.")
        else:
            break
    
    principles = []  # List to store principles
    
    while True:
        # Prompt user to enter the name of the principle
        name = input(f"Enter the name of the principle: ")
        
        while True:
            # Prompt user to enter the legal status of the principle
            legal_status = input(f"Enter the legal status of the principle (either '{heading1}' or '{heading2}'): ")
            if legal_status in [heading1, heading2]:
                break
            else:
                # Ensure the legal status is either heading 1 or heading 2
                print(f"Please enter either '{heading1}' or '{heading2}'.")
        
        while True:
            try:
                # Prompt user to enter the relative importance of the principle
                importance = float(input(f"Enter the relative importance of the principle: "))
                break
            except ValueError:
                # Ensure the importance is a valid number
                print("Please enter a valid number.")
        
        while True:
            try:
                # Prompt user to enter the percentage of activation of the principle
                activation = float(input(f"Enter the percentage of activation of the principle (0-100): "))
                if 0 <= activation <= 100:
                    break
                else:
                    # Ensure the activation is a number between 0 and 100
                    print("Please enter a number between 0 and 100.")
            except ValueError:
                # Ensure the activation is a valid number
                print("Please enter a valid number.")
        
        # Append the principle details to the list
        principles.append({
            'name': name,
            'legal_status': legal_status,
            'importance': importance,
            'activation': activation
        })
        
        # Ask if the user wants to add another principle
        another = input("Would you like to add another principle (yes or no)? ").strip().lower()
        if another != 'yes':
            break
    
    # Return the collected user inputs
    return act_type, heading1, heading2, principles

def calculate_area(importance, activation):
    width = 0.04 * importance  # Width of the arrow shaft based on importance
    length = 0.55 * activation / 100  # Length of the arrow shaft based on activation percentage
    shaft_area = width * length  # Area of the arrow shaft
    
    head_width = width * 1.8  # Width of the arrow head slightly wider than the shaft
    head_length = 0.02  # Length of the arrow head
    head_area = 0.5 * head_width * head_length  # Area of the arrow head
    
    total_area = shaft_area + head_area  # Total area of the arrow (shaft + head)
    return total_area, width, length, head_width  # Return total area, width, length, and head_width

def calculate_y_positions(n):
    y_positions = [0.5]  # Start at the center
    step = 0.2  # Step size for vertical positioning

    for i in range(1, n):
        if i % 2 == 1:
            y_positions.append(0.5 + (i // 2 + 1) * step)  # Above the center
        else:
            y_positions.append(0.5 - (i // 2) * step)  # Below the center

    return y_positions

def create_diagram(act_type, heading1, heading2, principles):
    fig, ax = plt.subplots(figsize=(12, 8))  # Create a new figure
    
    # Draw the headings on the left and right
    ax.text(-0.5, 1.1, heading1, fontsize=14, ha='center')
    ax.text(0.5, 1.1, heading2, fontsize=14, ha='center')
    
    # Draw the vertical line in the center
    ax.plot([0, 0], [0, 1], color='black', linewidth=1)
    
    left_area = 0  # Initialize total area for arrows pointing left
    right_area = 0  # Initialize total area for arrows pointing right
    
    left_principles = [p for p in principles if p['legal_status'] == heading1]
    right_principles = [p for p in principles if p['legal_status'] == heading2]
    
    left_y_positions = calculate_y_positions(len(left_principles))
    right_y_positions = calculate_y_positions(len(right_principles))
    
    for principle in principles:
        # Calculate the area of each principle
        area, width, length, head_width = calculate_area(principle['importance'], principle['activation'])
        if principle['legal_status'] == heading1:
            left_area += area  # Sum areas for left-pointing arrows
        else:
            right_area += area  # Sum areas for right-pointing arrows
    
    # Calculate the position of the circle based on total areas
    position = (right_area - left_area) / max(left_area + right_area, 1)
    
    # Draw the circle at the calculated position with increased size
    circle = plt.Circle((position, 0.5), 0.14, color='blue', fill=True)  # Circle radius increased by 1.5 times (0.05 * 1.5 = 0.075)
    ax.add_artist(circle)
    ax.text(position, 0.5, act_type, fontsize=12, ha='center', va='center', color='white')
    
    offset = 0.3  # Define an offset value to move arrows further left or right
    
    for i, principle in enumerate(left_principles):
        area, width, length, head_width = calculate_area(principle['importance'], principle['activation'])  # Unpack width, length, and head_width
        y_position = left_y_positions[i]
        # Draw left-pointing arrows with offset adjustment
        start_x = -length - offset  # Move arrow further left by offset
        ax.arrow(start_x, y_position, length, 0, width=width, head_width=head_width, head_length=0.02, fc='blue', ec='blue')
        ax.text(start_x + length / 2, y_position + width, principle['name'], fontsize=10, ha='center')
    
    for i, principle in enumerate(right_principles):
        area, width, length, head_width = calculate_area(principle['importance'], principle['activation'])  # Unpack width, length, and head_width
        y_position = right_y_positions[i]
        # Draw right-pointing arrows with offset adjustment
        start_x = length + offset  # Move arrow further right by offset
        ax.arrow(start_x, y_position, -length, 0, width=width, head_width=head_width, head_length=0.02, fc='blue', ec='blue')
        ax.text(start_x - length / 2, y_position + width, principle['name'], fontsize=10, ha='center')
    
    ax.set_xlim(-1, 1)  # Set x-axis limits
    ax.set_ylim(0, 1)  # Set y-axis limits
    ax.set_aspect('equal')  # Ensure the aspect ratio is equal to make the circle round
    ax.axis('off')  # Hide axes
    plt.show()  # Display the plot

if __name__ == "__main__":
    # Get user inputs
    act_type, heading1, heading2, principles = get_user_input()
    # Create and display the diagram
    create_diagram(act_type, heading1, heading2, principles)
