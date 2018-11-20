"""Input name and print odd characters"""

name=input("Enter name:- ")

#check that name is not blank
while len(name)<=0:
    print("Name is blank, enter again ")
    name=input("Enter name:- ")
#peint oddname characters in the name
print(name[::2])
#print oddname characters in the name
