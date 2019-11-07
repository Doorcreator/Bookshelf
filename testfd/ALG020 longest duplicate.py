import re
term = {}
def incword(text):
    # To match words in a string and return a dict containing all the words identified.
    matched_obj = re.finditer(r'\w+',text,re.A)              # match English characters only
    # matched_obj = re.finditer(r'[\u4e00-\u9fa5]+',text)    # match non-English characters only
    # matched_obj = re.finditer(r'[^\x00-\xff]+',text)       # match Chinese characters only
    for obj in matched_obj:
        wd = obj.group()
        term.setdefault(wd,0)
        term[wd]+=1
    # uncomment the following two lines to return a sorted term list
    # sorted_termlist=sorted(term.items(),key = lambda x:x[1])
    # return sorted_termlist
    return term
def extract_wdfrq(path):
    # To generate a word frequency list based on a file in a specific path.
    with open(path,'r', encoding = 'utf-8') as fr:
        lines = fr.readlines()
        for line in lines:
            term = incword(line)
    # sorted_termlist=sorted(term.items(),key = lambda x:x[1],reverse = True)
    # uncomment the following lines to write the sorted term list into a file on the disk.
    # pathw = ''.join([path.split('.')[0],'_wdfrq.',path.split('.')[1]])
    # with open(pathw,'w', encoding = 'utf-8') as fw:
        # for wdtpl in sorted_termlist:
            # wdc = ''.join([wdtpl[0],'\t',repr(wdtpl[1]),'\n'])
            # fw.write(wdc)
    # return sorted_termlist
    return term
def com_len(str01,str02):
    # To identify the maximum length of a substring shared by two strings starting with the same character.
    max_len = 0; i = 1; j = 1
    while max_len<len(str01) and str01[:i]==str02[:j]:
        i += 1
        j += 1
        max_len += 1
    return max_len
def com_len02(str01,str02):
# To identify the maximum length of a substring shared by two strings, not necessarily starting with the same character.
    max_len = -1
    for i in range(len(str01)):
        for j in range(len(str02)):
            if str01[i] == str02[j]:
                curr_len = com_len(str01[i:],str02[j:])
                if curr_len > max_len:
                    max_len = curr_len
                    max_i = i
    return str01[max_i:max_i+max_len]
def com_len_beta(str01,str02):
    # Another version of com_len, but not as efficient as com_len.
    s_str,l_str,n1,n2 = (str01,str02,len(str01),len(str02)) if len(str01)<len(str02) else (str02,str01,len(str02),len(str01))
    arr = {}
    substr = ''
    for k in range(len(s_str),0,-1):
        for i in range(len(s_str)):
            for j in range(len(l_str)-k+1):
                if s_str[i:i+k] == l_str[j:j+k]:
                    if s_str[i:i+k] in substr:
                        continue
                    else:
                        substr = s_str[i:i+k]
                        arr[substr] = len(substr)
                        break
    sorted_str = sorted(arr.items(),key=lambda x:x[1],reverse=True)
    return sorted_str[0][1]
def com_len_dic(dic01,i,dic02,j):
    # To identify the maximum length of a substring shared by two dicts of strings.
    # i: start position of common substring in dict01
    # j: start position of common substring in dict02
    max_len = 0
    pre_surpl = -1 # additional common characters before the first common string.
    post_surpl = 1 # additional common characters after the last common string.
    try:
        while abs(pre_surpl)<=len(dic01[i-1][pre_surpl:]) and dic01[i-1][pre_surpl:] == dic02[j-1][pre_surpl:]:
            pre_surpl -= 1
        while dic01[i]==dic02[j]:
            i += 1
            j += 1
            max_len+=1
        while dic01[i][:post_surpl] == dic02[j][:post_surpl]:
            post_surpl += 1
        pre_surpl += 1
        post_surpl -= 1
    except KeyError:
        pre_surpl += 1
        post_surpl -= 1
    return max_len,abs(pre_surpl)+post_surpl,pre_surpl,post_surpl
def merge_lines(path):
    # To merge all the lines in a file in a path into a single string.
    m = []
    with open(path,'r', encoding = 'utf-8') as fr:
        lines = fr.readlines()
        for line in lines:
            new_line = line.strip()
            m.append(new_line)
    merged_str = ' '.join(m)
    return merged_str
def hash_char(string):
    # To convert a string to its hash value.
    h = 0
    hash_size = 14879
    for c in string:
        h = h*31+ ord(c)
    return h%hash_size
def hash_regex_char(string):
    # To convert a string to its hash value, intended to be used in combination with re.sub().
    string = string.group()
    h = 0
    hash_size = 14879
    for c in string:
        h = h*31+ ord(c)
    return repr(h%hash_size)
def hashify(text):
    # To convert a large body of text into hashed form. Words shall be converted to their hash values, while other characters shall be left as they are.
    hashed_text = re.sub(r'\w+',hash_regex_char,text)
    return hashed_text
def str2dic(string):
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
            dic[k] = string[0]
            k += 1
            string = string[1:]
    return dic
def str2suf_arr01(string):
    # To generate a sorted suffix array based on a string.
    total_bytes = len(string)
    sub_str = {}
    norm_unit = 800
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
        j = 0
        while j<len(key):
            suf[i]=key[j:].strip()
            if i>0 and suf[i] == suf[i-1]:
                del suf[i-1]
            i += 1
            j += 1
    suf_dic = sorted(suf.items(),key = lambda x:x[1])
    return suf_dic
def gen_word_list(string):
    terms = set()
    matched_obj = re.finditer(r'\w+',string,re.A)
    for obj in matched_obj:
        wd = obj.group()
        terms.add(wd)
    return terms
