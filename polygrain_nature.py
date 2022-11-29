import numpy as np
from pyevtk.hl import gridToVTK
import pandas as pd
import matplotlib.pylab as plt

def readfile(step):
    filename = 'grainvol%d.txt' % step
    df = pd.read_csv(filename, sep=" ")
    return df

def nature_dict(Nstep = 800, Noutput = 20):
    grainvol_dict = {}
    for i in range(100, Nstep + Noutput, Noutput):
        grainvol_dict[i] = readfile(i)

    grainvol_mean_dict = {}
    grainvol_std_dict = {}
    for key in grainvol_dict:
        key_mean = grainvol_dict[key]['grainvol'].mean()
        key_std = grainvol_dict[key]['grainvol'].std()
        grainvol_mean_dict[key] = key_mean
        grainvol_std_dict[key] = key_std
    return grainvol_mean_dict, grainvol_std_dict

def nature_plot():
    grainvol_mean_dict = nature_dict(Nstep = 800, Noutput = 20)[0]
    grainvol_std_dict = nature_dict(Nstep = 800, Noutput = 20)[1]
    mean_list = grainvol_mean_dict.items()
    mean_List = sorted(mean_list) 
    x, y = zip(*mean_list) 
    plt.plot(x, y, label = "Average")

    std_list = grainvol_std_dict.items()
    std_List = sorted(std_list) 
    x, y = zip(*std_list) 
    plt.plot(x, y, label = 'Standard Deviation')
    plt.title("Average and Standard Deviation of Grainvol")
    plt.xlabel("Time Step")
    plt.ylabel("Average and Standard ")
    plt.legend(loc = "lower right")
    plt.show()