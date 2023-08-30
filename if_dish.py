bangladeshi=["Illish","Panta"]
indian=["Nan","Dall"]
chinese=["Fried Rice","Chiken"]

dish=input("Enter a dish name:")

if dish in indian:
    print("Indian")
elif dish in bangladeshi:
    print("Bnagladeshi")
elif dish in chinese:
    print("Chinese")
else:
    print("Dont know which cousine is this",dish)




