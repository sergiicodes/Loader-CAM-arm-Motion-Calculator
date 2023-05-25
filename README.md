# Industrial Arm Motion Plotter

This is one of the projects I am currently working on as an R&D Engineer for a manufacturing company. The Python code presented here is specifically designed to track the motion of a robotic arm called a loader. The loader's main function is to push packaged products into cardboard cases. 

The Industrial Arm Motion Plotter was developed to analyze and visualize the loader arm's position and motion. By using this Python program, other engineers, including controls and electrical engineers, in the department can gain a better understanding of the loader's movements. 

The code utilizes the NumPy and Matplotlib libraries to calculate and plot the positions and angles of the loader arm tool. It supports various types of motion, including elliptical, horizontal, and vertical paths. Additionally, it includes functions to validate the constructed path and ensure it falls within the working window.

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
```

2. Simulating a horizontal motion for the arm:
```python
x_arr, t_arr = x_horiz(t, dx, a, n=num)
y_arr = y_horiz(t, D, t_arr)
```

3. Enabling the vertical motion of the arm:
```python
x_arr, t_arr = x_vert(t, dx, a, n=num, orientation='forward')
y_arr = y_vert(t, D, dy, t_arr, orientation='forward')
```


Feel free to experiment with different parameter values and cases of movement to visualize and analyze the motion of the industrial arm.


## CAD Models of Robotic Arm
![Picture9](https://github.com/sergiicodes/Loader-CAM-arm-Motion-Calculator/assets/79073281/6449165b-ed15-4945-8936-4d21d54d3e63)

![Picture7](https://github.com/sergiicodes/Loader-CAM-arm-Motion-Calculator/assets/79073281/764bbdc6-7c45-4ebf-8bf3-3a861ab6839a)

![Picture6](https://github.com/sergiicodes/Loader-CAM-arm-Motion-Calculator/assets/79073281/c3bf92f4-de9f-413e-970c-604c1244b3d3)

![Picture4](https://github.com/sergiicodes/Loader-CAM-arm-Motion-Calculator/assets/79073281/1394b009-a0b4-4861-a345-64b6508d7c1d)

![Picture3](https://github.com/sergiicodes/Loader-CAM-arm-Motion-Calculator/assets/79073281/2fc90867-03bf-4885-9b4e-ac6c8dbecb5c)

![Picture10](https://github.com/sergiicodes/Loader-CAM-arm-Motion-Calculator/assets/79073281/3ed13b3e-46b1-4586-b499-554f7792cbf3)
