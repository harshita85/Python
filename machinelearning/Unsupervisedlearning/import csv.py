import csv
from tabulate import tabulate

# Open and read the CSV file
with open('students.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)

    # Convert reader to a list to access headers and rows
    data = list(reader)

    # First row is usually the header
    headers = data[0]
    rows = data[1:]

    # Display in tabular format using tabulate
    print(tabulate(rows, headers=headers, tablefmt="grid"))