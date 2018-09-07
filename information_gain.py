# -*-coding=utf-8-*-
'''
@Author: tq
������ʵ�ּ�����Ϣ���棬ID3-��Ϣ���棬C4.5��Ϣ������
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
label = {} # ��������Ϊ��������ֵ�Ǹ������Ŀ

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

# ����������
# ͳ�Ƹ������Եļ��㹫ʽ
dic = {}
for sample in data:
    if sample[0] not in dic:
        dic[sample[0]] = [0, 0, 0] # ����ͳ������i�ĵ�����0�� 1����Ŀ���Լ��������ܹ�����Ŀ
    if sample[1] == 0:
        dic[sample[0]][0] += 1
    else:
        dic[sample[0]][1] += 1
    dic[sample[0]][2] += 1
#��ʼ����
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


