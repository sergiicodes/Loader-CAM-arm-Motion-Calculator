#loader_arm_CAMS
#NOTE - here y is the vertical axis 
#here I have plotted the motion for the industrial arm for several cases of movement  

import numpy as np
import matplotlib.pyplot as plt

'''
UP / FORWARD MOVES
I think, THINK!!, that inverting t_arr will make the move reversed
'''


def x_ellipse(t,dx,a,n=10,orientation='forward'):
    '''
    Returns x positions for path of loader arm tool
    t - time of move
    dx - horizontal distance
    n - number of points for curve
    elliptic path, x coords
    
    
    '''
    k = np.pi/t
    t_arr = np.linspace(0,t,num=n)
    if orientation == 'forward':
        return dx/2 * np.cos(np.pi-k*t_arr)+a, t_arr
    else:
        return dx/2 * np.cos(k*t_arr)+a, t_arr 

def y_ellipse(t,dy,D,t_arr,orientation='forward'):
    '''
    Returns y positions for path of loader arm tool
    t - time of move
    dy - vertical distance
    n - number of points for curve
    elliptic path, y coords
    
    '''
    k = np.pi/t
    if orientation == 'forward':
        return dy * np.sin(k*t_arr) + D
    else:
        return dy * np.sin(np.pi - k*t_arr) + D

def x_horiz(t,dx,a,n=10,orientation='forward'):
    '''
    Returns x positions for path of loader arm tool
    t - time of move
    dx - horizontal distance
    n - number of points for curve
    horizontal path, x coords
    
    
    '''
    k = dx/t
    t_arr = np.linspace(0,t,num=n)
    if orientation == 'forward':
        return k*t_arr - a, t_arr
    else:
        return -k*t_arr - a, t_arr

def y_horiz(t,D,t_arr,orientation='forward'):
    '''
    Returns y positions for path of loader arm tool
    t - time of move
    dy - vertical distance
    n - number of points for curve
    horizontal path, y coords
    
    '''
    y = np.ones_like(t_arr)
    return D*y

def x_vert(t,dx,a,n=10,orientation='forward'):
    '''
    Returns x positions for path of loader arm tool
    t - time of move
    dx - horizontal distance
    n - number of points for curve
    vertical path, x coords
    
    
    '''
    t_arr = np.linspace(0,t,num=n)
    x = np.ones_like(t_arr)
    return a*x, t_arr

def y_vert(t,D,dy,t_arr,orientation='forward'):
    '''
    Returns y positions for path of loader arm tool
    t - time of move
    dy - vertical distance
    n - number of points for curve
    vertical path, y coords
    
    '''
    k = dy/t
    if orientation == 'forward':
        return k*t_arr + D
    else:
        return D - k*t_arr

def X(x,y):
    '''

    Parameters
    ----------
    x - horizontal move distance at a given point(s) in space
    array
    y - vertical move distance at a given point(s) in space
    array
    a - horizontal offset, real
    b - vertical offset, real

    Returns
    -------
    array of lengths of imaginary hypotenuse robot arms form

    '''
    return np.sqrt((x)**2 + (y)**2)


def phi(X,L1,L2):
    '''
    X - lengths of hyp. of robot arm triangle
    L1 - Upper arm length
    L2 - lower arm length
    returns angles btw upper and lower arm throughout motion
    
    FOR CAM - array of angles for J2 (elbow joint) CAM
    Note, must first be converted from radians to degrees
    '''
    top = L1**2 + L2**2 - X**2
    bot = 2*L1*L2
    return np.arccos(top/bot)

def theta(X,L2,phi):
    '''
    X - lengths of hyp. of robot arm triangle
    phi - angle btw upper and lower arm
    L2 - lower arm length
    returns angle btw upper arm and hypotenuese
    '''
    return np.arcsin(L2/X * np.sin(phi))

def Big_theta(theta,x,bigX):
    '''
    theta - angle btw upper arm and hypotenuese
    x - horizontal move distance at a given point(s) in space
    array
    bigX - lengths of imaginary hypotenuse robot arms form
    returns angles between upper arm and ground
    
    FOR CAM - array of angles for J1 (shoulder joint) CAM
    '''
    return np.pi - theta - np.arccos(x/bigX)

