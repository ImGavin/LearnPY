# coding=utf-8
# 题目21：猴子吃桃问题：
# 猴子第一天摘下若干个桃子，当即吃了一半，还不瘾，又多吃了一个第二天早上又将剩下的桃子吃掉一半，又多吃了一个。
# 以后每天早上都吃了前一天剩下的一半零一个。到第10天早上想再吃时，见只剩下一个桃子了。求第一天共摘了多少。
def get_peach_num(days,left_num):
    a_list = []
    an = left_num
    a_list.append(an)
    for day in range(2,days+1):
        an = (an+1)*2
        a_list.append(an)
    return '第{}天共{}个桃子：'.format(days-len(a_list)+1,a_list[len(a_list)-1])

# print get_peach_num(10,1)

# 题目：两个乒乓球队进行比赛，各出三人。
# 甲队为a,b,c三人，乙队为x,y,z三人。已抽签决定比赛名单
# 有人向队员打听比赛的名单。a说他不和x比，c说他不和x,z比，请编程序找出三对赛手的名单
def rm_factor(A_list,c_list,only):
    for i in A_list:
        count = 0
        for m in c_list:
            if i in m:
                count += 1
        if count == 1:
            to_rm = ''
            for m in c_list:
                if i in m:
                    only.append(m)
                    c_list.remove(m)
                    to_rm = m[1]
            for m in c_list:
                if to_rm == m[1]:
                    c_list.remove(m)
        # print c_list
    return (c_list,only)

def get_competition_list(A_list,B_list,not_zh):
    c_list = []
    only = []
    for i in A_list:
        for j in B_list:
            if not(i+j in not_zh):
                c_list.append(i+j)
    print c_list

    while len(c_list) >= 1:
        c_list = rm_factor(A_list,c_list,only)[0]
        only = rm_factor(A_list,c_list,only)[1]

    return only

# A_list = ['a','b','c']
# B_list = ['x','y','z']
# not_zh = ['ax','cx','cz']
# print get_competition_list(A_list,B_list,not_zh)

# 题目23：打印出如下图案（菱形）:
#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *
def print_lingxing(bian_len):
    for x in range(1,bian_len+1):
        space_len = bian_len - x
        print ' ' * space_len + '*' * (x*2-1)
    for x in range(bian_len-1,0,-1):
        space_len = bian_len - x
        print ' ' * space_len + '*' * (x*2-1)

# print_lingxing(8)

# 题目24：有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和
def get_squence_sum(n):
    fib = []
    fz = 2
    fm = 1
    a,b = 1,1
    sum = 2
    fib.append(b)
    for x in range(n):
        a,b = b,a+b
        fib.append(b)
    # print fib
    for i in range(1,n):
        fz,fm = fm+fz,fz
        sum += fz / float(fm)
    print sum

# get_squence_sum(20)

# 题目25：求1+2!+3!+...+20!的和
def get_sum_of_jiecheng(n):
    sum = 0
    for i in range(1,n+1):
        an = 1
        for j in range(i,1,-1):
            an = an * j
        sum = sum + an
    return sum
# print get_sum_of_jiecheng(20)

# 题目26：利用递归方法求5!
def get_jiecheng(n):
    if n > 0:
        return n * get_jiecheng(n-1)
    elif n == 0:
        return 1
    else:
        return 'Please give a zhengzhegnshu !'
# print get_jiecheng(3)

# 题目27：利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来
def get_revert_str(a_str):
    r_str = ''
    if len(a_str)>1:
        r_str = a_str[-1] + get_revert_str(a_str[0:-1])
    else:
        r_str = a_str[-1]
    return r_str

# print get_revert_str(raw_input('Input a string:'))
# print 'abc'[0:-1]

# 题目28：有5个人坐在一起，
# 问第5个人多少岁，他说比第4个人大2岁。
# 问第4个人，他说比第3个人大2岁。
# 问第3个人，又说比第2人大2岁。
# 问第2个人，说比第一个人大2岁。
# 最后问第一个人，他说是10岁。
# 请问第五个人多大？

def get_the_age(person):
    age = 0
    if person > 1:
        age = 2 + get_the_age(person-1)
    else:
        age = 10
    return age

# print get_the_age(3)

# 题目29：给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字

def get_num_len_and_revert(num):
    num = str(num)
    l = len(num)
    rv = ''
    if len(num)>1:
        rv = num[-1] + get_num_len_and_revert(num[0:-1])
    else:
        rv = num[-1]
    return rv
# ipt = '12345'
# print '{}位数：'.format(len(ipt)) + ' '.join(get_num_len_and_revert(ipt))

# 题目30：一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同
def is_huiwen_num(num):
    num = str(num)
    ct = len(num) / 2
    flag = True
    for i in xrange(ct):
        if num[i] != num[-(i+1)]:
            flag = False
    return flag
# num = raw_input("Input a number:")
# print '{}是不是回文数：{}'.format(num,is_huiwen_num(num))
