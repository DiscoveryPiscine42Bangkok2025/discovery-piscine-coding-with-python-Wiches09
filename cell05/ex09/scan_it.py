import sys

if len(sys.argv) != 3:
    print("none")
else:
    keyword = sys.argv[1]
    word = sys.argv[2]
    print(word.count(keyword))
