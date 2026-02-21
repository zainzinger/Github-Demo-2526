#  Copyright (c) 2026. Harald Zainzinger, HTL Rennweg
# import doctest


def      count_lines(   text  : str  ) -> int:
    """
    >>> print(2 + 1)
    3
    """
    return len(text.split("\n"))

if __name__ == '__main__':

    print(count_lines('a \n b \n c'))