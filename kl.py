#-*-coding=utf-8-*-
import sys
import math
#la = sys.stdin.readline().strip().split()
#lb = sys.stdin.readline().strip().split()
la = [1,1,1,2,3,4,1,2,3,4,1,3,4,1,2,3,3,1,2,3,1,2,3,1,3,1]
lb = [2,2,2,2,3,4,4,2,2,1,2,4,3,2,2,1,3,4,4,2,4,3]
da = {}
db = {}
for sample in la:
    if sample not in da:
        da[sample] = 0
    da[sample] += 1
for sample in lb:
    if sample not in db:
        db[sample] = 0
    db[sample] += 1
# º∆À„kl
for key in da:
    da[key] /= float(len(la))
    #print da[key]
for key in db:
    db[key] /= float(len(lb))
    #print db[key]
kl = 0.0
for key in da:
    kl += da[key]* math.log(float(da[key]/db[key]), 2)
print kl