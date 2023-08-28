import random


class GuessingGame:
    def __init__(self):
        self.characters = ["温", "顺", "乱"]
        self.numbers = ["1", "2", "3"]
        random.shuffle(self.characters)
        self.character_to_number = {num: char for num, char in zip(self.numbers, self.characters)}
        self.answers = {}

    def generate_answers(self):
        for num in self.numbers:
            other_numbers = [n for n in self.numbers if n != num]
            answer = random.choice(other_numbers)
            self.answers[num] = self.character_to_number[answer]

    def play_game(self):
        self.generate_answers()

        for num, answer in self.answers.items():
            print(f"{num}说：{answer}")

        guess = int(input("请输入你猜测是乱的角色的序号： "))
        guessed_character = self.character_to_number.get(str(guess))

        if guessed_character == "乱":
            print("恭喜！你猜对了。")
        else:
            print("很抱歉，你猜错了。")


if __name__ == "__main__":
    game = GuessingGame()
    game.play_game()
