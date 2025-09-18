num = input()

try:
    num = int(num)
    if (int(num) > 0):
        print("This number is Positive.")
    elif (int(num) < 0):
        print("This number is Negative.")
    elif (int(num) == 0):
        print("This number is both Positibe and Negative.")

except:
    print("This is not number.")
