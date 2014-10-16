hello_str = "Hello, world!"
vowel_str = ""
consonant_str = ""
for index in range(len(hello_str)):
    if hello_str[index] in "aeiou":
        vowel_str += hello_str[index]
    else:
        consonant_str += hello_str[index]

print("vowels:", vowel_str)
print("consonants:", consonant_str)
