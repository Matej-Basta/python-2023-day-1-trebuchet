try:
    with open('input.txt', "r") as input_file:
        with open('output.txt', "w") as output_file:
            combinations = []
            for line in input_file.readlines():
                digits = []
                for character in line:
                    if character.isdigit():
                        digits.append(character)
                combinations.append(digits[0] + digits[-1])
            result = 0
            for combination in combinations:
                result += int(combination) 
            print(result)
            output_file.write(str(result))

except FileNotFoundError as file_not_found_error:
    print("File not found!")
except IndexError as index_error:
    print("There were no digits in the line.")