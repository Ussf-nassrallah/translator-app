# translate app that take a string from the user and replace the vowels with 'z' character

def translate(str):
    output = ""
    for letter in str:
        if letter in "aeiou":
            output = output + 'z'
        elif letter in "AEIOU":
            output = output + 'Z'
        else:
            output = output + letter
    return output

user_input = input("Enter a phrase: ")
translate_input = translate(user_input)
print(translate_input)