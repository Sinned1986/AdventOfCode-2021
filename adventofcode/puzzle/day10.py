def read_codelines():
    code_lines = []
    with open('day/10/input.txt') as fv:
        for row in fv:
            code_lines.append(row[:-1])

    return code_lines

def day10a():
    code_lines = read_codelines()
    remaining_stack = []
    score = 0
    for i, code_line in enumerate(code_lines):
        stack = []
        for j, char in enumerate(list(code_line)):
            if char == '(':
                stack.append(')')
            elif char == '[':
                stack.append(']')
            elif char == '{':
                stack.append('}')
            elif char == '<':
                stack.append('>')
            elif char == ')':
                expected_char = stack.pop()
                if char != expected_char:
                    score += 3
                    break
            elif char == ']':
                expected_char = stack.pop()
                if char != expected_char:
                    score += 57
                    break
            elif char == '}':
                expected_char = stack.pop()
                if char != expected_char:
                    score += 1197
                    break
            elif char == '>':
                expected_char = stack.pop()
                if char != expected_char:
                    score += 25137
                    break
            else:
                raise Exception('unknown char')
    remaining_stack.append(stack)
    return score


def day10b():
    pass


if __name__ == '__main__':
    print(day10a())
    print(day10b())
