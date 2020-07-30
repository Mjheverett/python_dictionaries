input_string = input("Please enter a sentence: ")
string_dictionary = {}
input_words = input_string.split()

for i in range(len(input_words)):
    letter = str(input_words[i])
    if letter in string_dictionary:
        string_dictionary[letter] += 1
    else:
        string_dictionary[letter] = 1

print(string_dictionary)