def split_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    list1, list2 = [], []
    for line in lines:
        num1, num2 = map(int, line.split())
        list1.append(num1)
        list2.append(num2)

    return list1, list2

def variation(list1, list2):
    list1.sort()
    list2.sort()
    total = 0
    for i, j in zip(list1, list2):
        print(i,j)
        total+=abs(i-j)
    return total

list1, list2 = split_file('input.txt')
print(variation(list1, list2))