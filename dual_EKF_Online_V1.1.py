"""

Dual Extended kalman filter (EKF) for vehicle state & parameter estimation

Example Model 1: Diffential-drive forward kinematic model

author: weichang.xu

The methodology is based on the paper:

"T. A. Wenzel , K. J. Burnham , M. V. Blundell & R. A. Williams (2006) 
Dual extended Kalman filter for vehicle state and parameter estimation"

Link this paper: https://doi.org/10.1080/00423110500385949

Online param estimation

"""

import numpy as np
import math
import matplotlib.pyplot as plt

"""
state vector in this model:

Xs = [x, y , theta]': the robot state vector
Xp = [r, L]': the robot unknown parameter vector
u = [phi1, phi2]': the control vector
z = [x, y]': the output vector

x: global coordinate x-value of the original point P of the robot body reference frame [m]
y: global coordinate y-value of the original point P of the robot body reference frame [m]
theta: the angular difference between the global and robot body reference frames [rad]

L: The distance for each wheel to the centre point P [m]
r: The diameter of the wheel [m]
phi1,2: The spinning speed of wheel 1,2 [rad/s]
"""

# Estimation parameter of EKF
Qs = np.diag([0.1, 0.1, math.radians(1.0)])**2 # State estimatior process noise covariance
Rs = np.diag([0.1, 0.1])**2 # State estimator measurement noise covariance

Qp = np.diag([0.04, 0.02])**2 # Parameter estimatior process noise covariance
Rp = np.diag([0.1, 0.1])**2 # Parameter estimatior measurement noise covariance

#  Simulation parameter
Qsim = np.diag([0.2, 0.2])**2 ## Add noise to measurement raw data
Rsim = np.diag([math.radians(30.0), math.radians(30.0)])**2 ## Add noise to control inputs
DT = 0.1  # time tick [s] 
SIM_TIME = 50.0  # simulation time [s]

# Real kinematic parameter of the mobile robot
L = 2 # [m]
r = 4 # [m]
ratio = r/(2 * L) # r/2L

# Unknown kinematic parameters' initial guess
L0 = 1.7 # [m]
r0 = 3.7 # [m]

# data visualization flag
show_animation = 1
show_graph = 0

def calc_input():

    phi_1 = 1.0 # [rad/s] 
    phi_2 = 1.0 # [rad/s] 
    u = np.matrix([phi_1, phi_2]).T 
    return u

def observation(Xs_True, u):
    """
    Observation sensor:
    
    GPS: x-y value
    """

    # add noise to gps x-y & gyro sensor theta
    zx = Xs_True[0, 0] + np.random.randn() * Qsim[0, 0]  
    zy = Xs_True[1, 0] + np.random.randn() * Qsim[1, 1]
    z = np.matrix([zx, zy])

    
    # add noise to input
    ud1 = u[0, 0] + np.random.randn() * Rsim[0, 0]
    ud2 = u[1, 0] + np.random.randn() * Rsim[1, 1]
    ud = np.matrix([ud1, ud2]).T

    Xs_True = motion_model(Xs_True, ud)
    
    return Xs_True, z, ud

def motion_model(x, u):
    """
    motion model
    x_{t+1} = x_t + r * (phi_1 + phi_2) * DT * cos(theta) / 2L
    y_{t+1} = y_t + r * (phi_1 + phi_2) * DT * sin(theta) / 2L
    theta_{t+1} = theta_t + r * (phi_1 - phi_2) * DT / 2L
    """
    F = np.eye(3)

    B = np.matrix([[DT * math.cos(x[2, 0]) * ratio, DT * math.cos(x[2, 0]) * ratio],
                   [DT * math.sin(x[2, 0]) * ratio, DT * math.sin(x[2, 0]) * ratio],
                   [DT * ratio, -DT * ratio],
                   ])

    x = F * x + B * u

    return x

def state_predict_motion_model(Xs_Est, u, Xp_Pred):
    """
    motion model
    x_{t+1} = x_t + r * (phi_1 + phi_2) * DT * cos(theta) / 2L
    y_{t+1} = y_t + r * (phi_1 + phi_2) * DT * sin(theta) / 2L
    theta_{t+1} = theta_t + r * (phi_1 - phi_2) * DT / 2L
    """
    theta = Xs_Est[2, 0] # [rad]
    r = Xp_Pred[0, 0] # [m]
    L = Xp_Pred[1, 0] # [m]
    ratio = r/(2 * L) # r/2L

    F = np.eye(3)

    B = np.matrix([[DT * math.cos(theta) * ratio, DT * math.cos(theta) * ratio],
               [DT * math.sin(theta) * ratio, DT * math.sin(theta) * ratio],
               [DT * ratio, -DT * ratio],
               ])
    Xs_Pred = F * Xs_Est + B * u

    return Xs_Pred

def param_model(Xp_Est):

    return Xp_Est

def observation_model(x):
    #  Observation Model
    H = np.matrix([
        [1.0, 0.0, 0.0],
        [0.0, 1.0, 0.0]])

    z = H * x

    return z

