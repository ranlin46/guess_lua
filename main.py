
import random


class GuessingGame:
    def __init__(self):
        self.characters = ["温", "顺", "乱"]
        self.numbers = ["1", "2", "3"]

        random.shuffle(self.characters)

        self.character_to_number = {
            num: char
            for num, char in zip(self.numbers, self.characters)
        }

        self.answers = {}

    # 第一次发言
    def generate_answers(self):
        for num in self.numbers:
            other_numbers = [
                n for n in self.numbers if n != num
            ]

            answer = random.choice(other_numbers)

            self.answers[num] = self.character_to_number[answer]

    # 第二次发言
    def ask_again(self, num):
        real_character = self.character_to_number[num]
        first_answer = self.answers[num]

        second_answer = [
            char for char in self.characters
            if char != real_character and char != first_answer
        ][0]

        return second_answer

    # 游戏主流程
    def play_game(self):
        self.generate_answers()

        print("=== 猜猜谁是乱 ===")
        print("每个人都不会说出自己的真实身份！")

        for num, answer in self.answers.items():
            print(f"{num}说：{answer}")

        # 玩家可以选择追问，也可以直接猜测
        while True:
            ask_num = input(
                "你想追问几号？请输入1、2、3，输入0跳过追问："
            )

            if ask_num == "0":
                print("你选择不追问，直接猜测！")
                break

            elif ask_num in self.numbers:
                second_answer = self.ask_again(ask_num)
                print(f"{ask_num}第二次说：{second_answer}")
                break

            else:
                print("无效的编号，请重新输入！")

        # 玩家猜测
        while True:
            guess = input(
                "现在你认为谁是乱？请输入1、2或3："
            )

            if guess in self.numbers:
                break
            else:
                print("无效的编号，请重新输入！")

        guessed_character = self.character_to_number[guess]

        if guessed_character == "乱":
            print("恭喜！你猜对了。")
        else:
            print("很抱歉，你猜错了。")

        # 公布真实身份
        print("真实身份：")
        for num, char in self.character_to_number.items():
            print(f"{num}号是{char}")


if __name__ == "__main__":
    game = GuessingGame()
    game.play_game()
