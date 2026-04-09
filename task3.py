import numpy as np
import matplotlib.pyplot as plt

#   This code i the same but to start with no particles and 
#   add 100 every second two changes were made

x = np.empty((0, 2), dtype=float)#  Creates empty array we can append to 
u = np.array([0.3,0])
h = 0.1
D = 0.02
I = np.identity(2)
T = 0
Cstaes = []
c = []
states = []
ccalc = 0
while T <=60:
    for i in range(10):#    And here the particles get added 10 per 0.1 seconds
        x = np.vstack([x, [0,0]])
    for i in range(len(x)):
        x[i] += u*h + np.sqrt(2*D*h)*np.random.multivariate_normal([0, 0], np.eye(2))
    if T % 15 == 0 and (T != 0):
        c=[]
        ccalc = 0
        states.append(x.copy())
        X = np.linspace(0, 25, 200)
        Y = np.linspace(-5, 5, 100)
        nx, ny = np.meshgrid(X, Y, indexing='ij')
        Z = np.zeros_like(nx)
        for i in range(nx.shape[0]):
            for j in range(nx.shape[1]):
                pos = np.array([nx[i,j], ny[i,j]])
                Z[i,j] = np.mean(np.linalg.norm(x - pos, axis=1) < 0.1)
        Cstaes.append([nx,ny,Z])
    T += h
    T = np.round(T,1)

fig ,axs = plt.subplots(2,2,  figsize=(10, 8))
for i in range(len(Cstaes)):
    axs.flat[i].contourf(Cstaes[i][0], Cstaes[i][1], Cstaes[i][2], levels=20, cmap='viridis')
    axs.flat[i].set_xlim(0, 25)
    axs.flat[i].set_ylim(-5, 5)
    axs.flat[i].set_title(f'Tid: {15*(i+1)} s')
plt.show()

fig, axs = plt.subplots(2, 2, figsize=(10, 8))
for i in range(len(states)):
    axs.flat[i].scatter(states[i][:, 0], states[i][:, 1], s=1)
    axs.flat[i].set_title(f'Tid: {15*(i+1)} s')
    axs.flat[i].set_xlim(0, 25)
    axs.flat[i].set_ylim(-5, 5)
plt.show()


