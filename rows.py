import csv

file = open("data.csv", "r")
reader = csv.reader(file)

row_count = 0
for row in reader:
    row_count += 1

print("Total rows in CSV:", row_count)
file.close()
