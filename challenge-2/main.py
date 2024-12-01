import csv
from collections import Counter

column_1 = []
column_2 = []
end_value = 0

with open('../data/lists.csv', 'r') as csv_file:
    reader=csv.reader(csv_file)
    for row in reader:
        column_1.append(int(row[0].split("   ")[0]))
        column_2.append(int(row[0].split("   ")[1]))

c2_count = Counter(column_2)

value_to_add = 0

for i in column_1:
    value_to_add =  c2_count[i] * i
    end_value += value_to_add

print(end_value)