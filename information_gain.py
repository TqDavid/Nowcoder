# -*-coding=utf-8-*-
'''
@Author: tq
决策树实现计算信息增益，ID3-信息增益，C4.5信息增益率
'''
import sys
import math
#N = int(input())
#data = []
#for i in range(0, N):
#    word = map(int, raw_input().split(','))
#    data.append(word)
N = 5
data = [[1,1],[1,1],[2,0], [0,0],[3,0]]
label = {} # 类别的名称为键，类别的值是该类别数目

for sample in data:
    currentLabel = sample[1]
    if currentLabel not in label.keys():
        label[currentLabel] = 0
    label[currentLabel] += 1
    #print currentLabel, label[currentLabel]
Entropy = 0.0
for i in label:
    pi = float(label[i]) / N
    #print pi
    Entropy -= pi * math.log(pi, 2)
print Entropy

# 计算条件熵
# 统计各个属性的计算公式
dic = {}
for sample in data:
    if sample[0] not in dic:
        dic[sample[0]] = [0, 0, 0] # 依次统计属性i的单变量0， 1的数目，以及该属性总共的数目
    if sample[1] == 0:
        dic[sample[0]][0] += 1
    else:
        dic[sample[0]][1] += 1
    dic[sample[0]][2] += 1
#开始计算
pi = 0.0
for key in dic:
    p1 = 0.0
    p2 = 0.0
    dd = dic[key]
    p1 = float(dd[0]/dd[2])
    p2 = float(dd[1] / dd[2])
    print p1, p2
    if p1 == 0 or p2 ==0:
        pitemp = 0
    else:
        pitemp = (-1.0) *(p1 * math.log(p1, 2)) - p2 *math.log(p2, 2)
    pi += dd[2] / N * pitemp
print "%.2f" % (Entropy - pi)






#for i in range(0,N):
#    print (data[i])


