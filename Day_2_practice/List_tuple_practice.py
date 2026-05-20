# WAP to take the input from the user enter the names of the three faviourate movies and store them in the list
Movies = []

Movies.append(str(input("Enter the Movie 1 : ")))
Movies.append(str(input("Enter the Movie 2 : ")))
Movies.append(str(input("Enter the Movie 3 : ")))


print(Movies)


# WAP to check the list contains the palidrome items or not

List1 = []
List1.append(input("Enter the value in the list at index 1 : "))
List1.append(input("Enter the value in the list at index 2 : "))
List1.append(input("Enter the value in the list at index 3 : "))
List1.append(input("Enter the value in the list at index 4 : "))
List1.append(input("Enter the value in the list at index 5 : "))

List2 = List1.copy()
List2.reverse()
if(List1 == List2):
    print("The List is palidrome")
else:
    print("List is not Palidrome ")


# count the No. of the students with a grade in the class
Grade_List = []
No_of_students = int(input("Enter the No. of the students : "))
for x in range(No_of_students):
  Grade_List.append(input(f"Enter The Grade for the student {x+1} : "))

Grade_List.sort()
Grade_tuple =(Grade_List)
Count_grade = str(input("Enter the Grade You want to count in the class :  "))
print(Grade_tuple.count(Count_grade))
