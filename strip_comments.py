import re


def strip_comments(strng, markers):
    if not markers:
        return strng
    escaped_markers = re.escape("".join(markers))
    if not strng or len(strng) == 1:
        return ""
    pattern = r"[" + escaped_markers + "]+" + r".*" + r"(?=["+escaped_markers+"]|\n|$)"
    result = "".join(re.split(pattern, strng))
    result = "\n".join([line.rstrip() for line in result.split("\n")])
    return result

strip_comments("  avocados , @ oranges ' @\n= = @ watermelons\nbananas ? # - '\n@ = bananas\n? , avocados apples", ['.', '@', '?', '#', '='])

# FASTER SOLUTION WITH CODEWARS SOLUTIONS HELP
# import re
# def solution(string, markers):
#     return string if not markers else re.sub(f" *[{re.escape(''.join(markers))}].*", "", string, re.MULTILINE)

