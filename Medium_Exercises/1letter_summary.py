input_string = input("Please enter a word: ")

string_dictionary = {}

for i in input_string:
    if i in string_dictionary:
        string_dictionary[i] += 1
    else:
        string_dictionary[i] = 1

print(string_dictionary)