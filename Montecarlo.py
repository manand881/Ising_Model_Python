from numba import jit

import random
import numpy
import math

#   Function to generate uniform random numbers

@jit(parallel=True)
def pick_random(ran0):
    
    ran0=round(random.uniform(0,1),12)
    
    return ran0 

#   End of function

@jit(nopython=True)
def Monte_Carlo(m , n ,i , j , ipass , npass , nequil , iterator , iterator2 , ran0 , a , magnetization , magnetization_ave , magnetization2_ave , energy , beta , DeltaU , output_count,energy_ave,energy2_ave ):
    
    for ipass in range(0,npass+1):
            
            if(ipass>nequil):
            
                output_count+=1
                magnetization = numpy.sum(a[1:iterator-2,1:iterator2-2])/(iterator*iterator2*1.00)
                magnetization_ave = magnetization_ave + magnetization
                magnetization2_ave = magnetization2_ave + magnetization**2
                energy = 0.00

                for i in range(0,iterator):
                    for j in range(0,iterator2):
                    
                        energy = energy - a[m,n]*(a[m-1,n]+a[m+1,n]+a[m,n-1]+a[m,n+1])
                
                energy = energy / (iterator*iterator2*2.0)
                energy_ave = energy_ave + energy
                energy2_ave = energy2_ave + energy**2

            ran0=pick_random(ran0) 
            m=int((iterator-2)*ran0)  
            ran0=pick_random(ran0)
            n=int((iterator2-2)*ran0)
            trial_spin=-1*(a[m,n]) 

            DeltaU = -1*(trial_spin*(a[m-1,n]+a[m+1,n]+a[m,n-1]+a[m,n+1])*2)
                    
            ran0=pick_random(ran0)
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



    return m , n ,i , j , ipass , npass , nequil , iterator , iterator2 , ran0 , a , magnetization , magnetization_ave , magnetization2_ave , energy , beta , DeltaU , output_count,energy_ave,energy2_ave