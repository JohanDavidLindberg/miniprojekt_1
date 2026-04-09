import numpy as np
import matplotlib.pyplot as plt


#   Creates all particles, lists and constants needed later
x = np.zeros((2000, 2), dtype=float)
u = np.array([0.3,0])
h = 0.1
D = 0.02
I = np.identity(2)
T = 0
Cstaes = []
c = []
states = []
ccalc = 0
#   Itterates untill 60s
while T <=60:
    for i in range(len(x)):#    Updates position of particles using given model
        x[i] += u*h + np.sqrt(2*D*h)*np.random.multivariate_normal([0, 0], np.eye(2))
    
    #   To save every 15 seconds 
    if T % 15 == 0 and (T != 0):
        c=[]
        ccalc = 0
        states.append(x.copy())#    Makes a copy of x to save 

        #  Creates a grid with all the coordinates
        X = np.linspace(0, 25, 200)
        Y = np.linspace(-5, 5, 100)
        nx, ny = np.meshgrid(X, Y, indexing='ij')
        C = np.zeros_like(nx)#  and a matrix matching for the concentration values 

        for i in range(nx.shape[0]):#   200
            for j in range(nx.shape[1]):#   100
                #   Takes out the current position and does monte carlo using the mean
                #   and the driac delta with 0.1 distance
                pos = np.array([nx[i,j], ny[i,j]])
                C[i,j] = np.mean(np.linalg.norm(x - pos, axis=1) < 0.1)
        Cstaes.append([nx,ny,C])
    T += h
    T = np.round(T,1)

#   Plots the concentration in all 4 time steps at the same time
fig ,axs = plt.subplots(2,2,  figsize=(10, 8))
for i in range(len(Cstaes)):
    axs.flat[i].contourf(Cstaes[i][0], Cstaes[i][1], Cstaes[i][2], levels=20, cmap='viridis')
    axs.flat[i].set_xlim(0, 25)
    axs.flat[i].set_ylim(-5, 5)
    axs.flat[i].set_title(f'Tid: {15*(i+1)} s')
plt.show()

#   Plots the position of particles in all 4 time steps at the same time
fig, axs = plt.subplots(2, 2, figsize=(10, 8))
for i in range(len(states)):
    axs.flat[i].scatter(states[i][:, 0], states[i][:, 1], s=1)
    axs.flat[i].set_title(f'Tid: {15*(i+1)} s')
    axs.flat[i].set_xlim(0, 25)
    axs.flat[i].set_ylim(-5, 5)
plt.show()


