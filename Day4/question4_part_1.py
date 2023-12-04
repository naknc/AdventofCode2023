import re

lines = [ line.strip() for line in list(open("input4.txt", "r").readlines())]
#print(lines)

def splitter(line):
    splitted = line.split("|")
    return splitted

def extract_integers(input_string):
    # Define the regular expression pattern to match integers
    integer_pattern = r'\b\d+\b'

    # Use re.findall to find all matches in the input string
    integers = re.findall(integer_pattern, input_string)

    # Convert the matched strings to actual integers
    integers = [int(num) for num in integers]

    return integers

def finder(extracted_left, extracted_right):
    count = 0
    for left in extracted_left[1:]:
        if left in extracted_right:
            count += 1
            
    if count == 0:
        print(0)
        return 0    

    print(2**(count-1))        
    return 2**(count-1)        

final = 0
for line in lines:
    s = splitter(line)
    extracted_left = extract_integers(s[0])
    extracted_right = extract_integers(s[1])
    final += finder(extracted_left, extracted_right)

print(final)


    