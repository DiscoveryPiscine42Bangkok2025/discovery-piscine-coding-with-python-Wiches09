import sys

word = str(input("What was a parameter? "))

if str(sys.argv[1]) == word:
    print("Good job!")
else:
    print("Nope, sorry...")
