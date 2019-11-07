import re,random
from ALG008_bisearch_v2 import bi_search02
from ALG020_longest_duplicate import *
def str2dic02(string):
    # To convert a string to a dict with each word (or other character) in the form of a key-value pair.
    dic = {}
    k = 0
    while len(string)>0:
        matched_obj = re.match(r'\w+',string)
        if matched_obj:
            dic[k] = matched_obj.group()
            k += 1
            string = string[matched_obj.span()[1]:]
        else:
            if string[0] != ' ':
                dic[k] = string[0]
                k += 1
            string = string[1:]
    return dic
def gen_word_list(string):
    terms = set()
    matched_obj = re.finditer(r'\w+',string,re.A)
    for obj in matched_obj:
        wd = obj.group()
        terms.add(wd)
    return terms
def com_len(str01,str02):
    # To identify the maximum length of a substring shared by two strings starting with the same character.
    max_len = 0; i = 1; j = 1
    while max_len<len(str01) and str01[:i]==str02[:j]:
        i += 1
        j += 1
        max_len += 1
    return max_len
def str2suf_arr03(string):
    # To generate a sorted suffix array based on a string. Only strings containing complete words (instead of part of a word, as in str2suf_arr01) shall be identified.
    total_bytes = len(string)
    sub_str = {}
    norm_unit = 4000
    start = 0
    end = norm_unit
    if total_bytes > norm_unit:
        n = total_bytes//norm_unit + 1
        for k in range(n):
            sub_str[k] = string[start:end]
            start += norm_unit
            end += norm_unit
    else:
        sub_str[0] = string
    suf = {}
    i = 0
    for key in sub_str.values():
        # wdlst = gen_word_list(key)
        j = 0
        # print('wdlst:%s'%wdlst)
        # print('i:%s,j:%s'%(i,j))
        while j<len(key):
            k_str = key[j:]
            matched_obj = re.match(r'\w+',k_str,re.A)
            # print('k_str:%s'%k_str)
            # print('matched_obj:%s'%matched_obj)
            if matched_obj:
                next_wd = matched_obj.group()
                # print('next_wd:%s'%next_wd)
                wd_width = len(next_wd)
                # suf[i]=k_str
                suf[i]=str2dic02(k_str)
                # print('suf[%s]:%s'%(i,suf[i]))
                i += 1
                j += wd_width
            else:
                if k_str[0] != ' ':
                    suf[i]=str2dic02(k_str)
                    # print('suf[%s]:%s'%(i,suf[i]))
                    i += 1
                    j += 1
                else:
                    j += 1
    suf_dic = sorted(suf.items(),key = lambda x:x[1][0])
    # print('suf:%s'%suf)
    # print('suf_dic:%s'%suf_dic)
    return suf_dic
a = [-11,-8,-6,-5,3,8,9,13,13,13,15,17]
e = 'Ask not what your country can do for you, ask what you can do for your country.'
f = 'of the people, by the people, for the people.'
g = 'the house of his precious things, the silver, and the gold'
gen_txt = []
def gen_rand_txt(curr_wd,base_txt):
    wd_dic = str2suf_arr03(base_txt)
    # print('wd_dic:%s'%wd_dic)
    init_wd_lst = [w[1][0] for w in wd_dic]
    # print('init_wd_lst:%s'%init_wd_lst)
    pos = bi_search02(curr_wd,init_wd_lst)
    # print('pos:%s'%pos)
    wd_occur = init_wd_lst.count(curr_wd)
    rand_pos = pos + random.randint(0,wd_occur-1)
    # print('rand_pos:%s'%rand_pos)
    # print('wd_dic[%s][1]:%s'%(rand_pos,wd_dic[rand_pos][1]))
    if len(wd_dic[rand_pos][1])>1:
        next_wd = wd_dic[rand_pos][1][1]
    else:
        next_wd = wd_dic[rand_pos][1][0]
    # print('curr_wd:%s'%curr_wd)
    gen_txt.append(curr_wd)
    # print('next_wd:%s'%next_wd)
    curr_wd = next_wd
    while curr_wd != '.':
        return gen_rand_txt(curr_wd,base_txt)
    return gen_txt
# for i in range(5):
# gen_txt = []
# print(gen_rand_txt('the',g))
# str2suf_arr03(e)