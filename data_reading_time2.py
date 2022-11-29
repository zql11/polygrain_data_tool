import numpy as np
from pyevtk.hl import gridToVTK
from time import time
import matplotlib.pylab as plt
import pandas as pd

def readfile(Nx, Ny, Nz,step):
    filename = 'grainvol%d.txt' % step
    grainvol = np.zeros((Nx, Ny, Nz))
    df = pd.read_csv(filename, sep=" ")
    df.set_index(['x', 'y','z'], inplace=True)
    
    t0 = time()
    for row in df_1.iterrows():
        grainvol[int(row[0][0]), int(row[0][1]), int(row[0][2])] = row[1]
    t1 = time()
    time_cost_iterrows = t1 - t0
    
    t2 = time()
    for row in df_1.itertuples():
        grainvol[row[0][0], row[0][1], row[0][2]] = row[1]
    t3 = time()
    time_cost_itertuples = t3 - t2
    
    
    return grainvol, time_cost_iterrows, time_cost_itertuples

Nx = 64; Ny = 64; Nz = 64
Nstep = 800; Noutput = 20

times_list_iterrows = []
times_list_itertuples = []

for i in range(20, Nstep + Noutput, Noutput):
    grainvol = readfile(Nx, Ny, Nz, i)[0]
    time_cost_iterrows = readfile(Nx, Ny, Nz, i)[1]
    time_cost_itertuples = readfile(Nx, Ny, Nz, i)[2]
    
    times_list_iterrows.append(time_cost_iterrows)
    times_list_itertuples.append(time_cost_itertuples)


plt.plot(times_list_iterrows, label = 'iterrows')
plt.plot(times_list_itertuples, label = 'itertuples')

plt.title("Running Time for Different Method")
plt.xlabel("Time Step")
plt.ylabel("Running Time (ms)")
plt.legend(loc = "upper right")
plt.show()