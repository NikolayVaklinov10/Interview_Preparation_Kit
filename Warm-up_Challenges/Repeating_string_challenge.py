import math
import os
import random
import re
import sys
import pandas as pd

# Complete the repeatedString function below.


def repeatedString(s, n):
    return s.count('a') *( n//(len(s))) + s[:(n%(len(s)))].count('a')




















