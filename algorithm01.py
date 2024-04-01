import time

# select * from student where id
# in(select stu_id from score where c_name = '计算机' and grade > 95)
#
# create table student(
#     s_id int(5)
#     S_name varchar(20)
#     s_age int(3)
#     s_sex char(2)
#     s_address varchar(11)
# )
# alter table student add s_ed varchar(10)
# alter table student drop column s_address
#
# insert into student values()
# update student set s_ed = '大专' where s_phone like'11%'
# delete from student where s_sex = '男' and s_name like 'C%'
#
# select * from emp as e left join work_log as b where e.emp_no = b.emp_no and e.name='james' and month(w.work_date)=1
#
# select e.emp_no,e.ename,sum(w.work_hour) as 工时
# from emp as e join work_log as w
# where e.emp_no=w.emp_no
# and month(w.work_date)=1
#
#
# group by e.emp_no
# having sum(w.work_hour)<160；
# order by
# group by
# limit 0,10
# a left join b on a.score = b.score where name = 'guowang' group by id having count(score)> 100  order by count(score) desc limit
#
# def bubbleSort(int[] arr)
#     int temp = 0;
#     for(int i = arr.length-1;i>0;i--){
#         for (int j=0;j < i;j++){
#                 if(arr[j]<arr[j+1]){
#                     temp = arr[j];
#                     arr[j]=arr[j+1];
#                     arr[j+1]= temp
#             }
#         }
#     }
# def selectionSort(int[] arr)
#     int temp,min=0;
#     for(i=0;i<arr.length-1;i++){
#         min = i;
#         if(arr[min]>arr[j]){
#             min = j;
#     }
#     if(min != i){
#     temp = arr[i]
#     arr[i] = arr[min]
#     arr[min]= temp
#     }
#     }

# N = int(input("N:"))
# fib = [0 for x in range(N+1)]
# fib[0] = 0
# fib[1] = 1
# for i in range(2,N+1)
#     fib[i] = fib[i-1] + fib[i-2]
# print fib[N]


# str = input("请输入：")
# print("你输入的内容是：", str)
#
# for i in range(1, 5):
#     for j in range(1, 5):
#         for k in range(1, 5):
#             if (i != k) and (i != j) and (j != k):
#                 print(i * 100 + j * 10 + k)
# 列表
# i = int(input('净利润:'))
# arr = [1000000, 600000, 400000, 200000, 100000, 0]
# rat = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
# r = 0
# for idx in range(0, 6):
#     if i > arr[idx]:
#         r += (i - arr[idx]) * rat[idx]
#         print((i - arr[idx]) * rat[idx])
#         i = arr[idx]
# print(r)

# 判断某年某月某日是该年的多少天
# year = int(input('year:\n'))
# month = int(input('month:\n'))
# day = int(input('day:\n'))
# days = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
# sum1 = 0
# if 0 < month <= 12:
#     sum1 = days[month - 1]
# else:
#     print('data error')
# sum1 += day
# leap = 0
# if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
#     leap = 1
# if (leap == 1) and (month > 2):
#     sum1 += 1
# print('it is the %dth day.' % sum1)

# 三个数从小到大输出
# l = []
# for i in range(3):
#     x = int(input('integer:\n'))
#     l.append(x)
# l.sort()
# print(l)

# 斐波那契数列
# def fib(n):
#     if n == 1 or n == 2:
#         return 1
#     return fib(n - 1) + fib(n - 2)
#
#
# print(fib(10))


# def fib(n):
#     if n == 0:
#         return [0]
#     if n == 1:
#         return [0, 1]
#     if n == 2:
#         return [0, 1, 1]
#     fibs = [0, 1, 1]
#     for i in range(2, n):
#         print(i)
#         print(fibs[-1] + fibs[-2])
#         fibs.append(fibs[-1] + fibs[-2])
#
#     return fibs
#
#
# print(fib(10))

# # 将列表的数据复制到另外一个列表中
# a = [1, 2, 3]
# b = a[:]
# print(b)

# 九九乘法表格

# for i in range(1, 10):
#     print()
#     for j in range(1, i+1):
#         print("%d*%d=%d " % (i, j, i * j), end="")

# 输出字典
# myD = {1: 'a', 2: 'b'}
# for key, value in dict.items(myD):
#     print(key, value)
#     time.sleep(1)

# 输出列表

# l = [1, 2, 3, 4]
# for i in range(len(l)):
#     print(l[i])
#     time.sleep(1)
# 暂停一秒输出，并格式化当前时间

# print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
# time.sleep(1)
# print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
# 判断101-200之间的素数
# from math import sqrt
# from sys import stdout
# h = 0
# leap = 1
# for m in range(101,201):
#     k = int(sqrt(m+1))
#     for i in range(2,k+1):
#         if m%1 ==0:
#             leap = 0
#             break
#
#     if leap == 1:

# # 水仙花数：
# for n in range(100, 1000):
#     i = n // 100
#     j = n // 10 % 10
#     k = n % 10
#     if n == i * i * i + j * j * j + k * k * k:
#         print(n)

