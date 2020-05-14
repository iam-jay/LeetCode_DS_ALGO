"""
For each place to put the comma, we separate the string into two 
fragments. For example, with a string like "1234", 
we could separate it into fragments "1" and "234", 
"12" and "34", or "123" and "4".
Then, for each fragment, we have a choice of where to 
put the period, to create a list make(...) of choices. 
For example, "123" could be made into "1.23", "12.3", or "123".
Because of extranneous zeroes, we should ignore possibilities 
where the part of the fragment to the left of the decimal starts 
with "0" (unless it is exactly "0"), and ignore 
possibilities where the part of the fragment to the right of 
the decimal ends with "0", as these are not allowed.
"""
import itertools


def ambiguous_coordinates(s: str) -> list[str]:
    def make_left_right(s: str):
        n = len(s)
        for i in range(1, n+1):
            left = s[:i]
            right = s[i:]
            if (not left.startswith('0') or left == '0') and not right.endswith('0'):
                yield left + ("." if i != n else '') + right
    s = s[1:-1]
    return ["({}, {})".format(*cord) for i in range(1, len(s)) for cord in itertools.product(make_left_right(s[:i]),
                                                                                             make_left_right(s[i:]))]
