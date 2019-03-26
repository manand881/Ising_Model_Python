#   Ising Model in Python.

#   13-03-2019.
#   Written by Anand Mahesh.
#   Python 3.7.
#   NumPy has been installed and used in this project.
#   tools used: Visual Studio Code, GitHub Desktop.
from numba import jit
import numpy
import random
import time
import math
import csv

time_start = time.perf_counter()    #   For Program Runtime Profiling. Time.clock() has been depreciated 


i=0                     #   Dummy Intgers
j=0                     #   Dummy Intgers
m=0                     #   Dummy Intgers
n=0                     #   Dummy Intgers
# n2=0                    #   Dummy Intgers
# m2=0                    #   Dummy Intgers
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
# DeltaU1=0               #   energy changes for lattice gas
# DeltaU2=0               #   energy changes for lattice gas
log_eta=0               #   log of random number to compare to
magnetization=0         #   magnetization of all spins in lattice
magnetization_ave=0     #   cumulative average magnetization
magnetization2_ave=0    #   cumulative average of mag. squared
energy=0                #   energy of all spins in lattice
energy_ave=0            #   cumulative average of energy
energy2_ave=0           #   cumulative average of energy squared
output_count=0          #   Number of times things have been added to averages
ran0=0                  #   T B C
# rand_uniform=0          #   T B C
stringreader=""         #   variable to read files from text to be later converted to int
iterator=0              #   to be used with for loop / dummy operation
iterator2=0             #   to be used  for loop / dummy operations


print("MONTE CARLO 2D ISING MODEL\n")
print("Monte Carlo Statistics for 2D Ising Model with periodic boundary conditions\n")
print("The critical temperature is approximately 2.3, as seen on Chandler p. 123.\n")

ising = open("ising.in", "r")       #   This section is for reading input parameters and assigning it to global variables
                                       
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
stringreader=(ising.readline())
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
    MovieOn=True                           #    To be removed

ising.close()

a=numpy.ones(shape=(nrows,ncols))          #   Creating a matrix of spins populated by zeros

#   Funtions

#   Function to determine the number of rows and columns the spin matrix must have

@jit
def matrix_row_col_check():
    
    global iterator                         #   global is called to manipulate global variables
    global iterator2
    global nrows
    global ncols
    global a

    iterator = nrows
    iterator2 = ncols

    if(nrows%2!=0):
        iterator+=1
    if(ncols%2!=0):
        iterator2+=1

    a=numpy.ones((iterator,iterator2),dtype=int)

#   End of Function

#   Function to generate uniform random numbers

@jit
def pick_random():

    global ran0
    
    ran0=round(random.uniform(0,1),12) 

#   End of function

spin_attribute = open("spin_array_attribute.csv", "w")
spin_attribute.write("number of rows :"+str(nrows))
spin_attribute.write("\nnumber of columns :"+str(ncols))

nscans=int((high_temp-low_temp)/temp_interval+1)    #   Determining the number of scans

if(MovieOn==True):

    spin_attribute.write("\n51")
    spin_attribute.write("\n1")

else:
    
    spin_attribute.write("\nnumber of scans :"+str(nscans))
    spin_attribute.write("\n2")

spin_attribute.close()

spin = open("spin_array.csv","w+")
spin_writer=csv.writer(spin)
spin_row=["temp","i","j","a[i,j]"]
spin_writer.writerow(spin_row)

magnet = open("magnetization.csv","w+")
magnet.write("Temp , Ave_magnetization , Ave_magnetization^2 , Susceptibility")
magnet.write("\n")
magnet_writer=csv.writer(magnet)

energyObj = open("energy.csv","w+")
energyObj.write("Temp , Ave_energy , Ave_energy^2 , C_v")
energyObj.write("\n")
energy_writer=csv.writer(energyObj)

#   Scan Loop

