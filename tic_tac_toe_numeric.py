def print_matrix(matrix):
    for i in range(2):
        print(" ",end="")
        print(matrix[i][0],matrix[i][1],matrix[i][2],sep=" | ")
        print("--- --- ---")
    print(" ",end="")
    print(matrix[2][0],matrix[2][1],matrix[2][2],sep=" | ")

def check(matrix):
    if matrix[0][0]!=" "and matrix[0][1]!=' ' and matrix[0][2]!=' ' and matrix[0][0]+matrix[0][1]+matrix[0][2]==15:
        return 1
        
    if matrix[1][0]!=' 'and matrix[1][1]!=' ' and  matrix[1][2]!=' ' and matrix[1][0]+matrix[1][1]+matrix[1][2]==15:
        return 1
        
    if matrix[2][0]!=' ' and matrix[2][1]!=' 'and matrix[2][2]!=' ' and matrix[2][0]+matrix[2][1]+matrix[2][2]==15:
        return 1
        
    if matrix[0][0]!=' 'and  matrix[1][0]!=' ' and matrix[2][0]!=' ' and matrix[0][0]+matrix[1][0]+matrix[2][0]==15:
        return 1
        
    if matrix[0][1]!=' 'and  matrix[1][1]!=' ' and matrix[2][1]!=' ' and matrix[0][1]+matrix[1][1]+matrix[2][1]==15:
        return 1
        
    if matrix[0][2]!=' 'and  matrix[1][2]!=' ' and matrix[2][2]!=' ' and matrix[0][2]+matrix[1][2]+matrix[2][2]==15:
        return 1
        
    if matrix[0][0]!=' 'and  matrix[1][1]!=' ' and matrix[2][2]!=' ' and matrix[0][0]+matrix[1][1]+matrix[2][2]==15:
        return 1
        
    if matrix[0][2]!=' 'and matrix[1][1]!=' ' and matrix[2][0]!=' ' and matrix[0][2]+matrix[1][1]+matrix[2][0]==15:
        return 1
        
    ##
print("Positions for reference\n")
print(" 1 | 2 | 3","--- --- ---"," 4 | 5 | 6","--- --- ---"," 7 | 8 | 9",sep="\n")
print("\n\n")

matrix=[
    [' ',' ',' '],
    [' ',' ',' '],
    [' ',' ',' ']
    ]
odd=[]
even=[]
for t in range(9):
    print_matrix(matrix)
    print("\n\n")
    if t%2==0:
        print("Player 1 turn")
        pos=int(input("Enter the position you want to play Odd: "))
        i,j=(pos-1)//3,(pos-1)%3
        while pos>9 or pos<0 or matrix[i][j]!=' ':
            pos=int(input("Enter a valid position: "))
            i,j=(pos-1)//3,(pos-1)%3
        val=int(input("Enter the value you want to enter: "))    
        while(val>9 or val<0 or val%2==0 or val in odd):
            val=int(input("Enter the valid value: "))
             
        matrix[i][j]=val
        odd.append(val)
        if check(matrix):
            print("Player 1 wins")
            break
    else:
        print("Player 2 turn")
        pos=int(input("Enter the position you want to play Even: "))
        i,j=(pos-1)//3,(pos-1)%3
        while matrix[i][j]!=' ':
            pos=int(input("Enter a valid position: "))
            i,j=(pos-1)//3,(pos-1)%3
        val=int(input("Enter the value you want to enter: "))
        while(val>9 or val<0 or val%2!=0 or val in even):
            val=int(input("Enter the valid value: "))
             
        matrix[i][j]=val
        even.append(val)
        if check(matrix):
            print("Player 2 wins")
            break
    print("\n")
else:
    print("Draw")
s
