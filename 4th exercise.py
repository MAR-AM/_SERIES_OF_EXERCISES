n = int(input("Write the age of child : "))
while n <= 0 :
    n = int(input("Write the age (the age will be greater than 6 ) : "))
if n == 6 or n == 7 :
    print("Chick")
elif n == 8 or n == 9 :
    print("Pupil")
elif n == 10 or n == 11 :
    print("small")
elif n > 12 :
    print("Youngest")