for iscan in range(1,nscans+1):                                     #   Main for loop    
    temp = float(round((high_temp - temp_interval*(iscan-1)), 3))   #   rounding off to two decimal places for optimisation purposes 
    print("Running Program for Temperature : "+str(temp)+"\n")
    
    beta  =  1.0/temp
    output_count   =   0
    energy_ave  =  0.0
    energy2_ave  =  0.0
    magnetization_ave  =  0.0
    magnetization2_ave  =  0.0
    
    if(ConfigType==1):                                              #   Section for choosing Configtype
        
        #   Checkerboard Pattern Matrix

        matrix_row_col_check()        
        
        a[1::2,::2] = -1
        a[::2,1::2] = -1

    elif(ConfigType==2):
        
        #   Interface Pattern Matrix

        matrix_row_col_check()

        for i in range(0,iterator):
            for j in range(0,iterator2):
                if(j>=iterator2/2):
                    dummyval=-1
                else:
                    dummyval=1
                a[:,j]=dummyval
        dummyval=0   

    elif(ConfigType==3):

        #   Unequal Interface Pattern Matrix

        matrix_row_col_check()

        for i in range(0,iterator):
            for j in range(0,iterator2):
                if(j>=iterator2/4):
                    dummyval=-1
                else:
                    dummyval=1
                a[:,j]=dummyval
        dummyval=0

    elif(ConfigType==4):

        #   Random Pattern Matrix

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

    #   End of Config Chooser
    
    #   Main loop containing Monte Carlo algorithm

    for ipass in range(0,npass+1):
        
        if(MovieOn and ipass%(npass/50)==0):
            for i in range(0,iterator):
                for j in range(0,iterator2):
                    spin.write(i,j,a[i,j])

        if(ipass>nequil):
           
            output_count+=1
            magnetization = numpy.sum(a[1:iterator-2,1:iterator-2])/(iterator*iterator2*1.00)
            magnetization_ave = magnetization_ave + magnetization
            magnetization2_ave = magnetization2_ave + magnetization**2
            energy = 0.00

            for i in range(0,iterator):
                for j in range(0,iterator2):
                   
                    energy = energy - a[m,n]*(a[m-1,n]+a[m+1,n]+a[m,n-1]+a[m,n+1])
            
            energy = energy / (iterator*iterator2*2.0)
            energy_ave = energy_ave + energy
            energy2_ave = energy2_ave + energy**2

        pick_random() 
        m=int((iterator-2)*ran0)  
        pick_random()
        n=int((iterator2-2)*ran0)
        trial_spin=-1*(a[m,n]) 

        DeltaU = -1*(trial_spin*(a[m-1,n]+a[m+1,n]+a[m,n-1]+a[m,n+1])*2)
                
        pick_random()
        log_eta=math.log(ran0+(1e-10))
        
        if(-beta*DeltaU>log_eta):
            
            a[m,n]=trial_spin

            if(m==1):

                a[iterator-1,n]=trial_spin
            
            if(m==iterator-1):
                
                a[0,n]=trial_spin
            
            if(n==1):
                
                a[m,iterator2-1]=trial_spin
            
            if(n==iterator2-1):
                
                a[m,0]=trial_spin
    
    #   End Monte carlo pases

    if(MovieOn!=True):
        
        for i in range(0,iterator):
            for j in range(0,iterator2):
                # spin.write(""+str(temp)+"\t"+str(i)+"\t"+str(j)+"\t"+str(a[i,j]))
                spin_row=[temp,i,j,a[i,j]]
                spin_writer.writerow(spin_row)
    
    # magnet.write("\n"+str(temp)+","+str(abs(magnetization_ave/output_count))+","+str(magnetization2_ave/output_count))
    magnet_row=[temp , abs(magnetization_ave/output_count) , magnetization2_ave/output_count , beta*(magnetization2_ave/output_count - (magnetization_ave/output_count)**2)]
    magnet_writer.writerow(magnet_row)
    
    # energyObj.write("\n"+str(temp)+","+str(energy_ave/output_count)+","+str(energy2_ave/output_count)+","+str((beta**2)*(energy2_ave/output_count - (energy_ave/output_count)**2)))
    # energy_writer=csv.writer(energyObj)
    energy_row=[temp , energy_ave/output_count , energy2_ave/output_count , (beta**2)*(energy2_ave/output_count - (energy_ave/output_count)**2)]
    energy_writer.writerow(energy_row)

#   End Scan Loop

print("\nProgram Completed\n")

spin.close()                                            #   Closing open files.This part is important as open files may not allow writing of new data
magnet.close()
energyObj.close()

Profiler = open("Program_Profile.csv","a+")
time_elapsed=time.perf_counter()-time_start             #   Program execuion time profiler
Profiler.write("\n"+str(time_elapsed)+"")
Profiler.close()

#   THE END