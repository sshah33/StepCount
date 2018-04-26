import csv
import sys

walk_time = []
walk_data = []
avg=[]
sum=0.0
file = open('walk-shoe.csv')
reader = csv.reader(file)

def stepCount(data_avg):
    count=0;
    for x in range (0, len(avg),37):
        max=0
        for var in range(x, x+37):
            if(avg[x] > max):
                max=avg[x]
        if(max > data_avg):
            count=count+1
    print("Number of steps walked =",count)

def preprocess(sum):
    for row in reader:
        walk_data.append(row[2])
        walk_time.append(row[0])
    window=walk_time.index("300") #according to the data nearest value to 0.3s window is 300ms. hence setting window size to index of 311ms
    walk_data_sum = 0.0
    for var in range(1, len(walk_data)):
        walk_data_sum = walk_data_sum + float(walk_data[var])
    data_avg = walk_data_sum/(len(walk_data)-1) #average of entire data
    for var in range(1, window+1):
        sum= sum + float(walk_data[var])
    avg.append(sum/window)
    for var in range (window+2, len(walk_data)):
        sum = sum - float(walk_data[var-(window+1)])
        sum = sum + float(walk_data[var])
        avg.append(sum/window)
    stepCount(data_avg) #called step count process

preprocess(sum) #called initial process
file.close()
