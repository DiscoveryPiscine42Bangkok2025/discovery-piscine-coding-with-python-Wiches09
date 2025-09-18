num1 = input("First number: ")
num2 = input("Second number: ")

try:
    num1 = int(num1)
    num2 = int(num2)
    print(num1, "+", num2, "=", num1+num2)
    print(num1, "-", num2, "=", num1-num2)
    print(num1, "*", num2, "=", num1*num2)
    print(num1, "/", num2, "=", num1/num2)

except:
    print("error")
