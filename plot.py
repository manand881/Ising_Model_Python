import matplotlib.pyplot as plt
h=[]
i=[]
j=[]
a=0.01
for k in range(1,100):
    j.append(a*2)
    a+=1
plt.plot(j)
plt.savefig('foo.png')