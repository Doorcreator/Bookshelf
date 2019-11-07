# 火柴拼字游戏
def max_num(n):
    return eval('1'*(n>>1))
def used_match(n):
    dic = {'0':6,'1':2,'2':5,'3':5,'4':4,'5':5,'6':6,'7':3,'8':7,'9':6}
    n = repr(n)
    ms = 0
    for i in range(len(n)):
        ms += dic[n[i]]
    return ms
def scrabble_equ(num_of_matchsticks):
    results = set()
    if num_of_matchsticks < 9:
        return 'No enough matches!'
    avail_matchstick = num_of_matchsticks - 4
    max_n = max_num(avail_matchstick)
    for i in range(0,max_n+1):
        if used_match(i) > avail_matchstick:
            break
        for j in range(0,max_n+1):
            if used_match(j) > avail_matchstick:
                break
            k = i + j
            try:
                if used_match(i) + used_match(j) + used_match(k) == avail_matchstick and k <= max_n:
                    results.add((i,j,k))
            except:
                continue
    results = sorted(results,key=lambda x:x[0])
    return results,len(results)

print(scrabble_equ(22))
