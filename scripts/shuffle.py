import csv
import random

# Specify the input and output CSV file names
input_file = 'sorted_image_links.csv'
output_file = 'shuffled_file.csv'

# Read the data from the input CSV file into a list of rows
with open(input_file, 'r', newline='') as csv_in:
    reader = csv.reader(csv_in)
    rows = list(reader)

# Shuffle the rows randomly
random.shuffle(rows)

# Write the shuffled data to the output CSV file
with open(output_file, 'w', newline='') as csv_out:
    writer = csv.writer(csv_out)
    for row in rows:
        writer.writerow(row)

print("CSV file has been shuffled and saved as 'shuffled_file.csv'.")
