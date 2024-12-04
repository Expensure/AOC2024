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

lst = read_file('input.txt')
print(lst)

def crossword_solver(lst):
    word = "XMAS"
    total = 0
    rows, cols = len(lst), len(lst[0])
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, -1), (-1, 1)]

    def check_word(y, x, dy, dx):
        for i in range(len(word)):
            ny, nx = y + i * dy, x + i * dx
            if not (0 <= ny < rows and 0 <= nx < cols) or lst[ny][nx] != word[i]:
                return False
        return True

    for y in range(rows):
        for x in range(cols):
            if lst[y][x] == word[0]:  # Check if the starting letter matches
                for dy, dx in directions:
                    if check_word(y, x, dy, dx):
                        total += 1
    return total

print(crossword_solver(lst))