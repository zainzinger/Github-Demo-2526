#  Copyright (c) 2026. Harald Zainzinger, HTL Rennweg
"""
Demonstriere was in der Github CI/CD-Pipeline passiert, wenn
* ein nicht benötigter import vorhanden ist
* Formatierung nicht passt
* ein Testfall fehlschlägt
"""

#import math


def count_lines( text ):
    """
    >>> count_lines('a  b c')
    4
    """
    return len(
        text.split()
    )


if __name__ == "__main__":


    print(count_lines("a   b   c"))
