
import random
import itertools


class GuessingGame:
    def __init__(self):
        self.characters = ["温", "顺", "乱"]
        self.numbers = ["1", "2", "3"]
        self.level = 1
        self.character_to_number = {}
        self.answers = {}

    # 生成新的一局
    def new_round(self):
        while True:
            shuffled = self.characters.copy()
            random.shuffle(shuffled)

            self.character_to_number = dict(
                zip(self.numbers, shuffled)
            )

            self.answers = {}

            for num in self.numbers:
                real = self.character_to_number[num]
                false_answers = [
                    char for char in self.characters
                    if char != real
                ]
                self.answers[num] = random.choice(false_answers)

            # 初级只生成无需追问就能确定"乱"的题目
            if self.level != 1 or self.is_provable(
                "乱", self.possible_assignments()
            ):
                break

    # 枚举所有符合已知线索的身份组合
    def possible_assignments(self, ask_num=None, second_answer=None):
        possibilities = []

        for arrangement in itertools.permutations(self.characters):
            candidate = dict(zip(self.numbers, arrangement))

            # 每个人的第一次回答都不能是真实身份
            if any(
                candidate[num] == self.answers[num]
                for num in self.numbers
            ):
                continue

            # 如果追问过，还要符合第二次的回答
            if ask_num is not None:
                if candidate[ask_num] == second_answer:
                    continue

            possibilities.append(candidate)

        return possibilities

    # 判断指定身份是否能通过线索唯一确定
    def is_provable(self, target, possibilities):
        possible_numbers = set()

        for candidate in possibilities:
            for num in self.numbers:
                if candidate[num] == target:
                    possible_numbers.add(num)

        return len(possible_numbers) == 1

    # 第二次必须说另一个假身份
    def ask_again(self, num):
        real = self.character_to_number[num]
        first = self.answers[num]

        return next(
            char for char in self.characters
            if char != real and char != first
        )

    # 检查输入
    def read_number(self, prompt, allow_skip=False):
        valid = self.numbers + (["0"] if allow_skip else [])

        while True:
            answer = input(prompt).strip()
            if answer in valid:
                return answer
            print("输入无效，请重新输入！")

    # 进行一局游戏
    def play_round(self):
        self.new_round()

        if self.level == 1:
            target = "乱"
        elif self.level == 2:
            target = random.choice(self.characters)
        else:
            target = None

        print(f"\n===== Level {self.level} =====")

        if self.level == 3:
            print("目标：还原所有人的真实身份！")
        else:
            print(f"目标：找出谁是「{target}」！")

        print("三个人都不会说出自己的真实身份。")

        for num, answer in self.answers.items():
            print(f"{num}号说：{answer}")

        ask_num = None
        second_answer = None

        # 中级和高级：选择直接作答或追问
        if self.level >= 2:
            print("\n请选择下一步操作：")

            if self.level == 2:
                print(f"本局目标：找出「{target}」")
            else:
                print("本局目标：还原所有人的真实身份")

            print("0 - 我已经知道答案，直接作答")
            print("1 - 追问1号")
            print("2 - 追问2号")
            print("3 - 追问3号")

            ask_num = self.read_number(
                "请选择操作（0、1、2、3）：",
                allow_skip=True
            )

            if ask_num == "0":
                ask_num = None
                print("你选择直接作答！")
            else:
                second_answer = self.ask_again(ask_num)
                print(f"你选择追问{ask_num}号。")
                print(f"{ask_num}号第二次说：{second_answer}")

        # 根据两轮信息计算所有可能的答案
        possibilities = self.possible_assignments(
            ask_num, second_answer
        )

        # 高级：必须还原所有身份
        if self.level == 3:
            while True:
                guess = input(
                    "依次输入1、2、3号的身份，例如：温顺乱："
                ).strip()

                if len(guess) == 3 and set(guess) == set(self.characters):
                    break

                print("请输入温、顺、乱三个字，每个只能用一次！")

            correct = all(
                guess[i] == self.character_to_number[num]
                for i, num in enumerate(self.numbers)
            )

            provable = len(possibilities) == 1

        # 初级和中级：找到指定身份
        else:
            guess = self.read_number(
                f"你认为谁是「{target}」？请输入1、2或3："
            )

            correct = self.character_to_number[guess] == target
            provable = self.is_provable(target, possibilities)

        # 公布结果
        print("\n===== 推理结果 =====")

        if not correct:
            print("猜错了，这一关需要再挑战。")
        elif not provable:
            print("猜对了！但现有线索还不能确定唯一答案。")
            print("这次属于猜中，暂时不升级。")
        else:
            print("推理成功！答案正确，而且证据充分！")

        print("\n符合当前线索的身份组合：")
        for candidate in possibilities:
            print(
                "、".join(
                    f"{num}号={candidate[num]}"
                    for num in self.numbers
                )
            )

        print("\n本局真实身份：")
        for num, char in self.character_to_number.items():
            print(f"{num}号是{char}")

        # 自动升级
        if correct and provable:
            if self.level < 3:
                self.level += 1
                print(f"\n恭喜升级！下一关：Level {self.level}")
            else:
                print("\n恭喜！你已通关当前版本全部三个等级！")

    # 连续游戏
    def play_game(self):
        print("欢迎来到《猜猜谁是乱》！")

        while True:
            self.play_round()

            again = input("\n继续游戏？(y/n)：").strip().lower()

            if again != "y":
                print("游戏结束，下次见！")
                break


if __name__ == "__main__":
    game = GuessingGame()
    game.play_game()
