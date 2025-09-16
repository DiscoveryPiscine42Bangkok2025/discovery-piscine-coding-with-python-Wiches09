num = input("Enter a number: ")

try:
    num = int(num)

    for i in range(1, 13):
        print(i, "x", num, "=", i*num)

except:
    print("Not a number!")
