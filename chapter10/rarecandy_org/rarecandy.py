from pathlib import Path
from enum import Enum
import readline
import random


PROBLEMS_FILEPATH = Path(__file__).parent / "problems.csv"


class FrontMenu(Enum):
    PLAY_NORMAL = "通常モードでプレイ"
    PLAY_RANDOM = "ランダムモードでプレイ"
    DISPLAY = "問題を表示する"
    REGISTER = "問題を登録する"
    DELETE = "問題を削除する"
    EXIT = "終了"


class DisplayMenu(Enum):
    DETAIL = "詳細を見る"
    EXIT = "閲覧終了"


class RegisterMenu(Enum):
    REGISTER = "選択肢を追加する"
    EXIT = "追加完了"


class DeleteMenu(Enum):
    DELETE = "問題を削除する"
    EXIT = "削除完了"


class Problem:
    def __init__(self, sentence, ans_no, *choices):
        self.sentence = sentence
        self.ans_no = int(ans_no)
        self.choices = list(choices)

    def __repr__(self):
        return f"Problem(sentence={self.sentence}, ans_no={self.ans_no}, choices={self.choices})"

    def tolist(self):
        return [self.sentence, str(self.ans_no)] + self.choices


def input_int(min_no, max_no):
    no = min_no - 1
    while not (min_no <= no <= max_no):
        print("> ", end="")
        input_no_str = input()
        try:
            no = int(input_no_str)
        except ValueError:
            no = min_no - 1
        if not (min_no <= no <= max_no):
            print(f"{min_no}から{max_no}までの数を入力してください")
    return no


def load_problems():
    problems = []
    with open(PROBLEMS_FILEPATH, "r") as f:
        for line in f:
            problems.append(Problem(*line.strip().split(",")))
    return problems


def play(problems):
    if len(problems) == 0:
        print("登録されている問題がありません")
        return

    for i, problem in enumerate(problems):
        correct = False
        while not correct:
            print(f"[問題{i}] {problem.sentence}")
            for j, choice in enumerate(problem.choices):
                print(f"{j}) {choice}")

            input_ans = input_int(0, len(problem.choices) - 1)

            correct = input_ans == problem.ans_no
            if correct:
                print("O")
            else:
                print("X")


def play_normal():
    problems = load_problems()
    play(problems)


def play_random():
    problems = load_problems()
    random.shuffle(problems)
    play(problems)


def display():
    problems = load_problems()

    if len(problems) == 0:
        print("登録されている問題がありません")
        return

    for i, problem in enumerate(problems):
        print(f"[{i}] {problem.sentence}")
    print()

    menu_no = 0
    while list(DisplayMenu)[menu_no] is not DisplayMenu.EXIT:
        for i, menu in enumerate(DisplayMenu):
            print(f"{i}) {menu.value} ", end="")

        menu_no = input_int(0, len(DisplayMenu) - 1)

        if list(DisplayMenu)[menu_no] is DisplayMenu.DETAIL:
            print("詳細を見たい問題の番号を入力してください")

            no = input_int(0, len(problems) - 1)

            problem = problems[no]
            print(f"問題文) {problem.sentence}")
            print(f"正解番号) {problem.ans_no}")
            for i, choice in enumerate(problem.choices):
                print(f"選択肢{i}) {choice}")
            print()

            for i, problem in enumerate(problems):
                print(f"[{i}] {problem.sentence}")
            print()


def register():
    print("問題文を入力してください")
    input_sentence = ""
    while len(input_sentence) == 0:
        print("> ", end="")
        input_sentence = input().strip()

    input_choices = []
    menu_no = 0
    while list(RegisterMenu)[menu_no] is not RegisterMenu.EXIT or len(input_choices) == 0:
        for i, menu in enumerate(RegisterMenu):
            print(f"{i}){menu.value} ", end="")
        print()

        menu_no = input_int(0, len(RegisterMenu) - 1)
        if list(RegisterMenu)[menu_no] is RegisterMenu.REGISTER:
            input_choice = ""
            while len(input_choice) == 0:
                print(f"選択肢{len(input_choices)} > ", end="")
                input_choice = input().strip()
            input_choices.append(input_choice)

        if len(input_choices) == 0:
            print("最低1つ選択肢を追加してください")

    print("正解の選択肢番号を入力してください")
    input_ans_no = input_int(0, len(input_choices) - 1)

    problem = Problem(input_sentence, input_ans_no, *input_choices)
    with open(PROBLEMS_FILEPATH, "a") as f:
        f.write(",".join(problem.tolist()) + "\n")


def delete():
    problems = load_problems()

    menu_no = 0
    while list(DeleteMenu)[menu_no] is not DeleteMenu.EXIT:
        for i, problem in enumerate(problems):
            print(f"[{i}] {problem.sentence}")
        print()

        for i, menu in enumerate(DeleteMenu):
            print(f"{i}){menu.value} ", end="")
        print()

        menu_no = input_int(0, len(DeleteMenu) - 1)

        if list(DeleteMenu)[menu_no] is DeleteMenu.DELETE:
            if len(problems) > 0:
                print("削除する問題番号を入力してください")

                no = input_int(0, len(problems) - 1)

                problems.pop(no)
                lines = []
                for problem in problems:
                    line = ",".join(problem.tolist()) + "\n"
                    lines.append(line)

                with open(PROBLEMS_FILEPATH, "w") as f:
                    f.writelines(lines)
            else:
                print("登録されている問題がありません")


def main():
    menu_no = 0
    while list(FrontMenu)[menu_no] is not FrontMenu.EXIT:
        for i, menu in enumerate(FrontMenu):
            print(f"{i}){menu.value} ", end="")
        print()

        menu_no = input_int(0, len(FrontMenu) - 1)
        if list(FrontMenu)[menu_no] is FrontMenu.PLAY_NORMAL:
            play_normal()
        elif list(FrontMenu)[menu_no] is FrontMenu.PLAY_RANDOM:
            play_random()
        elif list(FrontMenu)[menu_no] is FrontMenu.DISPLAY:
            display()
        elif list(FrontMenu)[menu_no] is FrontMenu.REGISTER:
            register()
        elif list(FrontMenu)[menu_no] is FrontMenu.DELETE:
            delete()
    print("終了")


if __name__ == "__main__":
    main()
