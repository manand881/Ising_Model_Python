def ReadInput(nrows,ncols,npass,nequil,high_temp,low_temp,temp_interval,ConfigType,MovieOn):
    
    f = open("ising.in", "r")
    next(f)
    nrows=(f.readline())
    next(f)
    ncols=(f.readline())
    next(f)
    npass=(f.readline())
    next(f)
    nequil=(f.readline())
    next(f)
    high_temp(f.readline())
    next(f)
    low_temp(f.readline())
    next(f)
    temp_interval=(f.readline())
    next(f)
    ConfigType=(f.readline())
    next(f)
    MovieOn=(f.readline())    
    return