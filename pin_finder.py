import itertools


def get_pins(observed):
    numbers = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [None, 0, None]]
    options = []
    result = []
    for num in observed:
        pos1 = pos2 = None
        current_options = num
        num = int(num)
        for row in numbers:
            if num in row:
                pos1, pos2 = numbers.index(row), row.index(num)
        for dx, dy in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
            x, y = pos1 + dx, pos2 + dy
            if 0 <= x < len(numbers) and 0 <= y < len(numbers[0]) and numbers[x][y] is not None:
                current_options += (str(numbers[x][y]))
        options.append(current_options)
    for a in list(itertools.product(*options)):
        result.append("".join(list(a)))
    return result


get_pins("123")
