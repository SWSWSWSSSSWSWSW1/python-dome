# 导入所需模块
import sys
import time
from getpass import getuser

# 获取用户的用户名
name = getuser()
name_check = input("你的名字是 " + name + " 吗？ → ")

# 检查用户输入的名字是否正确
if name_check.lower().startswith("y"):
    print("好的。")
    time.sleep(1)

# 如果用户输入的名字不正确，询问正确的名字
if name_check.lower().startswith("n"):
    name = input("那么你的名字是什么？ → ")

# 将用户输入的名字存储在列表中
userList = name

# Python 与用户的对话
print("你好", name + "，我是 Python。")
time.sleep(0.8)
print("你的名字的第一个字母是", userList[0] + "。")
time.sleep(0.8)
print("很高兴见到你。:)")
time.sleep(0.8)
response = input("你认为见到我很高兴吗？ → ")

# 其他对话
if response.lower().startswith("y"):
    print("很好 :)")  # 如果用户愿意见到 Python，打印“很好 :)”
    sys.exit()

elif response.lower().startswith("n"):
    response2 = input("是因为我是机器人吗？ → ")

else:
    print("你可能输入错误。请重新开始并重试。")
    sys.exit()

if response2.lower().startswith("y"):
    print("哎呀 :(")  # 如果用户认为见到 Python 不好是因为它是机器人，打印“哎呀 :(”

elif response2.lower().startswith("n"):
    response3 = input("那是为什么呢？ → ")
    time.sleep(1)
    print("噢。")  # 如果用户回答不是因为它是机器人，打印“噢。”

else:
    print("你可能输入错误。请重新开始并重试。")
    sys.exit()
