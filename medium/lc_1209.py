"""
create set form given string and from set create possible k size duplicate
Keep removing k size duplicates from string till there is nothing to remove
"""


def remove_duplicates(self, s: str, k: int) -> str:
    distinct = set(list(s))
    to_remove = []
    for item in distinct:
        to_remove.append(item*k)
    to_remove = set(to_remove)
    while True:
        start = s
        for dup in to_remove:
            if dup in s:
                s = s.replace(dup, "")
        if start == s:
            return s
