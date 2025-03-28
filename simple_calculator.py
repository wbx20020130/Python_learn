def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "不能除以零"
    return x / y

while True:
    print("选项:")
    print("输入'add'进行加法")
    print("输入'subtract'进行减法")
    print("输入'multiply'进行乘法")
    print("输入'divide'进行除法")
    print("输入'exit'结束程序")
    user_input = input(": ")
    if user_input == "exit":
        break
    if user_input in ("add", "subtract", "multiply", "divide"):
        num1 = float(input("输入第一个数: "))
        num2 = float(input("输入第二个数: "))
        if user_input == "add":
            print("结果: ", add(num1, num2))
        elif user_input == "subtract":
            print("结果: ", subtract(num1, num2))
        elif user_input == "multiply":
            print("结果: ", multiply(num1, num2))
        elif user_input == "divide":
            print("结果: ", divide(num1, num2))
    else:
        print("无效输入")
