import numpy as np
from pyevtk.hl import gridToVTK
from time import time
import matplotlib.pylab as plt
import pandas as pd

def readfile(Nx, Ny, Nz,step):
    filename = 'grainvol%d.txt' % step
    indata = np.loadtxt(filename, skiprows = 1)
#     print(indata)
    grainvol = np.zeros((Nx, Ny, Nz))
    
    t0 = time()
    for i in range(len(indata)):
        grainvol[int(indata[i,0]), int(indata[i, 1]), int(indata[i,2])] = indata[i, 3]
    t1 = time()
    time_cost_nor = t1 - t0
    
    t2 = time()
    for i, val in enumerate(indata):
        grainvol[int(indata[i,0]), int(indata[i, 1]), int(indata[i,2])] = indata[i, 3]
    t3 = time()
    time_cost_enu = t3 - t2
    
    t4 = time()
    for x in np.nditer(indata):
        grainvol[int(indata[i,0]), int(indata[i, 1]), int(indata[i,2])] = indata[i, 3]
    t5 = time()
    time_cost_iter = t5 - t4
    
    return grainvol, time_cost_nor, time_cost_enu, time_cost_iter

Nx = 64; Ny = 64; Nz = 64
Nstep = 800; Noutput = 20

times_list_nor = []
times_list_enu = []
times_list_iter = []

for i in range(20, Nstep + Noutput, Noutput):
    grainvol = readfile(Nx, Ny, Nz, i)[0]
    time_cost_nor = readfile(Nx, Ny, Nz, i)[1]
    time_cost_enu = readfile(Nx, Ny, Nz, i)[2]
    time_cost_iter = readfile(Nx, Ny, Nz, i)[3]
    
    times_list_nor.append(time_cost_nor)
    times_list_enu.append(time_cost_enu)
    times_list_iter.append(time_cost_iter)
    
plt.plot(times_list_nor, label = 'range of length')
plt.plot(times_list_enu, label = 'enumerate')
plt.plot(times_list_iter, label = 'iter')

plt.title("Running Time for Different Method")
plt.xlabel("Time Step")
plt.ylabel("Running Time (ms)")
plt.legend(loc = "center right")
plt.show()


