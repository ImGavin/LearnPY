# coding=utf-8
# 题目31：请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母

def guess_xingqi():
    F = raw_input("Please input the first str:")
    F = F.upper()
    xingqi = ['星期一','星期二','星期三','星期四','星期五','星期六','星期日']
    rs = ''
    if F == 'M':
        rs = xingqi[0]
    elif F == 'T':
        S = raw_input("Please input the second str:")
        S = S.upper()
        if S == 'U':
            rs = xingqi[1]
        elif S == 'H':
            rs = xingqi[3]
        else:
            rs = '输入结果，查不到是星期几'
    elif F == 'W':
        rs = xingqi[2]
    elif F == 'F':
        rs = xingqi[4]
    elif F == 'S':
        S = raw_input("Please input the second str:")
        S = S.upper()
        if S == 'A':
            rs = xingqi[5]
        elif S == 'U':
            rs = xingqi[6]
        else:
            rs = '输入结果，查不到是星期几'
    else:
        rs = '输入结果，查不到是星期几'
    return rs

# print guess_xingqi()

# 题目32：按相反的顺序输出列表的值。
def get_revert_list(a_list):
    a_list.reverse()
    return a_list
# l = [1,2,3]
# print get_revert_list(l)

# 题目33：按逗号分隔列表
def get_split_list(a_list):
    return '-'.join(a_list)

# list1 = ['C','Y','L']
# print get_split_list(list1)

# 题目34：练习函数调用
def hello_python():
    print "Hello Python!"

def three_hellos():
    for i in range(3):
        hello_python()
# if __name__ == '__main__':
#     three_hellos()

# 题目35：文本颜色设置
def set_text_colorfull(text):
    """
        查阅：https://www.cnblogs.com/daofaziran/p/9015284.html
        格式：开头部分：\033[显示方式;前景色;背景色m + 结尾部分：\033[0m
    """
    style = {
        0: '终端默认设置',
        1: '高亮显示',
        4: '使用下划线',
        5: '闪烁',
        7: '反白显示'
    }

    font = {
        30: '黑色',
        31: '红色',
        32: '绿色',
        33: '黄色'
    }

    bg_color = {
        40: '黑色',
        41: '红色',
        42: '绿色'
    }

    for s in style:
        for f in font:
            for bg in bg_color:
                # 过滤掉前景色与背景色一致的情况
                if font[f] != bg_color[bg]:
                    print '\033[{};{};{}m{} {}\033[0m'.format(s,f,bg,s,text)

# a_text = '白日依山尽，黄河入海流'
# set_text_colorfull(a_text)

# 题目36：求100之内的素数（质数）
def get_zhishu(fanwei):
    zhishu = []
    for n in range(2,fanwei+1):
        flag = 1
        for i in range(2,n/2+1):
            if n % i == 0:
                flag = 0
                break
        if flag == 1:
            zhishu.append(n)
    return zhishu

# print get_zhishu(100)

# 题目37：对10个数进行排序
def get_sort(a_list):
    # rs = []
    # a_list[0] = a_list[0]
    for i in range(0,len(a_list)):
        for j in range(0,len(a_list)-1-i):
            if a_list[j] < a_list[j+1]:
                a_list[j],a_list[j+1] = a_list[j+1],a_list[j]
            print a_list[j],a_list[j+1]
    return a_list

# print get_sort([22,123,21,52,13,2,35,68,1])

# 题目38：求一个3*3矩阵主对角线元素之和
def get_zhuduijiao_sum(juzhen):
    sum = 0.0
    for i in range(len(juzhen[0])):
        sum += juzhen[i][i]
    return sum

def get_a_juzhen(n):
    juzhen = []
    for i in xrange(n):
        juzhen.append([])
        for j in xrange(n):
            juzhen[i].append(float(raw_input("input num:\n")))
    return juzhen

# print get_a_juzhen(3)
# print get_zhuduijiao_sum(get_a_juzhen(3))

def get_sort_again_list(a_list,num):
    import copy
    index = 0
    rs = copy.deepcopy(a_list)
    for i in range(len(a_list)):
        if a_list[i] <= num and num <= a_list[i+1]:
            index = i+1
            break
    rs.append(num)
    for i in range(index+1,len(rs)):
        rs[i] = a_list[i-1]
    rs[index] = num
    # print a_list,rs
    return rs

# alist = [11,23,27,36,58,73]
# num = 22
# print get_sort_again_list(alist,num)

# 题目40：将一个数组逆序输出
def get_revert_array(arr):
    arr.reverse()
    return arr

# print get_revert_array([1,2,6,3,9])

