def capitalize_first_letter(input_string):
    words = input_string.split()
    capitalized_words = [word.capitalize() for word in words]
    result_string = ' '.join(capitalized_words)
    return result_string
input_str = input()
output_str = capitalize_first_letter(input_str)
print(output_str)