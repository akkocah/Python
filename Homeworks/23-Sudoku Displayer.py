sudoku = [
    [0, 0, 0, 0, 6, 4, 0, 0, 0],
    [7, 0, 0, 0, 0, 0, 3, 9, 0],
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 5, 0, 2, 0, 6, 0],
    [0, 8, 0, 4, 0, 0, 0, 0, 0],
    [3, 5, 0, 6, 0, 0, 0, 7, 0],
    [0, 0, 2, 0, 0, 0, 1, 0, 3],
    [0, 0, 1, 0, 5, 9, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 7, 0, 0]
]

def PrintSudoku(board):
    y = 0
    print("- "*15)
    for n in board:
        x = 0
        while x != 3:
            print(n[x]," ", end="")
            x += 1
        print("| ", end="")
        while x != 6:
            print(n[x]," ", end="")
            x += 1
        print("| ", end="")
        while x != 9:
            print(n[x]," ", end="")
            x += 1
        print(" ")
        y = y + 1
        if y == 0 or y == 3 or y == 6:
            print("- "*15)
    print("- "*15)

PrintSudoku(sudoku)

x = [
    [0, 0, 0, 0, 6, 4, 0, 0, 0],
    [7, 0, 0, 0, 0, 0, 3, 9, 0],
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 5, 0, 2, 0, 6, 0],
    [0, 8, 0, 4, 0, 0, 0, 0, 0],
    [3, 5, 0, 6, 0, 0, 0, 7, 0],
    [0, 0, 2, 0, 0, 0, 1, 0, 3],
    [0, 0, 1, 0, 5, 9, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 7, 0, 0]
]
counter = 0
for i in x:
    if counter == 0:
        print("- - - - - - - - - - - - - - - - ")
    i.insert(3, "|")
    i.insert(7, "|")
    print("  ".join(list(map(str,i))))
    counter +=1
    if counter % 3 == 0:
        print("- - - - - - - - - - - - - - - - ")

counter = 0
for j in x:
    if counter == 0:
        print("- "*16)
    print(*j[:3], "|", *j[3:6], "|", *j[6:], sep="  ")
    counter +=1
    if counter % 3 == 0:
        print("- "*16)

