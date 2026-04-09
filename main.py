import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D



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
while T <=60:
    
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
        print("NU KÖR DEN")
        for i in range(nx.shape[0]):
            for j in range(nx.shape[1]):
                pos = np.array([nx[i,j], ny[i,j]])
                Z[i,j] = np.mean(np.linalg.norm(x - pos, axis=1) < 0.2)
        Cstaes.append([nx,ny,Z])
        # X = np.linspace(0,25,20)
        # Y = np.linspace(-5,5, 10) 
        # nx, ny = np.meshgrid(X,Y, indexing='ij')
        # for i in range(20):
        #     for j in range(10):
        #         for k,xk in enumerate(x):
        #             if np.sqrt(np.abs(np.dot(xk,[i,j]))) < 0.1:
        #                 ccalc += 1
        #         print(f'i {i}, j {j}')
        #         c.append([i,j,ccalc/len(x)])
        # Cstaes.append(c)
        # print(Cstaes)¨
    T += h
    T = np.round(T,1)



# Funkar denna?!

# X = np.linspace(0, 25, 20)
# Y = np.linspace(-5, 5, 10)
# nx, ny = np.meshgrid(X, Y, indexing='ij')
# Z = np.zeros_like(nx)

# for i in range(nx.shape[0]):
#     for j in range(nx.shape[1]):
#         pos = np.array([nx[i,j], ny[i,j]])
#         Z[i,j] = np.mean(np.linalg.norm(x - pos, axis=1) < 0.1)

fig ,axs = plt.subplots(2,2,  figsize=(10, 8))
for i in range(len(Cstaes)):
    axs.flat[i].contourf(Cstaes[i][0], Cstaes[i][1], Cstaes[i][2], levels=20, cmap='viridis')
    axs.flat[i].set_xlim(0, 25)
    axs.flat[i].set_ylim(-5, 5)
    axs.flat[i].set_title(f'Tid: {15*(i+1)} s')
plt.show()








# nx, ny, Z = Cstaes[0]
# plt.contourf(nx, ny, Z, levels=20, cmap='viridis')
# plt.colorbar()
# plt.title('Contour of c')
# plt.xlim(0, 25)
# plt.ylim(-5, 5)
# plt.show()



fig, axs = plt.subplots(2, 2, figsize=(10, 8))
for i in range(len(states)):
    axs.flat[i].scatter(states[i][:, 0], states[i][:, 1], s=1)
    axs.flat[i].set_title(f'Tid: {15*(i+1)} s')
    axs.flat[i].set_xlim(0, 25)
    axs.flat[i].set_ylim(-5, 5)
plt.show()


