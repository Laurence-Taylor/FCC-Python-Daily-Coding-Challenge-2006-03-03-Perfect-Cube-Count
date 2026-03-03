def count_perfect_cubes(a, b):
    max_num = max(a,b)
    min_num = min(a,b)
    abs_max = max(abs(a),abs(b))
    count = 0
    for i in range(int(abs_max/3)):
        possible_number = i**3
        if possible_number == 0 and min_num <= possible_number <= max_num :
            count += 1
            continue
        if possible_number <= abs(max_num) and min_num <= possible_number <= max_num:
            count += 1
        if possible_number <= abs(min_num) and min_num < 0:
            count += 1
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