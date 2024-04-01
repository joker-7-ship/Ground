# import datetime
#
# if __name__ == '_main_':
#     # 输出今日日期，格式为 dd/mm/yyyy。更多选项可以查看 strftime() 方法
#     print(datetime.date.today().strftime('%d/%m/%Y'))
#
#     # 创建日期对象
#     miya1zakiBirthDate = datetime.date(1941, 1, 5)
#
#     print(miya1zakiBirthDate.strftime('%d/%m/%Y'))
#
#     # 日期算术运算
#     miya1zakiBirthNextDay = miya1zakiBirthDate + datetime.timedelta(days=1)
#
#     print(miya1zakiBirthNextDay.strftime('%d/%m/%Y'))
#
#     # 日期替换
#     miya1zakiFirstBirthday = miya1zakiBirthDate.replace(year=miya1zakiBirthDate.year + 1)
#
#     print(miya1zakiFirstBirthday.strftime('%d/%m/%Y'))
from sys import stdout

# import string
#
# s = input('请输入一个字符串:\n')
# letters = 0
# space = 0
# digit = 0
# others = 0
# for c in s:
#     if c.isalpha():
#         letters += 1
#     elif c.isspace():
#         space += 1
#     elif c.isdigit():
#         digit += 1
#     else:
#         others += 1
# print('char = %d,space = %d,digit = %d,others = %d' % (letters, space, digit, others))
#
# s = input('请输入一个字符串\n')
# for c in s:
#     if c.isalpha():
#         letters += 1
#     elif c.isspace():
#         space += 1
#     elif c.isdigit():
#         digit += 1
#     else:
#         others += 1
#
# print('char = %d,space = %d,digit = %d,others = %d' % (letters, space, digit, others))


# from functools import reduce
# Tn = 0
# Sn = []
# n = int(input('n = '))
# a = int(input('a = '))
# for count in range(n):
#     Tn = Tn + a
#     a = a*10
#     Sn.append(Tn)
#     print(Tn)
#     print(Sn)
# Sn = reduce(lambda x, y: x+y, Sn)
# print("计算和为:", Sn)

# from sys import stdout
#
# for j in range(2, 1001):
#     k = []
#     n = -1
#     s = j
#     for i in range(1, j):
#         if j % i == 0:
#             n += 1
#             s -= i
#             k.append(i)
#
#     if s == 0:
#         print(j)
#         for i in range(n):
#             stdout.write(str(k[i]))
#             stdout.write(' ')
#         print(k[n])
# tour = []
# height = []
# hei = 100
# tim = 10
# for i in range(1,tim + 1):
#     if i == 1:
#         tour.append(hei)
#     else:
#         tour.append(2*hei)
#     hei /= 2
#     height.append(hei)
# print('总高度：tour = {0}'.format(sum(tour)))
# print(tour)
# print('第10次反弹高度：height = {0}'.format(height[-1]))
# print(height)

#
# x1 = 1
# for n in range(1, 10):
#     x2 = 2 * (x1 + 1)
#     x1 = x2
#     print(x2)

# for i in range(ord('x'), ord('z') + 1):
#     for j in range(ord('x'), ord('z') + 1):
#         for k in range(ord('x'), ord('z') + 1):
#             if (i != k) and (j != k) and (i != j):
#                 if (i != ord('x')) and (k != ord('x')) and (k != ord('z')):
#                     print('order is a -- %s\t b -- %s\tc--%s' % (chr(i), chr(j), chr(k)))
# 穷举减去不符合条件的情况
for i in range(4):
    for j in range(2 - i + 1):
        stdout.write(' ')
    for k in range(2 * i + 1):
        stdout.write('*')
    print('')

# for i in range(3):
#     for j in range(i + 1):
#         stdout.write(' ')
#     for k in range(4 - 2 * i + 1):
#         stdout.write('*')
#     print('')