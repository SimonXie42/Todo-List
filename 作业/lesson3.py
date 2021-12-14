import csv
import random
data = {}
data2 = []
with open('1.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        if not row[0] in data:
            data[row[0]]=row[1:]
            data2.append(row)
        else:
            a = 'new_'+ str(row[0])
            data[a]=row[1:]
            data2.append(row)
print(data)
print(data2)

with open('2.csv','w',newline='')as f:
    writer = csv.writer(f)
    for i in data2:
        writer.writerow(i)
f.close()
with open('3.csv','w',newline='') as f:
    fieldnames = {'1','3','new_1'}
    writer = csv.DictWriter(f,fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow(data)
f.close()

with open('2.csv','a',newline='')as f:
    writer = csv.writer(f)
    for i in range(0,10):
        writer.writerow([str(random.randint(1,10)),str(random.randint(1,10)),str(random.randint(1,10))])
