def count_perfect_cubes(a, b):
    # Determine the max value
    max_num = max(a,b)
    # Determine the min value
    min_num = min(a,b)
    # determine the max absolute value
    abs_max = max(abs(a),abs(b))
    # init count in 0
    count = 0
    # In this case the logic is iterate over natural integer and find if the number cubed is in the range a-b. 
    # This is to save time and iterations, I suppose a big posibble range, but never will be reached
    for i in range(int(abs_max/3)):
        # Calculate posibble cubed number
        possible_number = i**3
        # Check possible_number = 0 because is an especial case and could be counted twice following my logic
        if possible_number == 0 and min_num <= possible_number <= max_num :
            count += 1
            continue
        # Check positive cases
        if possible_number <= abs(max_num) and min_num <= possible_number <= max_num:
            count += 1
        # Check negative cases
        if possible_number <= abs(min_num) and min_num < 0:
            count += 1
        # Check exit case
        if possible_number > abs_max:
            break

    return count

if __name__ == '__main__':
    print(count_perfect_cubes(3, 30))
    print('=========')
    print(count_perfect_cubes(1, 30))
    print('=========')
    print(count_perfect_cubes(30, 0))
    print('=========')
    print(count_perfect_cubes(-64, 64))
    print('=========')
    print(count_perfect_cubes(9214, -8127))