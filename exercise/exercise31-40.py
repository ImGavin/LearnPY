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

# 题目33：练习函数调用
def hello_python():
    print "Hello Python!"

def three_hellos():
    for i in range(3):
        hello_python()
# if __name__ == '__main__':
#     three_hellos()

# 题目34：文本颜色设置
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