def str2suf_arr02(string):
    # To generate a sorted suffix array based on a string. Only strings containing complete words (instead of part of a word, as in str2suf_arr01) shall be identified.
    total_bytes = len(string)
    sub_str = {}
    norm_unit = 3000
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
        wdlst = gen_word_list(key)
        j = 0
        while j<len(key)-1:
            k_str = key[j:].strip()
            k_str_next = key[j+1:].strip()
            matched_obj = re.match(r'\w+',k_str,re.A)
            if matched_obj:
                next_wd = matched_obj.group()
                if next_wd in wdlst:
                    if k_str != k_str_next:
                        suf[i]=k_str
            j += 1
            i += 1
    suf_dic = sorted(suf.items(),key = lambda x:x[1])
    return suf_dic
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
        wdlst = gen_word_list(key)
        j = 0
        while j<len(key):
            k_str = key[j:]
            matched_obj = re.match(r'\w+',k_str,re.A)
            if matched_obj:
                next_wd = matched_obj.group()
                wd_width = len(next_wd)
                suf[i]=k_str
                i += 1
                j += wd_width
            else:
                j += 1
    suf_dic = sorted(suf.items(),key = lambda x:x[1])
    return suf_dic
# To identify the longest duplicate substring in a string.
# V01
def dup_char01(string):
    arr = {}
    substr = ''
    for i in range(len(string)):
        for k in range(len(string)-1,0,-1):
            for j in range(i+1,len(string)-k+1):
                if string[i:i+k] == string[j:j+k]:
                    if string[i:i+k] in substr:
                        continue
                    else:
                        substr = string[i:i+k]
                        arr[substr] = len(substr)
                        break
    sorted_str = sorted(arr.items(),key=lambda x:x[1],reverse=True)
    return sorted_str[0][0]
# V02
def dup_char02(string):
    max_len = -1
    for i in range(len(string)):
        for j in range(i+1,len(string)):
            if string[i]==string[j]:
                curr_len = com_len(string[i:],string[j:])
                if curr_len > max_len:
                    max_len = curr_len
                    max_i = i
    return string[max_i:max_i+max_len]
# V03
def dup_char03(string):
    d_str = str2dic(string)
    max_str = []
    max_len = (-1,-1,-1)
    for i in range(len(d_str)):
        for j in range(i+1,len(d_str)):
            if d_str[i]==d_str[j]:
                curr_len = com_len_dic(d_str,i,d_str,j)
                if curr_len[0]>max_len[0] and curr_len[1]>=max_len[1]:
                    max_len = curr_len
                    max_i = i
    if max_len[0]<=2:
        return -1
    if max_len[2] != 0:
        max_str.append(d_str[max_i-1][max_len[2]:])
    for t in range(max_len[0]):
        max_str.append(d_str[max_i])
        max_i += 1
    max_str.append(d_str[max_i][:max_len[3]])
    return ''.join(max_str)
# V04
def dup_char04(string):
    suf_dic = str2suf_arr01(string)
    max_len = -1
    for i in range(len(suf_dic)-1):
        curr_len = com_len(suf_dic[i][1],suf_dic[i+1][1])
        if curr_len > max_len:
            max_len = curr_len
            max_i = i
    return suf_dic[max_i][1][:max_len]
# V05
def dup_char05(string):
    # optimized V04, replace str2suf_arr01 with str2suf_arr03, which improves efficiency at the cost of increased granularity, thus making it not applicable for short strings.
    suf_dic = str2suf_arr03(string)
    max_len = -1
    for i in range(len(suf_dic)-1):
        curr_len = com_len(suf_dic[i][1],suf_dic[i+1][1])
        if curr_len > max_len:
            max_len = curr_len
            max_i = i
    return suf_dic[max_i][1][:max_len]

a = 'blackssmellblacksteablackssme'
b = {-1:'u',0:'tpuzxk',1:'g',2:'c',3:'d',4:'e',5:'fker ',6:''}
c = {6:'zxk',7:'g',8:'c',9:'d',10:'e',11:'fk',12:'j',13:'erk',14:'yeo'}
d = 'banar abanary'
e = 'Ask not what your country can do for you, ask what you can do for your country.'
f = 'and let them have dominion over the fish of the sea, and over the fowl of the air, and over the cattle, and over all the earth, and over every creeping thing that creepeth upon the earth. So God created man in his own image, in the image of God created he him; male and female created he them. Ge1:28 And God blessed them, and God said unto them, Be fruitful, and multiply, and replenish the earth, and subdue it: and have dominion over the fish of the sea, and over the fowl of the air, and over every living thing that moveth upon the earth.'
# print(dup_char04(merge_lines(path02)))
# print(dup_char05(merge_lines(path01)))
# print(dup_char05(f))
# print(gen_word_list(f))
# print(com_len02(merge_lines(path03),merge_lines(path04)))
#v02 e:0.0012   f:0.0061    path03: 0.069   path01: 52    path05: 10.5
#      0.008      0.0065            0.073           71            11
# performance: 
# V01 191 s
# V02 0.34 s
# V03 0.15 s
# V04 0.013 s

# Iliad (by Samuel Butler):
# '''a messenger from Jove, who, though he be
# not near, yet takes thought for you and pities you. He bids you get
# the Achaeans instantly under arms, for you shall take Troy. There
# are no longer divided counsels among the gods; Juno has brought them
# over to her own mind, and woe betides the Trojans at the hands of
# Jove. Remember this'''
# Bible(kjv):
# 'the house of his precious things, the silver, and the gold, and the spices, and the precious ointment, and all the house of his armour, and all that was found in his treasures: there was nothing in his house, nor in all his dominion, that Hezekiah shewed them not'
