import os
import sys
from tabulate import tabulate


if len(sys.argv) < 2:
    print("Please vi trenger input")
    sys.exit()
bitmap = sys.argv[1]

bitmap = list(map(lambda x: int(x), bitmap.split(" ")))


unique_values = sorted(set(bitmap))
arr = []
for val in unique_values:
    arr.append([val])


for index, val in enumerate(arr):
    for bit in bitmap:
        if val[0] == bit:
            arr[index].append(1)
        else:
            arr[index].append(0)


print("Bitmap for each possible value\n")
print(tabulate(arr, headers=bitmap))

print("\nRun length encoding:")


def count_run_length(arr):
    output = f"{arr[0]}: "
    count_symbol = 0
    counter = 0
    i = 1
    while i < len(arr):
        if arr[i] == count_symbol:
            counter += 1
            i += 1
        else:
            if count_symbol == 0:
                count_symbol = 1
                output += f"{counter} zeroes, "
            else:
                count_symbol = 0
                output += f"{counter} ones, "
            counter = 0
    if count_symbol == 1:
        output += "rest ones"
    else:
        output = output[:-2]
        # output += "rest zeroes" # Optional but not needed
    print(output)


for val in arr:
    count_run_length(val)
