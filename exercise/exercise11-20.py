# coding=utf-8
# 题目11：古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少（对）？
# 程序分析：从第一对兔子出生算第1个月，兔子的对数 规律为数列：1,1,2,3,5,8,13,21....  分析可知，这是一个斐波那契数列
def fib(m):
    a,b = 1,1
    for x in range(2,m):
        a,b = b,a+b
    return b
# print fib(5)

# 题目12：判断101-200之间有多少个素数，并输出所有素数。
# 程序分析：判断素数的方法：用一个数分别去除2到sqrt(这个数)，如果能被整除，则表明此数不是素数，反之是素数。
def get_sushu(min,max):
    import math
    sushu = []
    for x in range(min,max+1):
        flag = 1
        for i in range(2,int(math.floor(math.sqrt(x)))+1):
            if x%i == 0:
                flag = 0
                break
        if flag == 1:
            sushu.append(x)
    return sushu
# print get_sushu(101,200)

# 题目13：打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方
def get_sxh():
    import math
    sxh_list = []
    for x in range(100,1000):
        b = x / 100
        s = x / 10 % 10
        g = x % 10 % 10
        fabs_sum = math.pow(b,3) + math.pow(s,3) + math.pow(g,3)
        if x == fabs_sum:
            sxh_list.append(x)
    return sxh_list
# print get_sxh()

# 题目14：将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5
def get_prime_factor(m):
    import math
    if (not isinstance(m,int)) or m < 0 :
        return 'Please give a positive integer!'
    print '{} ='.format(m),
    all_factor = []
    prime_factor = []
    if m == 1:
        all_factor.append(1)
        prime_factor.append(1)
    else:
        for x in range(2, m/2+1):
            if m%x==0:
                all_factor.append(x)

        for y in all_factor:
            while (m/y in all_factor):
                prime_factor.append(y)
                m = m/y
                print '{} *'.format(y),
    print '{}'.format(m)
        # prime_factor.append(m)
    # return all_factor,prime_factor
# get_prime_factor(90)

# 题目15：利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示
def get_class(score):
    score_class = ''
    if score >= 90:
        score_class = 'A'
    elif score >= 60:
        score_class = 'B'
    else:
        score_class = 'C'
    return '{}分对应等级:{}'.format(score,score_class)
# print get_class(int(raw_input('Input score：')))

# 题目16：输出指定格式的日期
def get_format_time(the_time,format):
    import time
    if not type(the_time) in [int,long]:
        return 'Please input a vilad timestamp!'
    elif not (0 < the_time and the_time <= 32535244799):
        return 'The timestamp outof the range!'
    return time.strftime(format,time.localtime(the_time))
# print get_format_time(32535244799,'%Y-%m-%d')

# 题目17：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数
def get_char_nums(str):
    eg_char_list = []
    space_char_list = []
    alab_num_list = []
    other_char_list = []
    for x in str:
        if x.isdigit():
            alab_num_list.append(x)
        elif x.isalpha():
            eg_char_list.append(x)
        elif x.isspace():
            space_char_list.append(x)
        else:
            other_char_list.append(x)
    print 'char = %d, space = %d, digit = %d, other = %d' % (len(eg_char_list),len(space_char_list),len(alab_num_list),len(other_char_list))

# get_char_nums(raw_input('Type a string:'))

# 题目18：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制
def get_sum(digit,times):
    if not digit.isdigit():
        return 'Please give a digit!'
    if not (u"{}".format(times)).isnumeric():
        return 'Please give a number!'
    str = digit[0]
    times = int(times)
    s = 0
    for n in range(1,times+1):
        s += int(str*n)
    return s
# print get_sum(raw_input('Give a digit:'),raw_input('Give the times:'))

# 题目19：一个数如果恰好等于它的因子之和(本身除外)，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数
def get_wanshu_by_range(anum):
    wanshu_list = []
    for x in range(1,anum+1):
        yz_list = []
        yz_sum = 0
        for i in range(1,x/2+1):
            if x%i == 0:
                yz_list.append(i)
                yz_sum += i
        if yz_sum == x:
            wanshu_list.append(x)
    return wanshu_list
anum = 1000
# print get_wanshu_by_range(anum)

# 题目20：一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
def get_frem_fall(high,times):
    total_dis = 0
    times_high = high
    for x in range(1,times+1):
        if x == 1:
            total_dis += times_high
        else:
            total_dis += times_high * 2
        times_high = times_high / 2.0
    print '第%d次落地时，共经过%f米' % (times,total_dis)
    print '第%d次弹起的高度为%f米' % (times,times_high)
# get_frem_fall(100,10)

