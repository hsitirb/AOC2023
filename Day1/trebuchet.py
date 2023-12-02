def line_value(line):
    line_nums = list(val for val in line if val.isnumeric())
    num = line_nums[0] + line_nums[-1]
    return int(num)

def lines_result(lines):
    return sum(line_value(line) for line in lines.splitlines())