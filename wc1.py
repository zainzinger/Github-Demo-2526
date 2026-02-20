#  Copyright (c) 2026. Harald Zainzinger, HTL Rennweg
import doctest


def count_lines(text):
    """
    >>> count_lines('a \n b \n c')
    3
    """
    return len(text.split("\n"))

if __name__ == '__main__':

    print(count_lines('a \n b \n c'))