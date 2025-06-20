def count_characters(input_str):
    vowels = "aeiouAEIOU"
    digits = "0123456789"
    
    vowel_count = 0
    consonant_count = 0
    digit_count = 0
    special_char_count = 0

    for char in input_str:
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
        elif char.isdigit():
            digit_count += 1
        elif not char.isspace():  # ignore spaces
            special_char_count += 1

    print("Vowels:", vowel_count)
    print("Consonants:", consonant_count)
    print("Digits:", digit_count)
    print("Special Characters:", special_char_count)

# Example usage
user_input = input("Enter a string: ")
count_characters(user_input)