import matplotlib.pyplot as plt
import csv

temp=[]
Ave_magnetization=[]

# h=[]
# i=[]
# j=[]
# a=0.01
# for k in range(1,100):
#     j.append(a*2)
#     a+=1
# plt.plot(j)
# plt.savefig('foo.png')
with open('magnetization.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    next(csvfile)
    for row in readCSV:
        # print(row[0])
        temp.append(row[0])
        Ave_magnetization.append(row[1])
        next(csvfile)

# plt.plot(temp,Ave_magnetization,'-gD')
plt.scatter(Ave_magnetization,temp, alpha=0.5)
plt.savefig('Temp__Vs__Ave_magnetization.png')
# s=area, c=colors,
print(temp)
print(Ave_magnetization)