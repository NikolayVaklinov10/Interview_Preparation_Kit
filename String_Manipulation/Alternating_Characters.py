# SOLUTION 1

# Complete the alternatingCharacters function below.
def alternatingCharacters(s):
    return len([1 for x in range(len(s)-1) if s[x]==s[x+1]])


# SOLUTION 2
import re


def alternatingCharacters(s):
    return len(s)-(len(re.findall('A+|B+',s)))