def jacobF(Xs_Pred, u):
    """
    Jacobian of Motion Model

    motion model
    x_{t+1} = x_t + r * (phi_1 + phi_2) * DT * cos(theta) / 2L
    y_{t+1} = y_t + r * (phi_1 + phi_2) * DT * sin(theta) / 2L
    theta_{t+1} = theta_t + r * (phi_1 - phi_2) * DT / 2L

    so
    dx/dTheta = - r * (phi_1 + phi_2) * DT * sin(theta) / 2L
    dy/dTheta = r * (phi_1 + phi_2) * DT * cos(theta) / 2L
    """
    theta = Xs_Pred[2, 0]
    phi_1 = u[0, 0]
    phi_2 = u[1, 0]
    phi_sum = phi_1 + phi_2
    Js = np.matrix([
        [1.0, 0.0, -DT * phi_sum * ratio * math.sin(theta)],
        [0.0, 1.0, DT * phi_sum * ratio * math.cos(theta)],
        [0.0, 0.0, 1.0]])

    return Js

def jacobHs(x):
    # Jacobian of Observation Model
    Hs = np.matrix([
        [1.0, 0.0, 0.0],
        [0.0, 1.0, 0.0]])

    return Hs

def jacobHp(Xp_Pred, Xs_Pred, u):
    """
    Jacobian of Parameter Observation Model:

    Hp = Hs * df(Xs, Xp)/ dXp

    motion model
    x_{t+1} = x_t + r * (phi_1 + phi_2) * DT * cos(theta) / 2L
    y_{t+1} = y_t + r * (phi_1 + phi_2) * DT * sin(theta) / 2L
    theta_{t+1} = theta_t + r * (phi_1 - phi_2) * DT / 2L

    so
    dx/dr = (phi_1 + phi_2) * DT * cos(theta) / 2L
    dy/dr = (phi_1 + phi_2) * DT * sin(theta) / 2L
    DTheta/dr = (phi_1 - phi_2) * DT / 2L

    dx/dL = - r * (phi_1 + phi_2) * DT * cos(theta) / 2 * L^2
    dy/dL = - r * (phi_1 + phi_2) * DT * sin(theta) / 2 * L^2
    DTheta/dL = - r * (phi_1 - phi_2) * DT / 2 * L^2

    """
    theta = Xs_Pred[2, 0]
    r = Xp_Pred[0, 0]
    L = Xp_Pred[1, 0]
    phi_1 = u[0, 0]
    phi_2 = u[1, 0]
    phi_sum = phi_1 + phi_2
    phi_sub = phi_1 - phi_2

    Hp = np.matrix([
        [phi_sum * DT * math.cos(theta) / (2 * L), -r * phi_sum * DT * math.cos(theta) / (2 * L * L)],
        [phi_sum * DT * math.sin(theta) / (2 * L), -r * phi_sum * DT * math.sin(theta) / (2 * L * L)]])

    return Hp

def ekf_state_estimator(Xs_Est, Ps_Est, z, u):

    #  Predict
    Xs_Pred = motion_model(Xs_Est, u)
    Js = jacobF(Xs_Pred, u)
    Ps_Pred = Js * Ps_Est * Js.T + Qs

    #  Update
    Hs = jacobHs(Xs_Pred)
    zPred = observation_model(Xs_Pred)
    y = z.T - zPred
    S = Hs * Ps_Pred * Hs.T + Rs
    K = Ps_Pred * Hs.T * np.linalg.inv(S)
    Xs_Est = Xs_Pred + K * y
    Ps_Est = (np.eye(len(Xs_Est)) - K * Hs) * Ps_Pred

    return Xs_Est, Ps_Est

def ekf_param_estimator(Xp_Est, Pp_Est, z, u):

    #  Prediction
    Xp_Pred = param_model(Xp_Est)
    Pp_Pred = Pp_Est + Qp

    #  Update
    Hp = jacobHp(Xp_Pred, Xs_Pred, u)
    zPred = observation_model(Xs_Pred)
    y = z.T - zPred
    Sp = Hp * Pp_Pred * Hp.T + Rp
    Kp = Pp_Pred * Hp.T * np.linalg.inv(Sp)
    Xp_Est = Xp_Pred + Kp * y
    Pp_Est = (np.eye(len(Xp_Est)) - Kp * Hp) * Pp_Pred

    return Xp_Est, Pp_Est

