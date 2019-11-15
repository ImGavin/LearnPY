# coding=utf-8
# 题目1：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
# 程序分析：可填在百位、十位、个位的数字都是1、2、3、4。组成所有的排列后再去 掉不满足条件的排列。
def get_a_hundred_num(*args):
    if len(args) >= 3:
        tmp = []
        for b in args:
            for s in args:
                for g in args:
                    if b == 0 :
                        continue
                    rs = b*100+s*10+g
                    if rs in tmp:
                        pass
                    else:
                        tmp.append(rs)
                        print rs
                    # if (b!=s) and (s!=g) and (g!=b):
                    # print b*100+s*10+g
        print len(tmp)
    else:
        return 'Please input 3 numbers!'
# get_a_hundred_num(1,2,3,4)

# 题目2：企业发放的奖金根据利润提成。
# 利润(I)低于或等于10万元时，奖金可提10%；
# 利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
# 20万到40万之间时，高于20万元的部分，可提成5%；
# 40万到60万之间时高于40万元的部分，可提成3%；
# 60万到100万之间时，高于60万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成
# 从键盘输入当月利润I，求应发放奖金总数？

# I = int(raw_input('净利润:'))
def get_bonus_by_net_profit(I):
    boundary = [1000000,600000,400000,200000,100000,0]
    rate = [0.01,0.015,0.03,0.05,0.075,0.10]
    JJ = 0
    for idx in range(0,len(boundary)):
        if I > boundary[idx]:
            JJ = JJ + (I-boundary[idx])*rate[idx]
            I = boundary[idx]
    return JJ
# print get_bonus_by_net_profit(int(raw_input('净利润(元):')))

# 题目3：一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
# 程序分析： 
# 假设该数为 x。
# 1、则：x + 100 = n2, x + 100 + 168 = m2
# 2、计算等式：m2 - n2 = (m + n)(m - n) = 168
# 3、设置： m + n = i，m - n = j，i * j =168，i 和 j 至少一个是偶数
# 4、可得： m = (i + j) / 2， n = (i - j) / 2，i 和 j 要么都是偶数，要么都是奇数。
# 5、从 3 和 4 推导可知道，i 与 j 均是大于等于 2 的偶数。
# 6、由于 i * j = 168， j>=2，则 1 < i < 168 / 2 + 1。
# 7、接下来将 i 的所有数字循环计算即可。

# 暴力算法，无法确认x范围，可能无法算出所有符合条件的值，且性能极差
# for x in range(0,1000):
#     for m in range(0,100):
#         for n in range(0,100):
#             if x + 100 == m * m:
#                 if x + 100 + 168 == n * n:
#                     print x,m,n

# 这个解法我服
# for i in range(2,85,2):
#     if 168 % i == 0:
#         j = 168 / i
#         if  i > j and (i + j) % 2 == 0 and (i - j) % 2 == 0 :
#             m = (i + j) / 2
#             n = (i - j) / 2
#             x = n * n - 100
#             print(x)



# 题目4：输入某年某月某日，判断这一天是这一年的第几天？

def get_day(year,month,day):
    try:
        year = int(year)
        month = int(month)
        day = int(day)
    except ValueError as e:
        return 'Tips: year,month or day is invalid!'
    if not (0<day and day<31):
        return 'day is invalid!'
    M_D31 = [1,3,5,7,8,10,12]
    M_D30 = [4,6,9,11]
    leap = 0
    rs = 0
    if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
        leap = 1
    for x in range(1,month):
        if x in M_D31:
            rs = rs + 31
        elif x in M_D30:
            rs = rs + 30
        elif x == 2:
            if leap == 1:
                rs = rs + 29
            else:
                rs = rs + 28
        else:
            return 'month is invalid!'
    return rs + day

# print get_day(year = raw_input('year:'), month = raw_input('month:'), day = raw_input('day:'))

# 题目5：输入三个整数x,y,z，请把这三个数由小到大输出。
def get_sort_results(*args):
    nums = list(args)
    for i in range(0,len(nums)-1):
        for idx in range(0,len(nums)-1-i):
            if nums[idx+1] < nums[idx]:
                tmp = nums[idx]
                nums[idx] = nums[idx+1]
                nums[idx+1] = tmp
    for x in nums:
        print x,
# get_sort_results(8,2,5,16,4,13)

# 题目6：斐波那契数列。
# 程序分析：斐波那契数列（Fibonacci sequence），又称黄金分割数列，指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……
def get_fibonacci_sequence(length):
    rs = []
    if length < 2:
        return 'Need length >= 2'
    elif length == 1:
        rs.append(1)
        return rs
    elif length == 2:
        return rs + [1,1]
    else:
        rs = rs + [1,1]
    for idx in range(2,length):
        rs.append(rs[idx-2] + rs[idx-1])
    return rs
# print get_fibonacci_sequence(10)

# 特神奇的代码
def fib(n):
    a,b = 1,1
    for i in range(n-1):
        a,b = b,a+b
    return a
# 输出了第10个斐波那契数列
# print fib(2)

# 题目7：将一个列表的数据复制到另一个列表中
def copy_list(l1):
    return l1[:]
alist = [1,2,3,4,5]
# print copy_list(alist)

# 题目8：输出 9*9 乘法口诀表
def get_multiplication_table(base_num):
    for row in range(1,base_num+1):
        print ''
        for column in range(1,row+1):
            # print '{}x{}={}'.format(column,row,column*row)+' ',
            print "%dx%d=%d" % (column,row,column*row),
# get_multiplication_table(9)

# 题目9、10：暂停一秒输出，并格式化当前时间
# import time
# def get_sleep_time(n):
#     time.sleep(n)
# def get_current_time():
#     return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
# for x in range(10):
#     get_sleep_time(1)
#     print get_current_time()