# 分数等级
# score = int(input('输入分数：\n'))
# if score>=90:

# //题目29：给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字

#
# x = int(input("请输入一个数：\n"))
# a = x // 10000
# b = x % 10000 // 1000
# c = x % 1000 // 100
# d = x % 100 // 10
# e = x % 10
#
# if a != 0:
#     print("5位数：", e, d, c, b, a)
# elif b != 0:
#     print("4 位数：", e, d, c, b)
# elif c != 0:
#     print("3 位数：", e, d, c)
# elif d != 0:
#     print("2 位数：", e, d)
# else:
#     print("1 位数：", e)

# a = int(input("请输入一个数字:\n"))
# x = str(a)
# flag = True
#
# for i in range(len(x) // 2):
#     if x[i] != x[-i - 1]:
#         flag = False
#         break
#
# if flag == True:
#     print("%d 是一个回文数!" % a)
# else:
#     print("%d 不是一个回文数!" % a)


# letter = input("please input:")
# # while letter  != 'Y':
# if letter == 'S':
#     print('please input second letter:')
#     letter = input("please input:")
#     if letter == 'a':
#         print('Saturday')
#     elif letter == 'u':
#         print('Sunday')
#     else:
#         print('data error')
#
# elif letter == 'F':
#     print('Friday')
#
# elif letter == 'M':
#     print('Monday')
#
# elif letter == 'T':
#     print('please input second letter')
#     letter = input("please input:")
#
#     if letter == 'u':
#         print('Tuesday')
#     elif letter == 'h':
#         print('Thursday')
#     else:
#         print('data error')
#
# elif letter == 'W':
#     print('Wednesday')
# else:
#     print('data error')

# a = ['one', 'two', 'three']
# for i in a[::-1]:
#     print (i)


# def hello_runoob():
#     print('RUNOOB')
#
#
# def hello_runoobs():
#     for i in range(3):
#         hello_runoob()
#
#
# if __name__ == '__main__':
#     hello_runoobs()


# class bcolors:
#     HEADER = '\033[95m'
#     OKBLUE = '\033[94m'
#     OKGREEN = '\033[92m'
#     WARNING = '\033[93m'
#     FAIL = '\033[91m'
#     ENDC = '\033[0m'
#     BOLD = '\033[1m'
#     UNDERLINE = '\033[4m'
#
#
# print(bcolors.WARNING + "警告的颜色字体?" )


# lower = int(input("输入区间最小值："))
# upper = int(input("输入区间最小值："))
#
# for num in range(lower, upper + 1):
#     if num > 1:
#         for i in range(2, num):
#             if(num % i) == 0:
#                 break
#         else:
#             print(num)


# a = []
# sum = 0.0
# for i in range(3):
#     a.append([])
#     for j in range(3):
#         a[i].append(float(input("input num:\n")))
# for i in range(3):
#     sum += a[i][i]
# print(sum)

# a = []
# for i in range(3):
#     a.append(float(input("input num:\n")))
# for i in range(3):
#     print(a[i])

# a = [1, 4, 6, 9, 13, 16, 19, 28, 40, 100, 0]
# print('原始列表:')
# for i in range(len(a)):
#     print(a[i])
# number = int(input("\n插入一个数字:\n"))
# end = a[9]
# if number > end:
#     a[10] = number
# else:
#     for i in range(10):
#         if a[i] > number:
#             temp1 = a[i]
#             a[i] = number
#             for j in range(i + 1, 11):
#                 temp2 = a[j]
#                 a[j] = temp1
#                 temp1 = temp2
#             break
# print('排序后列表:')
# for i in range(11):
#     print(a[i])

# a = [9, 6, 5, 4, 1, 3]
# N = len(a)
# print(N)
# print(a)
# print(len(a) // 2)
# for i in range(len(a) // 2):
#     a[i], a[N - i - 1] = a[N - i - 1], a[i]
# print(a)

# X = [[12, 7, 3],
#      [4, 5, 6],
#      [7, 8, 9]]
#
# Y = [[5, 8, 1],
#      [6, 7, 3],
#      [4, 5, 9]]
#
# result = [[0, 0, 0],
#           [0, 0, 0],
#           [0, 0, 0]]
#
# # 迭代输出行
# for i in range(len(X)):
#     # 迭代输出列
#     for j in range(len(X[0])):
#         result[i][j] = X[i][j] + Y[i][j]
#
# for r in result:
#     print(r)
# !/usr/bin/python
# -*- coding: UTF-8 -*-
from Tkinter import *
if __name__ == '__main__':


    canvas = Canvas(width=800, height=600, bg='yellow')
    canvas.pack(expand=YES, fill=BOTH)
    k = 1
    j = 1
    for i in range(0, 26):
        canvas.create_oval(310 - k, 250 - k, 310 + k, 250 + k, width=1)
        k += j
        j += 0.3

    mainloop()