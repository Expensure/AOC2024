import numpy as np
def read_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    lst = []
    for line in lines:
        numbers = [int(num) for num in line.strip().split()]
        lst.append(numbers)

    return lst


def count_checker(lst):
    total=0
    subcounter1=0
    subcounter2 = 0
    subcounter3 = 0
    for i in lst:

        # Check for doubles
        res = np.array(i)
        unique_res = np.unique(res)
        if len(unique_res) != len(res):
            print(i)
            subcounter1+=1
            continue

        # Check for alternating asc/desc
        is_ascending = i == sorted(i)
        is_descending = i == sorted(i, reverse=True)
        if not (is_ascending or is_descending):
            subcounter1 += 1
            continue

        fail = False
        for j in range(len(i) - 1):
            increase = i[j + 1] - i[j]
            if increase > 3 or increase < -3:
                print(i)
                fail = True
                subcounter1 += 1

        if fail == True:
            continue
        total+=1


    return total


lst = read_file('input.txt')
print(count_checker(lst))