# coding=utf-8
# 题目41：模仿静态变量的用法。

def varfunc():
    var = 0
    print 'var = %d' % var
    var += 1
# if __name__ == '__main__':
#     for i in range(3):
#         varfunc()

# 类的属性
# 作为类的一个属性吧
class Static:
    StaticVar = 5
    def varfunc(self):
        self.StaticVar += 1
        print self.StaticVar

# print Static.StaticVar
# a = Static()
# for i in range(3):
#     a.varfunc()

# 题目42：学习使用auto定义变量的用法
# num = 2
def autofunc():
    num = 1
    print 'internal block num = %d' % num
    num += 1
# for i in range(3):
#     print 'The num = %d' % num
#     num += 1
#     autofunc()

# 题目43：模仿静态变量(static)另一案例
# class Num:
#     nNum = 1
#     def inc(self):
#         self.nNum += 1
#         print 'nNum = %d' % self.nNum
#
# if __name__ == '__main__':
#     nNum = 2
#     inst = Num()
#     for i in range(3):
#         nNum += 1
#         print 'The num = %d' % nNum
#         inst.inc()

# 题目44：两个 3 行 3 列的矩阵，实现其对应位置的数据相加，并返回一个新矩阵

X = [[12,7,3],
    [4,5,6],
    [7,8,9]]

Y = [[5,8,1],
    [6,7,3],
    [4,5,9]]

def get_juzhen_sum(X,Y):
    rs = []
    for i in range(3):
        rs.append([])
        for j in range(3):
            rs[i].append(X[i][j] + Y[i][j])
    return rs

# print get_juzhen_sum(X,Y)

# 题目45：统计 1 到 100 之和
def get_sum_by_range(min,max):
    sum = 0
    for x in range(min,max+1):
        sum += x
    return sum

# print get_sum_by_range(1,100)

