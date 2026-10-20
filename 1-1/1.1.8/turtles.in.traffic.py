# courses being taken
my_courses = ["English", "Math", "CS"]
print() # blank line
print("Enter your points for " + "English")
print("Enter your points for " + "Math")
print("Enter your points for " + "CS")

redo = "y"
while (redo == "y"):
    for course in my_courses:
        points = int(input("Points -> "))
        if (points >= 90):
            print("A")
        elif (points >= 80):
            print("B")
        elif (points >= 70):
            print("C")
        elif (points >= 60):
            print("D")
        else:
            print("F")

        redo = input("Do you need to re-do these grades? (y/n)")