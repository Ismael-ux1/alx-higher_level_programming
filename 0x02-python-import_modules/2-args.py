#!/usr/bin/python3
if __name__ == "__main__":
    import sys
arguments = sys.argv[1:]
num_arguments = len(arguments)

# print the number of arguments
print(num_arguments, "arguments:")
# print the list of arguments
for i, arg in enumerate(arguments, start=1):
    print(f"{i}: {arg}")
