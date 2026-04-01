import json
import csv

# Read JSON
with open("input.json", "r") as json_file:
    data = json.load(json_file)

# Write CSV
with open("output.csv", "w", newline='') as csv_file:
    writer = csv.writer(csv_file)

    # Write header
    writer.writerow(data[0].keys())

    # Write data
    for item in data:
        writer.writerow(item.values())

print("JSON converted to CSV successfully!")
