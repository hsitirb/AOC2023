def line_value(line):
    num_dict = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
    idx = 0
    while idx < len(line):
        for key in num_dict.keys():
            if line[idx:].startswith(key):
                line = line[:idx] + num_dict[key] + line[idx + len(key):]
                idx += 1
                break
        else:
            idx += 1

    line_nums = list(val for val in line if val.isnumeric())
    num = line_nums[0] + line_nums[-1]
    return int(num)

def lines_result(lines):
    return sum(line_value(line) for line in lines.splitlines())


if __name__ == "__main__":
    with open("Day1/puzzle_input.txt") as file:
        lines = file.read()
    print(lines_result(lines))
