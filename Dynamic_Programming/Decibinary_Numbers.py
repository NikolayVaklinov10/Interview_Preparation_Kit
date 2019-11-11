import os
from collections import defaultdict
from bisect import bisect_right

MAX_NUMBERS = 285113
MAX_ITER = 10
MAX_DIGIT = 19


def get_dec(x):
    result, i = 0, 0
    while x > 0:
        result += (x % 10) * 2 ** i
        x, i = x // 10, i + 1
    return result


def get_matrix(d, j, positions):
    i_for_sum, max_num = 2 ** j, 5 ** (j - 1)
    max_num_last_index, direction = None, 1
    last_el = get_dec(10 ** j - 1)
    shift = 2 ** (j - 1)
    for i in range(shift, len(d)):
        if direction > 0:
            d[i] += d[i - shift]
            if d[i] == max_num:
                direction, max_num_last_index = 0, last_el - i
        elif direction == 0:
            d[i] = max_num
            if i == max_num_last_index:
                direction = -1
        else:
            d[i] = d[last_el - i]
        if i < i_for_sum:
            positions.append(positions[- 1] + d[i])
    return d, positions


def magic_func(result_in_dec, inner_shift, is_first, dcts, result_max_length, result):
    if (result_max_length <= 0):
        return result
    double_shift, sum_bits = 1 << (result_max_length - 1), 0
    for i in range(0, MAX_ITER):
        if i * double_shift <= result_in_dec and (sum_bits + dcts[result_max_length - 1][result_in_dec - i * double_shift] <= inner_shift):
            sum_bits += dcts[result_max_length - 1][result_in_dec - i * double_shift]
        else:
            if not is_first or i > 0:
                result += str(i)
            result = magic_func(result_in_dec - i * double_shift, inner_shift - sum_bits, is_first and i == 0, dcts, result_max_length - 1, result)
            return result
    return result


def decibinaryNumbers(x, dct, dcts, positions):
    if x <= 1:
        return 0
    result_in_dec = bisect_right(positions, x) - 1
    inner_shift = x - positions[result_in_dec]
    result = magic_func(result_in_dec, inner_shift, True, dcts, result_max_length=len(bin(result_in_dec)[2:]), result='')
    return result


def start():
    dct = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1] + [0] * (MAX_NUMBERS - 28)  # 4
    dcts = [[1] + [0] * (MAX_NUMBERS - 1), [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] + [0] * (MAX_NUMBERS - 10), dct]
    j, positions = 2, [1, 2, 3, 5, 7]
    while j < MAX_DIGIT:
        j += 1
        dct, positions = get_matrix(dct[:], j, positions)
        dcts.append(dct)
    return dct, dcts, positions


if __name__ == '__main__':
    dct, dcts, positions = start()
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        x = int(input())

        result = decibinaryNumbers(x, dct, dcts, positions)

        fptr.write(str(result) + '\n')

    fptr.close()
