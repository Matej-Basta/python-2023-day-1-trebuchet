from digits import Digits

try:
    with open('input.txt', "r") as input_file:
        with open('output.txt', "w") as output_file:
            combinations = []
            for line in input_file.readlines():
                values = {}
                for spelled_digit in Digits:
                    if spelled_digit.name in line:
                        values[line.find(spelled_digit.name)] = spelled_digit.value
                        values[line.rfind(spelled_digit.name)] = spelled_digit.value
                for index, character in enumerate(line):
                    if character.isdigit():
                        values[index] = character
                min_key = min(values.keys())
                max_key = max(values.keys())
                combinations.append(values[min_key] + values[max_key])
            result = 0
            for combination in combinations:
                result += int(combination) 
            print(result)
            output_file.write(str(result))
except FileNotFoundError as file_not_found_error:
    print("File not found!")
except IndexError as index_error:
    print("There were no digits in the line.")