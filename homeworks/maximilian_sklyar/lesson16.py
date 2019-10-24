import itertools as itr
import re


def Zip(text):
    r = ""
    for k, g in itr.groupby(text):
        r += str(k) + str(len(list(g)))
    return r


def Unzip(text):
    r = ""
    for z in zip(re.findall("\D+", text), re.findall("\d+", text)):
        r += str(z[0]) * int(z[1])
    return r
