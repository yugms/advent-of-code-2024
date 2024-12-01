import csv

column_1 = []
column_2 = []
end_value = 0
value_to_add = 0

with open('../data/lists.csv', 'r') as csv_file:
    reader=csv.reader(csv_file)
    for row in reader:
        column_1.append(int(row[0].split("   ")[0]))
        column_2.append(int(row[0].split("   ")[1]))

column_1.sort()
column_2.sort()

for i in range(len(column_1)):
    value_to_add = abs( column_2[i] - column_1[i])
    end_value += value_to_add

print(end_value)