def print_matrix(matrix):
    for i in range(3):
        print(" ",end="")
        print(matrix[i][0],matrix[i][1],matrix[i][2],matrix[i][3],sep=" | ")
        print("--- --- --- ---")
    print(" ",end="")
    print(matrix[3][0],matrix[3][1],matrix[3][2],matrix[3][3],sep=" | ")
def check(matrix):
    if matrix[0][0]!=' ' and matrix[0][0]==matrix[0][1]==matrix[0][2]==matrix[0][3]=='X':
        print("Player 1 wins")
        return 1
    if matrix[1][0]!=' ' and matrix[1][0]==matrix[1][1]==matrix[1][2]==matrix[1][3]=='X':
        print("Player 1 wins")
        return 1
    if matrix[2][0]!=' ' and matrix[2][0]==matrix[2][1]==matrix[2][2]==matrix[2][3]=='X':
        print("Player 1 wins")
        return 1
    if matrix[0][0]!=' ' and matrix[0][0]==matrix[1][0]==matrix[2][0]==matrix[3][0]=='X':
        print("Player 1 wins")
        return 1
    if matrix[0][1]!=' ' and matrix[0][1]==matrix[1][1]==matrix[2][1]==matrix[3][1]=='X':
        print("Player 1 wins")
        return 1
    if matrix[0][2]!=' ' and matrix[0][2]==matrix[1][2]==matrix[2][2]==matrix[3][3]=='X':
        print("Player 1 wins")
        return 1
    if matrix[0][0]!=' ' and matrix[0][0]==matrix[1][1]==matrix[2][2]==matrix[3][3]=='X':
        print("Player 1 wins")
        return 1
    if matrix[0][3]!=' ' and matrix[0][3]==matrix[1][2]==matrix[2][1]==matrix[3][0]=='X':
        print("Player 1 wins")
        return 1
    if matrix[3][0]!=' ' and matrix[3][0]==matrix[3][1]==matrix[3][2]==matrix[3][3]=='X':
        print("Player 1 wins")
        return 1  
    if matrix[0][3]!=' ' and matrix[0][3]==matrix[1][3]==matrix[2][3]==matrix[3][3]=='X':
        print("Player 1 wins")
        return 1
    ##
    if matrix[0][0]!=' ' and matrix[0][0]==matrix[0][1]==matrix[0][2]==matrix[0][3]=='o':
        print("Player 2 wins")
        return 1
    if matrix[1][0]!=' ' and matrix[1][0]==matrix[1][1]==matrix[1][2]==matrix[1][3]=='o':
        print("Player 2 wins")
        return 1
    if matrix[2][0]!=' ' and matrix[2][0]==matrix[2][1]==matrix[2][2]==matrix[2][3]=='o':
        print("Player 2 wins")
        return 1
    if matrix[0][0]!=' ' and matrix[0][0]==matrix[1][0]==matrix[2][0]==matrix[3][0]=='o':
        print("Player 2 wins")
        return 1
    if matrix[0][1]!=' ' and matrix[0][1]==matrix[1][1]==matrix[2][1]==matrix[3][1]=='o':
        print("Player 2 wins")
        return 1
    if matrix[0][2]!=' ' and matrix[0][2]==matrix[1][2]==matrix[2][2]==matrix[3][3]=='o':
        print("Player 2 wins")
        return 1
    if matrix[0][0]!=' ' and matrix[0][0]==matrix[1][1]==matrix[2][2]==matrix[3][3]=='o':
        print("Player 2 wins")
        return 1
    if matrix[0][3]!=' ' and matrix[0][3]==matrix[1][2]==matrix[2][1]==matrix[3][0]=='o':
        print("Player 2 wins")
        return 1
    if matrix[3][0]!=' ' and matrix[3][0]==matrix[3][1]==matrix[3][2]==matrix[3][3]=='o':
        print("Player 2 wins")
        return 1  
    if matrix[0][3]!=' ' and matrix[0][3]==matrix[1][3]==matrix[2][3]==matrix[3][3]=='o':
        print("Player 2 wins")
        return 1
    return 0
print("Positions for reference\n")
print("  1 |  2 |  3 |  4","---- ---- ---- ----","  5 |  6 |  7 |  8","---- ---- ---- ----","  9 | 10 | 11 | 12" ,"---- ---- ---- ----"," 13 | 14 | 15 | 16",sep="\n")
print("\n\n")

matrix=[
    [' ',' ',' ',' '],
    [' ',' ',' ',' '],
    [' ',' ',' ',' '],
    [' ',' ',' ',' ']
    ]
for i in range(16):
    print_matrix(matrix)
    print("\n\n")
    if i%2==0:
        print("Player 1 turn")
        pos=int(input("Enter the position you want to play X: "))
        i,j=(pos-1)//4,(pos-1)%4
        while pos>16 or pos<0 or matrix[i][j]!=' ':
            pos=int(input("Enter a valid position: "))
            i,j=(pos-1)//4,(pos-1)%4
        matrix[i][j]='X'
    else:
        print("Player 2 turn")
        pos=int(input("Enter the position you want to play o: "))
        i,j=(pos-1)//4,(pos-1)%4
        while matrix[i][j]!=' ':
            pos=int(input("Enter a valid position: "))
            i,j=(pos-1)//4,(pos-1)%4
        matrix[i][j]='o'
    print("\n")
    if check(matrix):
        break
else:
    print("Draw")
   
