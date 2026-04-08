import numpy as np
import matplotlib.pyplot as plt



x = np.zeros((2000, 2), dtype=float)
u = np.array([0.3,0])
h = 0.1
D = 0.02
I = np.identity(2)
T = 0
states = []
print(x[:,0])
while T <=60:
    
    for i in range(len(x)):
        x[i] += u*h + np.sqrt(2*D*h)*np.random.multivariate_normal([0, 0], np.eye(2))
    
    if T % 15 == 0 and (T != 0):
        states.append(x.copy())
    T += h
    T = np.round(T,1)
    print(T)
fig, axs = plt.subplots(2, 2, figsize=(10, 8))
for i in range(4):
    axs.flat[i].scatter(states[i][:, 0], states[i][:, 1], s=1)
    axs.flat[i].set_title(f'Tid: {15*(i+1)} s')
    axs.flat[i].set_xlim(0, 25)
    axs.flat[i].set_ylim(-5, 5)
plt.show()

