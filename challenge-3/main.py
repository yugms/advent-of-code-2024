import csv
from os import path

def array_number_flow_checker(array_to_check):
    # * checks if the array is strictly increasing or strictly decreasing * #
    return sorted(array_to_check) == array_to_check or sorted(array_to_check, reverse=True) == array_to_check

def array_number_gap_checker(array_to_check):
    for i in range(len(array_to_check)):
        if i > 0:
            difference_between_elements = abs(array_to_check[i] - array_to_check[i-1])
            if difference_between_elements < 1 or difference_between_elements > 3:
                return False
            else: continue
        else: continue
    return True

if __name__ == '__main__':

    csv_file = "../data/red-nosed-reports.csv"
    txt_file = "../data/red-nosed-reports.txt"
    delimiter = " "

     # * Converts a text file to CSV format * #
    if path.exists(csv_file):
        print("file already exists")
    else:
        with open(txt_file, 'r') as infile, open(csv_file, 'w', newline='') as outfile:
            writer = csv.writer(outfile, delimiter=delimiter)

            for line in infile:
                row = line.strip().split(delimiter)  # Split the line based on the delimiter
                writer.writerow(row)
        print("successfully generated file")

    # * extracts each row as an array into an array * #
    rows = []
    with open(csv_file, 'r') as csv_file_:
        reader=csv.reader(csv_file_)
        for row in reader:
            rows.append(list(map(int, row[0].split(" "))))
    
    # * checks how many rows are "safe" * #

    number_of_safe_rows = 0

    for row in rows:
        if array_number_flow_checker(row) and array_number_gap_checker(row):
            number_of_safe_rows += 1
    print(number_of_safe_rows)