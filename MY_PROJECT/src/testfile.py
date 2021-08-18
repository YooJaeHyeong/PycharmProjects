# count = 1
# s = 0
# # while count <= 10:
# for i in range(1, 11):
#     s = s + count
#     count = count + 1
# print("합계는", s)

# dan = int(input("원하는 단:"))
# i = 1
#
# while i <= 9:
#     print("%s * %s = %s" %(dan,i,dan*i))
#     i = i + 1
#
# print("구구단 출력")
# for i in range(2, 10):
#     print("------"+str(i)+"단------")
#     for j in range(1, 10):
#         print(i,"*",j,"=",i*j)
#
# dan2 = 2
#
# while dan2 <= 9:
#     i = 1
#     print(dan2,"단")
#     while i <= 9:
#         print(dan2, "*",i,"=", dan2*i)
#         i += 1
#         dan2 += 1

# import turtle
# t = turtle.Turtle()
# t.shape("turtle")
# i = 0
# # while i <= 5:
# #     t.forward(50)
# #     t.right(144)
# #     i = i + 1
#
# for i in range(1, 6):
#     t.forward(50)
#     t.right(144)
#     i = i +1

# import turtle
#
# t = turtle.Turtle()
#
# t.speed(0)
# t.width(3)
# length = 10
#
# while length < 500:
#     t.forward(length)
#     t.right(89)
#     length += 5

# total = 0
# answer = 'yes'
# while answer == 'yes':
#     number = int(input("숫자를 입력하세요: "))
#     total = total + number
#     answer = input("계속?(yes/no) ")
#
# print("합계는 : ", total)

# import random
#
# tries = guess = 0
# answer = random.randint(1, 100)
# print("1부터 100사이의 숫자를 맞추시오")
#
# while guess != answer:
#     guess = int(input("숫자를 입력하세요: "))
#     tries = tries + 1
#     if guess < answer:
#         print("낮음!")
#     elif guess > answer:
#         print("높음!")
#
# print("축하합니다. 총 시도횟수=",tries)

# import random
# while True:
#     x = random.randint(1, 100)
#     y = random.randint(1, 100)
#     print(x,"+",y,"=",end = " ")
#     answer = int(input())
#     if answer == x+y:
#         print("잘했어요")
#     else:
#         print("정답은",x+y,"입니다. 다음번에 잘할 수 있죠?")

# breads = ["호밀빵","위트","화이트"]
# meats = ["미트볼", "소시지","닭가슴살"]
# vegis = ["양상추","토마토","오이"]
# sauces = ["마요네즈","허니 머스타트","칠리"]
#
# print("달수네 샌드위치 가게의 가능한 조합")
# for b in breads:
#     for m in meats:
#         for v in vegis:
#             for s in sauces:
#                 print(b+"+"+m+"+"+v+"+"+s)
#

# word = input("단어를 입력하세요: ")
# for i in word:
#     if i == 'a' or i == 'e' or i =='i' or i =='o' or i == 'u':
#         break
#     else:
#         print(i, end='')

# n = 100
# sum = 0
# print("1부터 100까지의 홀수는: ")
# for i in range(1, n+1):
#     if i%2 != 0:
#         sum += i
#         print(i, end = " ")
# print("\n1부터 100까지의 홀수의 합은: ",sum)

# n = 1
# print("1부터 100까지의 홀수는: ")
# while n <= 100:
#     print(n, end =" ")
#     n += 2

# 짝수
# n = 100
# print("1부터 100까지의 짝수는: ")
# for i in range(1, n+1):
#     if i%2 == 0:
#         print(i, end = " ")

# n = 100
# print("1부터 100까지의 짝수는: ")
# while n <= 100:
#     if n % 2 == 0:
#         print(n, end = " ")
#         break
#
# start = int(input("시작 정수를 입력하세요: "))
# end = int(input("끝 정수를 입력하세요:"))
#
# sum = 0
#
# for i in range(start, end+1):
#     sum += i
# print(start,"에서",end,"까지 정수의 합: ",sum)

# end = int(input("숫자를 입력하세요:"))
# for j in range(end+1):
#     for i in range(end-j+1):
#         print(" ",end = " ")
#     for i in range(1, j+1):
#         print("*",end = " ")
#     print()
#

# print("<< 369게임 >>")
# num = int(input("1부터 어디까지 진행할까요?"))
#
# for i in range(1, num+1):
#     if i % 10 == 3 or i % 10 == 6 or i % 10 == 9:
#         print("짝",end =" ")
#     elif i % 10 == 0:
#         print("따봉", end = "")
#     else:
#         print(i, end = " ")
#
# for i in range(5):
#     print('*' * (5-i))

# for i in range(5):
#     print(str(5-i) * (5-i))

for i in range(5):
    print(" " * (5-i), "*" * (i+1))