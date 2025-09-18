num = input("Enter a number: ")
try:
    num = float(num)
    if num.is_integer():
        print("This number is integer.")
    else:
        print("This number is decimal.")

except:
    print("this is not a number.")
