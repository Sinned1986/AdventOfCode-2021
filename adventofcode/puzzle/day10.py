# Day 10: Syntax Scoring

def read_codelines():
    code_lines = []
    with open('day/10/input.txt') as fv:
        for row in fv:
            code_lines.append(row[:-1])

    return code_lines


def day10a():
    corruption_score , _ = day10()
    return corruption_score


def day10():
    code_lines = read_codelines()
    remaining_stacks = []
    corruption_score = 0

    for i, code_line in enumerate(code_lines):
        stack = []
        add_corruption_score = 0
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
                    add_corruption_score += 3
                    break
            elif char == ']':
                expected_char = stack.pop()
                if char != expected_char:
                    add_corruption_score += 57
                    break
            elif char == '}':
                expected_char = stack.pop()
                if char != expected_char:
                    add_corruption_score += 1197
                    break
            elif char == '>':
                expected_char = stack.pop()
                if char != expected_char:
                    add_corruption_score += 25137
                    break
            else:
                raise Exception('unknown char')

        if add_corruption_score > 0:
            corruption_score += add_corruption_score
        else:
            remaining_stacks.append(stack)

    autocomplete_scores = []
    for remaining_stack in remaining_stacks:
        new_score = 0
        for char in reversed(remaining_stack):
            new_score *= 5
            if char == ')':
                new_score += 1
            if char == ']':
                new_score += 2
            if char == '}':
                new_score += 3
            if char == '>':
                new_score += 4
        autocomplete_scores.append(new_score)

    autocomplete_scores.sort()

    return corruption_score, autocomplete_scores[len(autocomplete_scores)//2]


def day10b():
    _, autocomplete_score = day10()
    return autocomplete_score


if __name__ == '__main__':
    print(day10a())
    print(day10b())
