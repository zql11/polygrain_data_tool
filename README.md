# Polygrain Data Tool

## Data Introduction

A series of data from different time steps: 0, 20, 40, … 800.

For data at each time step:
The format is (i, j, k, grainvol). i, j, k is the id of each grid. There are 64 * 64 * 64 grids in total (Denoted by Nx = 64; Ny = 64; Nz = 64). Grainvol is the variable to visualize. It is in the range of 0 -1. 0 indicates grain boundary and 1 indicates grain. It is different for different grids and at different time step.

## Data Tool Introduction

1) Compare different methods to read 3D data faster. Measure the speedup after optimization. ```data_reading_time1.py``` and ```data_reading_time2.py``` show the time of different methods.

2) Calculate the average and standard deviation of grainvol at different time steps. Plot the average and standard deviation value vs time step. ```polygrain_nature.py```show the changes of average and standard deviation of grainvol at different time steps which can verified the nature of Polygrain.

3) Visualize the 3D data using python library. The size of  64 * 64 * 64 Polygrain can be visualized through ```Visualize_3D_Polygrain.py```.

## Image Show

64 * 64 * 64 grids data from 280 & 720 time step:

![200 Polygrain](https://user-images.githubusercontent.com/99223260/204435408-de555d6f-56a9-41ad-afd6-a4103968fb3a.png)                                    ![Polygrain_3D](https://user-images.githubusercontent.com/99223260/204432449-c8a30a6e-428c-48bd-a744-b0b2dcba0dfe.png)

256 * 256 * 256 grids data from 2000 time step:

![256](https://user-images.githubusercontent.com/99223260/204436207-8513a62b-0911-4798-a839-d5e97133bd4e.png)


