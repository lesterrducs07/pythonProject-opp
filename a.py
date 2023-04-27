#conditional statement
age = int(input("please enter your age: "))
height = int(input("please enter your height: "))

if age >= 18 and height >= 150:
    print("legal")
elif age >= 15 and height >= 120:
    print("teen")
elif age >= 5 and height >= 100:
    print("kid")
else:
    print("not applicable")
