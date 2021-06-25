import math
import csv

with open("data.csv", newline = "") as f:
    reader = csv.reader(f)
    classData = list(reader)

classData.pop(0)
data = []
for i in classData:
    data.append(i[1])
print(data)

def mean(data):
    totalNumberOfEntries = len(data)
    total = 0
    for numbers in data:
        total += float(numbers)
    mean = total/totalNumberOfEntries
    return mean

squaredData =[]
for num in data:
    diff = int(num) - mean(data)
    sqr = diff**2
    squaredData.append(sqr)

sum = 0
for sqnum in squaredData:
    sum += sqnum

result = sum/(len(data)-1)

SD = math.sqrt(result)
print("The standard deviation is " + str(SD))
