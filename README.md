# Industrial Arm Motion Plotter

This Python code plots the motion of an industrial arm for different cases of movement. It utilizes the NumPy and Matplotlib libraries to calculate and visualize the positions and angles of the loader arm tool.

## Features

- **Elliptical path**: The code can generate an elliptical motion for the loader arm tool, allowing for forward or reverse movement.
- **Horizontal path**: It can also simulate a horizontal motion, where the arm moves in a straight line horizontally.
- **Vertical path**: Additionally, the code supports vertical movement, where the arm moves in a straight line vertically.

## Usage

To use the code, follow these steps:

1. Ensure that you have Python 3.x installed on your system.
2. Install the necessary libraries by running the following command:
pip install numpy matplotlib

3. Open the Python script file (`loader_arm_CAMS.py`) in a text editor or IDE.
4. Adjust the parameters in the script to customize the motion of the industrial arm, such as arm lengths, offsets, and move distances.
5. Uncomment or comment out the relevant sections of code to enable or disable specific cases of movement.
6. Run the script to generate the plots showcasing the arm's motion.

## Validating the Path

The code includes functions to validate the constructed path and ensure that it falls within the working window. These functions check the position and angular parameters against defined constraints and provide feedback on the validity of the path.

## Plots

The script generates several plots to visualize the arm's motion:

- **Path Plot**: This plot shows the x and y coordinates of the arm's position, demonstrating the movement trajectory.
- **X Lengths Plot**: This plot displays the lengths of the imaginary hypotenuse formed by the robot arm throughout the motion.
- **Phi Plot**: This plot represents the angle between the upper and lower arms as the arm moves.
- **Big Theta Plot**: This plot showcases the angle between the upper arm and the ground during the motion.

## Examples

Below are a few examples of how the code can be utilized:

1. Generating an elliptical forward motion for the industrial arm:

```python
x_arr, t_arr = x_ellipse(t, dx, a, n=num, orientation='forward')
y_arr = y_ellipse(t, dy, D, t_arr, orientation='forward')
...

2. Simulating a horizontal motion for the arm:
x_arr, t_arr = x_horiz(t, dx, a, n=num)
y_arr = y_horiz(t, D, t_arr)
...

3. Enabling the vertical motion of the arm:
x_arr, t_arr = x_vert(t, dx, a, n=num, orientation='forward')
y_arr = y_vert(t, D, dy, t_arr, orientation='forward')
...

Feel free to experiment with different parameter values and cases of movement to visualize and analyze the motion of the industrial arm.
