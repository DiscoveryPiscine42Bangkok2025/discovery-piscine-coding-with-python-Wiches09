age = input("Tell ur age: ")

try:
    age = int(age)
    if (age >= 0):
        print("You are", age, "years old.")
        print("In 10 years, you'll be", age+10, "years old")
        print("In 20 years, you'll be", age+20, "years old")
        print("In 30 years, you'll be", age+30, "years old")

except:
    print("this is not a number")
