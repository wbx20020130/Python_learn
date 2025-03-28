import random

# 生成1到100之间的随机整数
x = random.randint(1, 100)

print("欢迎来到猜数字游戏！")
print("我已经选择了一个1到100之间的数字。")
print("你能猜到它是什么吗？")
print("你只有10次机会！")

attempts = 0

while attempts < 10:
    try:
        guess = int(input(f"请输入你的猜测（第{attempts + 1}次）："))
    except ValueError:
        print("无效输入，请输入一个1到100之间的整数。")
        continue

    if guess < 1 or guess > 100:
        print("请输入1到100之间的整数。")
        continue

    attempts += 1

    if guess < x:
        print("太小了！")
    elif guess > x:
        print("太大了！")
    else:
        print(f"恭喜你！你猜对了数字{x}！你一共猜了{attempts}次。")
        break
else:
    print(f"很遗憾，你已经用完了10次机会。正确的数字是{x}。")
