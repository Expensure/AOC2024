def read_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    lst = []
    for line in lines:
        sublist = []
        for i in line:
            sublist.append(i)
        lst.append(sublist)

    return lst

def crossword_solver(lst):
    word = "MAS"
    total = 0

    for y in range(len(lst)):
        for x in range(len(lst[0])):
            if lst[y][x] == word[1]:
                try:
                    if (
                            (lst[y - 1][x - 1] == word[0] and lst[y + 1][x + 1] == word[2])
                            or (lst[y - 1][x - 1] == word[2] and lst[y + 1][x + 1] == word[0])
                    ) and (
                            (lst[y - 1][x + 1] == word[0] and lst[y + 1][x - 1] == word[2])
                            or (lst[y - 1][x + 1] == word[2] and lst[y + 1][x - 1] == word[0])
                    ):
                        total+= 1
                except:
                    pass
    return total



print(crossword_solver(read_file('input.txt')))