def dual_ekf_estimator(Xs_Est, Ps_Est, Xp_Est, Pp_Est, z, u):

    # Prediction
    Xp_Pred = param_model(Xp_Est)
    Xs_Pred = state_predict_motion_model(Xs_Est, u, Xp_Pred)
    Js = jacobF(Xs_Pred, u)

    Pp_Pred = Pp_Est + Qp
    Ps_Pred = Js * Ps_Est * Js.T + Qs

    # Update
    Hs = jacobHs(Xs_Pred)
    Hp = jacobHp(Xp_Pred, Xs_Pred, u)
    zPred = observation_model(Xs_Pred)
    y = z.T - zPred

    # State correction
    S = Hs * Ps_Pred * Hs.T + Rs
    K = Ps_Pred * Hs.T * np.linalg.inv(S)
    Xs_Est = Xs_Pred + K * y
    Ps_Est = (np.eye(len(Xs_Est)) - K * Hs) * Ps_Pred

    # Parameters correction
    Sp = Hp * Pp_Pred * Hp.T + Rp
    Kp = Pp_Pred * Hp.T * np.linalg.inv(Sp)
    Xp_Est = Xp_Pred + Kp * y
    Pp_Est = (np.eye(len(Xp_Est)) - Kp * Hp) * Pp_Pred

    return Xs_Est, Ps_Est, Xp_Est, Pp_Est

def plot_covariance_ellipse(Xs_Est, Ps_Est):
    Pxy = Ps_Est[0:2, 0:2]
    eigval, eigvec = np.linalg.eig(Pxy)

    if eigval[0] >= eigval[1]:
        bigind = 0
        smallind = 1
    else:
        bigind = 1
        smallind = 0

    t = np.arange(0, 2 * math.pi + 0.1, 0.1)
    a = math.sqrt(eigval[bigind])
    b = math.sqrt(eigval[smallind])
    x = [a * math.cos(it) for it in t]
    y = [b * math.sin(it) for it in t]
    angle = math.atan2(eigvec[bigind, 1], eigvec[bigind, 0])
    R = np.matrix([[math.cos(angle), math.sin(angle)],
                   [-math.sin(angle), math.cos(angle)]])
    fx = R * np.matrix([x, y])
    px = np.array(fx[0, :] + Xs_Est[0, 0]).flatten()
    py = np.array(fx[1, :] + Xs_Est[1, 0]).flatten()
    plt.plot(px, py, "--r")

def main():
    print(__file__ + " start!!")

    time = 0.0

    # State Vector [x y yaw v]'
    Xs_Est = np.matrix(np.zeros((3, 1)))
    Xs_True = np.matrix(np.zeros((3, 1)))
    Ps_Est = np.diag([0.1, 0.1, math.radians(1.0)])**2 # state error covariance matrix 

    Xs_DR = np.matrix(np.zeros((3, 1)))  # Dead reckoning

    # Parameter State Vector [r, L]'
    Xp_Est = np.matrix([r0, L0]).T
    Xp_True = np.matrix([r, L]).T
    Pp_Est =  np.diag([0.1, 0.2])**2 # parameter error covariance matrix

    # Robot state vector history
    hXs_Est = Xs_Est
    hXs_True = Xs_True
    hz = np.zeros((1, 2))
    hXs_DR = Xs_True

    # Robot parameter vector history
    hXp_Est = Xp_Est
    hXp_True = Xp_True
    hz_p = np.zeros((1, 2))

    while SIM_TIME >= time:
        time += DT
        u = calc_input()
        Xs_True, z, ud = observation(Xs_True, u)

        Xs_Est, Ps_Est, Xp_Est, Pp_Est = dual_ekf_estimator(Xs_Est, Ps_Est, Xp_Est, Pp_Est, z, ud)
        Xs_DR = state_predict_motion_model(Xs_DR, ud, Xp_Est)

        # store data history
        hXs_Est = np.hstack((hXs_Est, Xs_Est))
        hXs_True = np.hstack((hXs_True, Xs_True))
        hz = np.vstack((hz, z))

        hXp_Est = np.hstack((hXp_Est, Xp_Est))
        hXp_True = np.hstack((hXp_True, Xp_True))
        hXs_DR = np.hstack((hXs_DR, Xs_DR))

        # data visualization
        if show_animation:
            plt.cla()
            plt.figure(1)
            plt.plot(hz[:, 0], hz[:, 1], ".g")
            plt.plot(np.array(hXs_True[0, :]).flatten(),
                     np.array(hXs_True[1, :]).flatten(), "-b")

            plt.plot(np.array(hXs_DR[0, :]).flatten(),
                     np.array(hXs_DR[1, :]).flatten(), "-k")

            plt.plot(np.array(hXs_Est[0, :]).flatten(),
                     np.array(hXs_Est[1, :]).flatten(), "-r")
            plt.title("Path Navigation")
            plt.axis("equal")
            #

            #
            # plt.figure(2)
            # #plot_covariance_ellipse(Xs_Est, Ps_Est)
            #
            # plt.plot(np.array(hXp_Est[0, :]).flatten(),"-b")
            # plt.plot(np.array(hXp_True[0, :]).flatten(), "-r")
            # plt.title("Param Update: r ")


            # plt.figure(3)
            # plt.plot(np.array(hXp_Est[1, :]).flatten(), "-b")
            # plt.plot(np.array(hXp_True[1, :]).flatten(), "-r")
            #
            # plt.title("Param Update: L ")


            plt.grid(True)
            plt.pause(0.001)

    print(hXp_Est)

if __name__ == '__main__':
    main()
