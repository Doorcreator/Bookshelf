# Problem: Find three 3-digit numbers (without repeated digits between one and another) (n1,n2,n3) that fit the equation x+y=z, where x=n1,y=n2, and z=n3.
# Solution:
# V01
def dup(n):
    # To divide a 3-digit number into three integers representing the digit each occupies.
    b = n//100
    s = (n-b*100)//10
    g = n-b*100-s*10
    return b,s,g
def test_equ01():
    # To collect the numbers that meet the preset conditions into a list, and then iterate over the numbers to check if they satisfy the equation.
    arr = []
    s = set()
    for m in range(123,988):
        n = set(dup(m))
        if 0 not in n and len(n) == 3:
            arr.append(m)
    for i in arr:
        for j in arr:
            for k in arr:
                try:
                    if len(set(dup(i)+dup(j)+dup(k))) == 9 and i+j==k:
                        s.add((i,j,k))
                except:
                    continue
    return len(s)/2
# V02
cards_in_hand = [1,2,3,4,5,6,7,8,9]
results = set()
flag = {}
box = {}
def test_equ02(cur_pos):
    # To find all the possible permutations formed by 9 unique digits from 1 to 9, and then check if they satisfy the equation.
    # cur_pos must start from 1 when the function is initially called.
    if cur_pos == len(cards_in_hand)+1:
        for i in range(1,len(box)+1):
            if box[1]*100+box[2]*10+box[3] + box[4]*100+box[5]*10+box[6] == box[7]*100+box[8]*10+box[9]:
                results.add(''.join([repr(v) for v in box.values()]))
    else:
        for i in range(0,len(cards_in_hand)):
            if flag.setdefault(i,0) == 0:
                box[cur_pos] = cards_in_hand[i]
                flag[i] = 1
                test_equ02(cur_pos+1)
                flag[i] = 0
    return len(results)/2
# print(test_equ01())
# print(test_equ02(1))
# result: 168
# V01: 245 s
# V02: 11 s
