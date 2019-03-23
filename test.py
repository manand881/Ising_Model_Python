# import csv
# import random
# baail=round(random.uniform(0,1),12)
# vaibhavi=round(random.uniform(0,1),12)
# anand=round(random.uniform(0,1),12)

# row = [baail, vaibhavi, anand]

# with open('people1.csv', 'a+') as testspin:
#     writer = csv.writer(testspin)
#     writer.writerow(row)

# testspin.close()
import random
import csv

magnet=open("test.csv","w+")
magnet.write("testing,testing2\n")
for i in range(1,11):
    # j=round(random.uniform(0,1),12)
    j=i**2
    l=j**2
    writer=csv.writer(magnet)
    k=[j,l]
    writer.writerow(k)

magnet.close