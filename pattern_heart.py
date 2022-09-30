for rows in range(6):
    for col in range(7):
        if (rows == 0 and col%3 != 0) or (rows == 1 and col%3 == 0) or (rows-col == 2) or (rows+col == 8):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()