def Working_Window_Check(x,y):
    '''
    Ensures that the constructed path is within the working window

    Parameters
    ----------
    x : array of x values for move
    y : array of y values for move

    Returns
    -------
    Valid path if valid, invalid path if invalid. gives info about
    what parameter is out of range.

    '''
    test = True
    for i in range(len(x)):
        if y[i] > -16 or y[i] < -40.8:
            test = False
            print('y out of range')
        elif x[i] < -25.26 or x[i] > 39.17:
            test = False
            print('x out of range')
        elif (y[i] < -42.8 and (x[i]>23.6 or x[i]<-14.4)):
            test = False
            print('x and y out of range')
        elif x[i] > 31.17 and y[i] < -34.8:
            test = False
            print('x and y out of range')
    if test:
        print("Valid Path")
    else:
        print("Invalid Path")

def Working_Window_Angular(theta,phi):
    '''
    Ensures that the constructed path is within the working window

    Parameters
    ----------
    x : array of x values for move
    y : array of y values for move

    Returns
    -------
    Valid path if valid, invalid path if invalid. gives info about
    what parameter is out of range.

    '''
    test = True
    for i in range(len(theta)):
        if theta[i] > 120 or theta[i] < 0:
            test = False
            print('a')
        elif phi[i] > 130 or phi[i] < 50:
            test = False
            print('b')
        elif theta[i]>65 and phi[i]<60:
            test = False
            print('c')
    if test:
        print("Valid Path")
    else:
        print("Invalid Path")



            
#Constraints
# Upper arm length
L1 = 20
# Lower arm length
L2 = 20
# x offset for move
a = 12.4
# y offset for move
D = -25.63
# horizontal move distance
dx = 20
# vertical move distance
dy = 6
# arbitrary unit, time, master degrees etc.
t = 360
# number of CAM points
num = 30
'''
## Creates a CAM following an ellipse
# Computes x coordinates and master positions
x_arr,t_arr = x_ellipse(t,dx,a,n=num,orientation='forward')
# Computes y coordinates
y_arr = y_ellipse(t,dy,D,t_arr,orientation='forward')
#Calculates distance from tool to shoulder joint
X_vals = X(x_arr,y_arr)
# Computes angle between the arms
phi_arr = phi(X_vals,L1,L2)
# Computes angle between upper arm and imaginary line
# between shoulder joint and tool
theta_arr = theta(X_vals,L2,phi_arr)
# Computes angle between upper arm and floor
Theta = Big_theta(theta_arr,x_arr,X_vals)*180/np.pi


'''

x_arr,t_arr = x_horiz(t,dx,a,n=num)
y_arr = y_horiz(t,D,t_arr)
X_vals = X(x_arr,y_arr)
phi_arr = phi(X_vals,L1,L2)
theta_arr = theta(X_vals,L2,phi_arr)
Theta = Big_theta(theta_arr,x_arr,X_vals)*180/np.pi

'''
x_arr,t_arr = x_vert(t,dx,a,n=num)
y_arr = y_vert(t,D,dy,t_arr,orientation='downj')
X_vals = X(x_arr,y_arr)
phi_arr = phi(X_vals,L1,L2)
theta_arr = theta(X_vals,L2,phi_arr)
Theta = Big_theta(theta_arr,x_arr,X_vals)*180/np.pi
'''

# Checks to ensure a valid path has been created
Working_Window_Check(x_arr,y_arr)
# Covnerts angle between the arms to degrees
Phi = phi_arr*180/np.pi
Working_Window_Angular(Theta,Phi)
# Plots
plt.plot(x_arr,y_arr)
plt.xlabel('x')
plt.ylabel('y')
plt.title('path')
plt.grid(True)
plt.show() 

plt.plot(t_arr,X_vals,'m')
#plt.plot(x_arr-a,X_vals+dy)
plt.xlabel('time (s)')
plt.ylabel('X')
plt.title('X lengths')
plt.grid(True)
plt.show() 

plt.plot(t_arr,Phi,'r-')
#plt.plot(x_arr-a,X_vals+dy)
plt.xlabel('time (s)')
plt.ylabel('phi')
plt.title('Angle phi')
plt.grid(True)
plt.show() 

'''
plt.plot(t_arr,theta_arr*180/np.pi,'g-')
#plt.plot(x_arr-a,X_vals+dy)
plt.xlabel('time (s)')
plt.ylabel('theta')
plt.title('Angle theta')
plt.show() 
'''

plt.plot(t_arr,Theta,'g-')
#plt.plot(x_arr-a,X_vals+dy)
plt.xlabel('time (s)')
plt.ylabel('Theta')
plt.title('Big Theta')
plt.grid(True)
plt.show() 