def Ising_input():

    nrows = 40                  #  number of rows of spins (even number)
    
    ncols = 40                  #  number of columns of spins (even number)

    npass = 21000               #  number of passes for each temperature

    nequil = 20800              #  number of equilibration steps for each temperature

    high_temp = 4.0             #  temperature to start scan at

    low_temp = 0.92             #  temperature to finish scan at

    temp_interval = 0.005       #  scanning interval

    ConfigType = 1              #  1: checkerboard, 2: interface, 3: unequal interface, 4: Random Matrix

    return nrows, ncols, npass, nequil, high_temp, low_temp, temp_interval, ConfigType
