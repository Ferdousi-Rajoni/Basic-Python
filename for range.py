exp = [2340, 2500, 2100, 3100, 2980]
total=0
for i in range (len(exp)):
    print('Month:',(i+1),'Expenses:',exp[i])
    total=total+exp[i]

    print("My total expenses is",total)

