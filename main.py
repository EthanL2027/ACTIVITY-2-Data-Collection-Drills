def main():
# Part A: Lists

    my_list = ["h", "e", "l", "l", "o"]

    print(my_list)
# The list contains h, e, l, l, o in that order.

    my_list.append("!")

    print(my_list)
# The exclamation mark was added to the end of the list.

    print(len(my_list))
# There are 6 elements in the list.

    print(my_list[4:6])
# The result is ['o', '!'] because indexes 4 and 5 are included.

    print(my_list[4:])
# The result is ['o', '!'], the same as the previous result.

    print(my_list[-2:])
# The result is ['o', '!'] because -2 starts at the second-to-last item.

    my_list.remove("l")
    print(my_list)
# The first "l" was removed, and the second "l" stayed.

    my_list.insert(2, "l")
    print(my_list)
# The "l" was inserted at index 2.

    del my_list[0]
    print(my_list)
# The first element, "h", was removed.

    last_item = my_list.pop()
    print(last_item)
# The removed item is "!".

    print(my_list)
# The list now contains ['e', 'l', 'l', 'o'].

    print(my_list[2])
# The result is "l".

    print("!" in my_list)
# False because the exclamation mark was removed.

    my_list.sort(reverse=True)
    print(my_list)
# The list is now sorted in descending alphabetical order.
# sort() changes the original list and returns None.

    print(sorted(my_list))
# This prints a new list in ascending alphabetical order.

    print(my_list)
# The original list stays in descending order because sorted() does not change it.



#Part B: Tuples

    my_tuple = ("red", "green", "blue")

    print(my_tuple)
# The tuple contains red, green, and blue.

    print(my_tuple[0])
# Prints "red" because index 0 is the first item.

    print(my_tuple[-1])
# Prints "blue" because -1 is the last item.

# my_tuple[1] = "yellow"
# This causes a TypeError because tuples are immutable.
# The tuple cannot be changed after it is created.

    one_item = ("hello",)
    print(one_item)
# The comma makes this a tuple containing one item.

    colors = ("red", "blue", "red", "green", "red")
    print(colors.count("red"))
# Prints 3 because red appears three times.

    print(colors.index("green"))
# Prints 3 because green is at index 3.


#Part C: Sets

    my_set = {"apple", "banana", "cherry"}
    print(my_set)
# The set contains apple, banana, and cherry.
# The order is not guaranteed because sets are unordered.

    my_set.add("orange")
    print(my_set)
# Orange was added to the set.

    my_set.add("banana")
    print(my_set)
# Nothing changed because sets do not allow duplicates.

    my_set.remove("apple")
    print(my_set)
# Apple was removed from the set.

    my_set.discard("pear")
# Nothing happened and no error occurred because pear was not in the set.

    tropical = {"banana", "mango", "papaya"}

    all_fruits = my_set.union(tropical)
    print(all_fruits)
# The result contains all unique items from both sets.
# Banana appears only once because sets do not allow duplicates.


#Part D: Dictionaries

    my_dict = {"name": "Sam", "age": 16, "grade": "11th"}

    print(my_dict)
# The keys are name, age, and grade.
# Their values are Sam, 16, and 11th.

    print(my_dict["age"])
# Prints 16.

# print(my_dict["school"])
# This causes a KeyError because school is not a key in the dictionary.

    my_dict["grade"] = "12th"
    print(my_dict)
# The grade value changed from 11th to 12th.

    my_dict["school"] = "Central High"
    print(my_dict)
# The new key is school, and its value is Central High.

    del my_dict["age"]
    print(my_dict)
# The age key and its value, 16, were removed.

    print(my_dict.get("locker"))
# Prints None because locker does not exist.
# No error occurs when using get() for a missing key.

    for key, value in my_dict.items():
        print(key, "->", value)

# This prints each key and its corresponding value.
# The loop makes it easy to read every entry in the dictionary.









if __name__ == "__main__":
    main()
