from collections import Counter

def split_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    list1, list2 = [], []
    for line in lines:
        num1, num2 = map(int, line.split())
        list1.append(num1)
        list2.append(num2)

    return list1, list2

def similarity(list1, list2):
    total = 0
    for i in list1:
        for j in list2:
            if i == j:
                total+=i
    return total

list1, list2 = split_file('input.txt')
print(similarity(list1, list2))