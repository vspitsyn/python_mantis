# -*- coding: utf-8 -*-
from model.project import Project
from sys import maxsize
import random

def random_strnum(prefix, maxnum):
    return prefix+str(random.randrange(0,maxnum,1))

testdata = [
    Project(name=random_strnum("New project ",maxsize), status="stable", igc=False, view_status = "private", description = ""),
    Project(name=random_strnum("My project ",maxsize), igc=True, view_status = "public", description = "Project for mantis-test\nSpitsyn V.M.")
    ]


#import random
#import string
# def random_string(prefix, maxlen):
#     symbols = string.ascii_letters+string.digits+string.punctuation+" "*10
#     return prefix+"".join([random.choice(symbols) for i in range(random.randrange(maxlen))])
#
# testdata = [Group(name="", header="", footer=""),
#     Group(name="ИУ6", header="We", footer="Are")]+ [
#     Group(name=random_string("name",10), header=random_string("header",20), footer=random_string("footer",20))
#     for i in range (3)]