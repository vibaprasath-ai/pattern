def pattern(rows):
    for i in range(1,rows+1):
        for j in range(rows-i):
            print(" ",end="")

        for k in range(i):
            print("* ",end="")

        print()

row = int(input("Enter Number Of Rows:"))
pattern(row)