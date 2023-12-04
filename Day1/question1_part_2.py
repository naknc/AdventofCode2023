count = 0
my_list = ["one", "two", "three" ,"four", "five", "six", "seven", "eight", "nine"]
my_new_list = [kelime[::-1] for kelime in my_list] # eno, owt, ...

# Open the file (specify the file name and mode)
with open('/Users/nihanakinci/My Python Projects/AdventofCode2023/Day1/input.txt', 'r') as file:
    # Reading all lines of the file
    lines = file.readlines()

# Printing each line to the screen
for line in lines:

    #------FOR LEFT------
    left = ""
    the_list = ""
   
    for letter in line:    
        #----FOR NUMBER----
        if letter.isdigit():
            left += letter
            break #break for left
        
        #----FOR STRING----
        the_list += letter
        for i,j in enumerate(my_list):
            if j in the_list:
                left += str(i+1)
                break

        if len(left) != 0: #Important: to finalize the for loop
            break
    
    #-----FOR RIGHT-----
    right = ""
    the_list = ""
    
    for letter in reversed(line):
        #----FOR NUMBER----
        if letter.isdigit():
            right += letter 
            break #break for right
        
        #----FOR STRING----
        the_list += letter
        for i,j in enumerate(my_new_list):
            if j in the_list:
                right += str(i+1)
                break

        if len(right) != 0: #Important: to finalize the for loop
            break

    #print("First number from lest", left) FOR TESTING
    #print("First number from right:", right) FOR TESTING
    
    #print(int(left+right)) #Print final number for each line

    #break #Break for first for loop

    count += int(left+right) #Add up of all numbers

print(count) #Sum of all numbers