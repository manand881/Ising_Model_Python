#  Ising Model in Python.

#  13-03-2019.
#  Written by Anand Mahesh.
#  Python 3.7.
#  NumPy has been installed and used in this project.

import numpy
import random
import time

time_start = time.perf_counter()    # for Program Runtime Profiling. Time.clock()


i=0                     #   Dummy Intgers
j=0                     #   Dummy Intgers
m=0                     #   Dummy Intgers
n=0                     #   Dummy Intgers
n2=0                    #   Dummy Intgers
m2=0                    #   Dummy Intgers
nrows=0                 #   Number of rows of A
ncols=0                 #   Number of Columns of 
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
MovieOn=None            #   set to .true. to make movie of 1 temp
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
iterator=0              #   to be used with for loop / dummy operation
iterator2=0             #   to be used with for loop / dummy operations


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
stringreader=(ising.readline())
if(stringreader==".true.\n"):
    MovieOn=True

ising.close()

a=numpy.zeros(shape=(nrows,ncols))          #   Matrix of spins

# Funtions

# Function to determine the number of rows and columns the spin matrix must have

def matrix_row_col_check():
    
    global iterator
    global iterator2
    global nrows
    global ncols
    global a

    iterator = nrows
    iterator2 = ncols

    if(nrows%2!=0):
        iterator=nrows+1
    if(ncols%2!=0):
        iterator2=ncols+1

    a=numpy.ones((iterator,iterator2),dtype=int)
    


spin = open("spin-array", "w")
spin.write("number of rows :"+str(nrows))
spin.write("\nnumber of columns :"+str(ncols))

nscans=int((high_temp-low_temp)/temp_interval+1)

# if(MovieOn==".true.\n"):
if(MovieOn==True):

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
        
        # Checkerboard Pattern Matrix

        matrix_row_col_check()        
        
        a[1::2,::2] = -1
        a[::2,1::2] = -1

    elif(ConfigType==2):
        
        # Interface Pattern Matrix

        matrix_row_col_check()

        for i in range(0,iterator):
            for j in range(0,iterator2):
                if(j>=iterator2/2):
                    dummyval=-1
                else:
                    dummyval=1
                a[:,j]=dummyval
        iterator=iterator2=dummyval=0   

    elif(ConfigType==3):

        # Unequal Interface Pattern Matrix

        matrix_row_col_check()

        for i in range(0,iterator):
            for j in range(0,iterator2):
                if(j>=iterator2/4):
                    dummyval=-1
                else:
                    dummyval=1
                a[:,j]=dummyval
        iterator=iterator2=dummyval=0
    elif(ConfigType==4):

        # Random Pattern Matrix

        matrix_row_col_check()
        
        for i in range(0,iterator):
            for j in range(0,iterator2):
                dummy=random.randint(1,100)
                if(dummy%2==0 or dummy==0):
                    dummy=1
                else:
                    dummy=-1
                a[i,j]=dummy

    else:
        print("Error! Check ConfigType parameter in ising.in")      

    for i in range(ipass,npass):
        if(MovieOn and ipass%(npass/50)):
            for i in range(1,nrows):
                for j in range(1,ncols):
                    spin.write(i,j,a[i,j])

        if(ipass>nequil):
           
            output_count+=1
            magnetization = sum(a[1:nrows,1:ncols])/(ncols*nrows*1.00)
            magnetization_ave = magnetization_ave + magnetization
            magnetization2_ave = magnetization2_ave + magnetization**2
            energy = 0.00
           
            for i in range(1,nrows):
                for j in range(1,ncols):
                   
                    energy = energy-a[m,n]*(a[m-1,n]+a[m+1,n]+a[m,n-1]+a[m,n+1])
            
            energy = energy / (ncols*nrows*2.0)
            energy_ave = energy_ave + energy
            energy2_ave = energy2_ave + energy**2
        

        
Profiler = open("Program_Profile.txt","a+")
time_elapsed=time.perf_counter()-time_start
Profiler.write("Program took "+str(time_elapsed)+" seconds to run\n")
Profiler.close()
spin.close()
magnet.close()
temper.close()