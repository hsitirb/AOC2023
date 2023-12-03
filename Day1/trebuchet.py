def line_value(line):
    num_dict = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
    line_nums = []
    for idx in range(len(line)):
        if line[idx].isnumeric():
            line_nums.append((idx, line[idx]))
        else:
            for key, val in num_dict.items():
                if line[idx:idx + len(key)] == key:
                    line_nums.append((idx, val))
    line_nums.sort()
    num = line_nums[0][1] + line_nums[-1][1]
    return int(num)

def lines_result(lines):
    return sum(line_value(line) for line in lines.splitlines())


if __name__ == "__main__":
    with open("Day1/puzzle_input.txt") as file:
        lines = file.read()
    print(lines_result(lines))
