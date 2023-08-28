import random

# 创建角色和数字
characters = ["温", "顺", "乱"]
numbers = ["1", "2", "3"]

# 随机搭配角色和数字
random.shuffle(characters)

# 创建角色和数字的映射
character_to_number = {num: char for num, char in zip(numbers, characters)}

# 创建每个角色的回答
answers = {}
for num in numbers:
    other_numbers = [n for n in numbers if n != num]
    answer = random.choice(other_numbers)
    answers[num] = character_to_number[answer]

# 输出每个角色的回答
for num, answer in answers.items():
    print(f"{num}说：{answer}")

guess = int(input("请输入你猜测是乱的角色的序号： "))
# 获取玩家猜测的角色对应的字符
guessed_character = character_to_number.get(str(guess))

# 判断玩家猜测是否正确
if guessed_character == "乱":
    print("恭喜！你猜对了。")
else:
    print("很抱歉，你猜错了。")

