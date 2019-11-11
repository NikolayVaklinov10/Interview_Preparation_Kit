
def isBalanced(s):
    match = {')': '(', ']': '[', '}': '{', }
    stack = []
    for c in s.strip():
        if c in match.values():
            stack.append(c)
        else:
            if stack and stack[-1] == match[c]:
                stack.pop()
            else:
                return 'NO'
    return 'YES' if len(stack) == 0 else 'NO'










