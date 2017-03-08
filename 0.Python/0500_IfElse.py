# demo1
a = 10

if a > 5:
    print("a > 5")
else:
    print("a <= 5")


# demo2
score = 77

if score >= 90 and score <= 100:
    print('本次考试，等级为A')
elif score >= 80 and score < 90:
    print('本次考试，等级为B')
elif score >= 70 and score < 80:
    print('本次考试，等级为C')
elif score >= 60 and score < 70:
    print('本次考试，等级为D')
elif score >= 0 and score < 60:
    print('本次考试，等级为E')


# demo3
import random

player = input('请输入：剪刀(0)  石头(1)  布(2):')

player = int(player)

computer = random.randint(0, 2)

if ((player == 0) and (computer == 2)) or ((player == 1) and (computer == 0)) or ((player == 2) and (computer == 1)):
    print('获胜，哈哈，你太厉害了')
elif player == computer:
    print('平局，要不再来一局')
else:
    print('输了，不要走，洗洗手接着来，决战到天亮')
