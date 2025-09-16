num = input("Enter a number less than 25")
if (int(num) > 25):
    print("Error")
else:
    for i in range(int(num), 25+1):
        print("Inside the loop, my variable is ", i)
