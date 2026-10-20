def main():
# Part A: Lists

# Create a list of letters
my_list = ["e", "t", "h", "a", "n"]

print(my_list)
# The list contains e, t, h, a, n in that order.

# Add an exclamation mark
my_list.append("!")

print(my_list)
# The exclamation mark was added to the end of the list.

# Count the items
print(len(my_list))
# There are 6 elements in the list.

# Get the last two items using positive indexes
print(my_list[4:6])
# The result is ['n', '!'].

# Slice from index 4 to the end
print(my_list[4:])
# The result is ['n', '!'].

# Use negative indexing
print(my_list[-2:])
# The result is ['n', '!'].

# Remove the letter "h"
my_list.remove("h")
print(my_list)
# The letter h was removed from the list.

# Insert "h" back at index 2
my_list.insert(2, "h")
print(my_list)
# The letter h was inserted at index 2.

# Delete the first element
del my_list[0]
print(my_list)
# The first element, e, was removed.

# Remove and save the last item
last_item = my_list.pop()
print(last_item)
# The removed item is "!".

print(my_list)
# The list now contains ['t', 'h', 'a'].

# Print the item at index 2
print(my_list[2])
# The result is "a".

# Check if "!" is in the list
print("!" in my_list)
# False because the exclamation mark was removed.

# Sort the list in reverse order
my_list.sort(reverse=True)
print(my_list)
# The list is sorted in reverse alphabetical order.

# Create a sorted copy
print(sorted(my_list))
# This prints a new list in alphabetical order.

print(my_list)
# The original list stays in reverse alphabetical order.




if __name__ == "__main__":
    main()
