count = 0

# Open the file (specify the file name and mode)
with open(
    "/Users/nihanakinci/My Python Projects/AdventofCode2023/Day1/input.txt", "r"
) as file:
    # Reading all lines of the file
    lines = file.readlines()

# Printing each line to the screen
for line in lines:
    # ------FOR LEFT------
    left = ""

    for letter in line:
        if letter.isdigit():
            left += letter
            break  # break for left

    # -----FOR RIGHT-----
    right = ""
    for letter in reversed(line):
        if letter.isdigit():
            right += letter
            break  # break for right

    # print("Soldan ilk sayı:", left) (FOR TESTING)
    # print("Sağdan ilk sayı:", right) (FOR TESTING)

    # print(int(left+right)) #Print final number for each line

    # break #Break for first for loop

    count += int(left + right)  # Add up of all numbers

print(count)  # Sum of all numbers
