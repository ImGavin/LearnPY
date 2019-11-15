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
    return ','.join(a_list)

list1 = ['C','Y','L']
print get_split_list(list1)
