''''
# Defining two lists (numbers and words)
list1 = [3,4,5,6,7]
list2 = ["hello", "world"]

## Display Examples:
# Output World
print(list2[1])

# Outup 5
print(list1[2])

# Change values in a list
# Access the list via the ID
list2[0] = "Goodbye"
print(list2[0])


# Using a loop with a list
for num in list1:
    #printing elements - list remains unchanged
    #print(num)

    #popping an element removes it, but it lets you access it
    print(list1.pop())
    print(list1)
