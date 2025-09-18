import sys

args = sys.argv[1:]

if not args:
    print("none")
else:
    printed = False
    for arg in args:
        if not arg.endswith("ism"):
            print(arg+"ism")
            printed = True

    if not printed:
        print("none")
