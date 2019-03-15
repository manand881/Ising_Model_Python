import numpy

def Interface_Func(a,nrows,ncols):
    iterator=nrows
    iterator2=ncols

    if(nrows%2!=0):
        iterator=nrows+1
    if(ncols%2!=0):
        iterator2=ncols+1

    a=numpy.ones((iterator,iterator2),dtype=int)
        
    for i in range(0,iterator):
        for j in range(0,iterator2):
            if(j>=iterator2/2):
                dummyval=-1
            else:
                dummyval=1
            a[:,j]=dummyval
    iterator=iterator2=dummyval=0
    print(a)
    return   

Interface_Func(a,4,6)