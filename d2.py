def array_number_flow_checker(array_to_check: list) -> bool:
    # * checks if the array is strictly increasing or strictly decreasing * #
    return sorted(array_to_check) == array_to_check or sorted(array_to_check, reverse=True) == array_to_check

def array_number_gap_checker(array_to_check: list) -> bool:
    # * checks if the gap between each element is greater than 1 and less then 3
    for i in range(len(array_to_check)):
        if i > 0:
            difference_between_elements = abs(array_to_check[i] - array_to_check[i-1])
            if difference_between_elements < 1 or difference_between_elements > 3:
                return False
            else: continue
        else: continue
    return True

def row_safe_with_row_removed_check(array_to_check: list) -> bool:
    for i in range(len(array_to_check)):
        new_array = array_to_check[:i] + array_to_check[i + 1:]
        if array_number_gap_checker(new_array) and array_number_flow_checker(new_array):
            return True
    return False


if __name__ == '__main__':

    # * extracts each row as an array into an array * #
    rows = []
    with open('./data/day2.txt', 'r') as file:
        for line in file:
            numbers = line.split() # splits the line
            numbers = [int(num) for num in numbers] # turns into integer
            rows.append(numbers)

    number_of_safe_rows = 0
    number_of_safe_rows_with_dampener = 0

    for row in rows:
        if array_number_flow_checker(row) and array_number_gap_checker(row):
            number_of_safe_rows += 1
        if row_safe_with_row_removed_check(row):
            number_of_safe_rows_with_dampener += 1

    print(f"number of safe rows: {number_of_safe_rows}")
    print(f"number of safe rows with dampener: {number_of_safe_rows_with_dampener}")