
def riddle(arr):
    n = len(arr)
    ans = [0] * n
    stack = [0]

    def pop(v):
        nonlocal stack, ans
        i = 1
        while i < len(stack) and stack[-i] > v:
            ans[i-1] = max(ans[i-1], stack[-i])
            stack[-i] = v
            i += 1

    for v in arr:
        if stack[-1] > v:
            pop(v)
        stack.append(v)

    pop(0)
    return ans



