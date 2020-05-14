
"""
start with open=0, close=0 brackets and keep opening till max open 
and close whenever open is > close. do backtracking
"""


def generate_parenthesis(n):
    string = [""] * n * 2
    result = []
    _generate_parenthesis(n, 0, 0, 0, string, result)
    return result


def _generate_parenthesis(n, opn, close, pos, string, result):
    if close == n:
        result.append("".join(string))
        return
    else:
        if opn < n:
            string[pos] = "("
            _generate_parenthesis(n, opn+1, close, pos+1, string, result)
        if opn > close:
            string[pos] = ")"
            _generate_parenthesis(n, opn, close+1, pos+1, string, result)
