import sys

if len(sys.argv) != 2:
    print("none")
else:
    word = sys.argv[1]
    result = ""

    for i in word:
        if i == "z":
            result += "z"

    if result:
        print(result)
    else:
        print("none")
