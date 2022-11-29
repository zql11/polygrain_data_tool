import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D 
import numpy as np

def readfile(Nx, Ny, Nz,step):
    filename = 'grainvol%d.txt' % step
    indata = np.loadtxt(filename, skiprows = 1)
    grainvol = np.zeros((Nx, Ny, Nz))
    for i in range(len(indata)):
        grainvol[int(indata[i,0]), int(indata[i, 1]), int(indata[i,2])] = indata[i, 3]
    
    return grainvol

def plot_3D(Nx = 64, Ny = 64, Nz = 64, Nstep = 800, Noutput = 20):
    grainvol_data = []
    for i in range(600, Nstep + Noutput, Noutput):
        grainvol = readfile(Nx, Ny, Nz, i)
        grainvol_data.append(grainvol)
        
    for i in range(len(grainvol_data)):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        X, Y, Z = np.mgrid[:64, :64, :64]
        ax.scatter(X, Y, Z, c=grainvol_data[i].ravel())
#         plt.savefig("{i}.png")
        plt.show()