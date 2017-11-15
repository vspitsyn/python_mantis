from sys import maxsize
import random

def clear_double_space(s):
    index_space = s.find('  ')
    if index_space > -1:
        s = clear_double_space(s[0:index_space] + s[index_space + 1:len(s)])
    return s

def key_one_in_one(list):
    return [int(list[0]),int(list[1])]

def random_strnum(prefix, maxnum):
    return prefix+str(random.randrange(0,maxnum,1))
