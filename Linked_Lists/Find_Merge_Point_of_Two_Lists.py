
def findMergeNode(headA, headB):
    curA = headA
    curB = headB
    while not curA == curB:
        if curA.next is None:
            curA = headB
        else:
            curA = curA.next
        if curB.next is None:
            curB = headA
        else:
            curB = curB.next
    return curA.data






