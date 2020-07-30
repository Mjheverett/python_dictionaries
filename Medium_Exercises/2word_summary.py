input_string = input("Please enter a sentence: ")

string_dictionary = {}

for i in range(len(input_string)):
    letter = str(input_string[i])
    if letter in string_dictionary:
        string_dictionary[letter] += 1
    else:
        string_dictionary[letter] = 1

print(string_dictionary)