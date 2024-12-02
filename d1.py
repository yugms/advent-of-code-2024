from collections import Counter

column_1 = []
column_2 = []

with open('./data/day1.txt', 'r') as file:
    for line in file:
        numbers = line.split() # splits the line
        numbers = [int(num) for num in numbers] # turns into integer
        column_1.append(numbers[0]) # creates two separate lists with the numbers
        column_2.append(numbers[1])

column_1.sort() # sorts the numbers
column_2.sort()

# challenge 1
total_distance = 0
for i in range(len(column_1)):
    distance  = abs( column_2[i] - column_1[i]) # find the distance in between and creates one big value
    total_distance += distance

# challenge 2
c2_count = Counter(column_2) # count of how many times each number comes up
similarity_score = 0
for i in column_1:
    number_similarity  =  c2_count[i] * i
    similarity_score += number_similarity

print(f"distance: {total_distance}")
print(f"similarity score: {similarity_score}")