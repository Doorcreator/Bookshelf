# Huffman coding algorithm
# ref:
# https://www.geeksforgeeks.org/huffman-coding-greedy-algo-3/
# https://www.techiedelight.com/huffman-coding/
# https://www2.cs.duke.edu/csed/poop/huff/info/
# https://www.huffmancoding.com/my-uncle/huffman-algorithm
# http://bhrigu.me/blog/2017/01/17/huffman-coding-python-implementation/
from ALG019_priority_queue_nb import PriorityQueue
import re
# A class for Huffman tree building.
class TreeNode():
    def __init__(self,value,key):
        self.value = value
        self.key = key
        self.left = None
        self.right = None
# To calculate frequency of each character in a string.
def gen_charfreq(string):
    charfreq = {}
    for char in string:
        charfreq.setdefault(char,0)
        charfreq[char] += 1
    return charfreq
# To build a Huffman tree using priority queue.
def huffman_tree(charfreq):
    charfreq = sorted(charfreq.items(),key = lambda item:item[1])
    heap = []
    pq = PriorityQueue()
    for item in charfreq:
        node = TreeNode(item[1],item[0])
        pq.sift_up_min(heap,(node.value,node))
    while len(heap) > 1:
        root = TreeNode(None,None)
        node01 = pq.extract_min(heap)[0].key
        node02 = pq.extract_min(heap)[0].key
        root.left,root.right = node01,node02
        root.value = node01.value + node02.value
        pq.sift_up_min(heap,(root.value,root))
    return root
encd_dict = {}
# To generate an encoding dictionary.
def gen_encd_dict(root,code):
    if root.left == root.right == None:
        encd_dict[root.key] = code
    else:
        gen_encd_dict(root.left,code+'0')
        gen_encd_dict(root.right,code+'1')
    return encd_dict
# To encode a string with the encoding dict generated above.
def encode_char(string):
    charfreq = gen_charfreq(string)
    root = huffman_tree(charfreq)
    encd_dict = gen_encd_dict(root,'')
    encd_str = []
    while len(string) > 0:
        for char in encd_dict:
            match_obj = re.match(char,string)
            if match_obj != None:
                encd_str.append(encd_dict[match_obj.group()])
                string = string.replace(match_obj.group(),'',1)
    return ''.join(encd_str),encd_dict
# To decode a string with a decoding dict generated based on the encoding dict.
def decode_char(encoded_char,encd_dict):
    decd_dict = {}
    for item in encd_dict.items():
        decd_dict[item[1]] = item[0]
    decd_str = []
    while len(encoded_char) > 0:
        for code in decd_dict:
            match_obj = re.match(code,encoded_char)
            if match_obj != None:
                decd_str.append(decd_dict[match_obj.group()])
                encoded_char = encoded_char.replace(match_obj.group(),'',1)
    return ''.join(decd_str)
str = 'Huffman coding is a data compression algorithm.'
# str = '0021101567'
if __name__=='__main__':
    ecd = encode_char(str)
    dec = decode_char(ecd[0],ecd[1])
    print('Original string:\n%s'%str+'\n'*2+'Huffman codes:\n%s'%ecd[1]+'\n'*2+'Encoded string:\n%s'%ecd[0]+'\n'*2+'Decoded string:\n%s'%dec)
