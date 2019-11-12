def decodeHuff(root , s):
   #Enter Your Code Here
    temp=root
    string=[]
    for i in s:
        c=int(i)
        if c==1:
            temp=temp.right
        elif c==0:
            temp=temp.left
        if temp.right == None and temp.left==None:
            string.append(temp.data)
            temp=root
    b=''.join(string)
    print(b)





