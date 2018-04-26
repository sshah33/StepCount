import csv

f =  open('walk-shoe.csv')

csv_f = csv.reader(f)
timeSlots = []
for row in csv_f:
    timeSlots.append(row[0])
print(len(timeSlots))
f.close()
