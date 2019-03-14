#  Ising Model in Python.

#  13-03-2019.
#  Written by Anand Mahesh.
#  Python 3.7.
#  NumPy has been installed and used in this project.

import numpy
import csv

i=0                     #   Dummy Intgers
j=0                     #   Dummy Intgers
m=0                     #   Dummy Intgers
n=0                     #   Dummy Intgers
n2=0                    #   Dummy Intgers
m2=0                    #   Dummy Intgers
nrows=0                 #   Number of rows of A
ncols=0                 #   Number of Columns of 
a=numpy.zeros(shape=(nrows+2,ncols+2))  #   Matrix of spins
temp=0                  #   Temperature
beta=0                  #   Inverse Temperature
ConfigType=0            #   Starting Configuration type
npass=0                 #   number of passes for MC algorithm
ipass=0                 #   the current pass number
nequil=0                #   number of equilibration steps
trial_spin=0            #   values of changed spin
high_temp=0             #   starting temp for scan
low_temp=0              #   final temp for scan
temp_interval=0         #   interval between scan points
nscans=0                #   number of scans (each at diff T)
iscan=1                 #   current number
iscan1=0                #   current number
MovieOn=""              #   set to .true. to make movie of 1 temp
DeltaU=0                #   change in energy between 2 configs
DeltaU1=0               #   energy changes for lattice gas
DeltaU2=0               #   energy changes for lattice gas
log_eta=0               #   log of random number to compare to
magnetization=0         #   magnetization of all spins in lattice
magnetization_ave=0     #   cumulative average magnetization
magnetization2_ave=0    #   cumulative average of mag. squared
energy=0                #   energy of all spins in lattice
energy_ave=0            #   cumulative average of energy
energy2_ave=0           #   cumulative average of energy squared
output_count=0          #   Number of times things have been added to averages
ran0=0                  #   T B C
rand_uniform=0          #   T B C
stringreader=""         #   variable to read files from text to be later converted to int
print("MONTE CARLO 2D ISING MODEL\n")
print("Monte Carlo Statistics for 2D Ising Model with periodic boundary conditions\n")
print("The critical temperature is approximately 2.3, as seen on Chandler p. 123.\n")

ising = open("ising.in", "r")

next(ising)
stringreader=(ising.readline())
nrows=int(stringreader)

next(ising)
stringreader=(ising.readline())
ncols=int(stringreader)

next(ising)
stringreader=(ising.readline())
npass=int(stringreader)

next(ising)
nequil=(ising.readline())
nequil=int(stringreader)

next(ising)
stringreader=(ising.readline())
high_temp=float(stringreader)

next(ising)
stringreader=(ising.readline())
low_temp=float(stringreader)

next(ising)
stringreader=(ising.readline())
temp_interval=float(stringreader)

next(ising)
stringreader=(ising.readline())
ConfigType=int(stringreader)

next(ising)
MovieOn=(ising.readline())

ising.close()

spin = open("spin-array", "w")
spin.write("number of rows :"+str(nrows))
spin.write("\nnumber of columns :"+str(ncols))

nscans=int((high_temp-low_temp)/temp_interval+1)

if(MovieOn==".true.\n"):
    spin.write("\n51")
    spin.write("\n1")
else:
    spin.write("\nnumber of scans :"+str(nscans))
    spin.write("\n2")

temper = open("temperature.dat","w")
temper.write("Temperature\t\t\ti\t\t\tj\t\t\tspin")
magnet = open("magnetization","w")
magnet.write("Temp\t\t\tave_magnetization\t\t\tave_magnetization^2\t\t\tsusceptibility")
energy = open("energy","w")
energy.write("temp ave_energy\t\t\tave_energy^2\t\t\tC_v")

for iscan in range(1,nscans):    
    temp = high_temp - temp_interval*(iscan-1)
    print("Running Program for Temperature : "+str(temp))
    beta  =  1.0/temp
    output_count=energy_ave=energy2_ave=magnetization_ave=magnetization2_ave=0
    if(ConfigType==1):
        print("1")
    elif(ConfigType==2):
        print("2")
    elif(ConfigType==3):
        print("3")
    else:
        print("Error! Check ConfigType parameter in ising.in")