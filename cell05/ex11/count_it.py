import sys

print(f"parameters: {len(sys.argv) - 1}")

for args in sys.argv[1:]:
    print(args, "=", len(args))
