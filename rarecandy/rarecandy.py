import readline
import os
import random
from enum import Enum
from typing import List


PROBLEM_FILEPATH = 'problem.csv'


def input_int(min_no: int, max_no: int) -> int:
    no = min_no - 1
    while no < min_no or max_no < no:
        print('> ', end='')
        input_no_str = input()
        try:
            no = int(input_no_str)
        except ValueError:
            no = min_no - 1
        if no < min_no or max_no < no:
            print(f'{min_no}から{max_no}までの数を入力してください')
    return no


class FrontMenu(Enum):
    PLAY_NORMAL = '通常モードでプレイ'
    PLAY_RANDOM = 'ランダムモードでプレイ'
    DISPLAY = '問題を表示する'
    REGISATER = '問題を登録する'
    DELETE = '問題を削除する'
    EXIT = '終了'


class DisplayMenu(Enum):
    DETAIL = '詳細を見る'
    EXIT = '閲覧終了'


class RegisterMenu(Enum):
    REGISTER = '選択肢を追加する'
    EXIT = '登録終了'


class DeleteMenu(Enum):
    DELETE = '問題を削除する'
    EXIT = '削除終了'


class Problem:
    def __init__(self, sentence: str, ans_idx: int, choice_lst: List[str]):
        self.sentence = sentence
        self.ans_idx = ans_idx
        self.choice_lst = choice_lst

    def tolist(self) -> List[str]:
        return [self.sentence, str(self.ans_idx)] + self.choice_lst


class Game:
    def __init__(self):
        self.problem_lst = []
        if os.path.isfile(PROBLEM_FILEPATH):
            with open(PROBLEM_FILEPATH, 'r') as f:
                for line in f:
                    cell_lst = line.split(',')
                    self.problem_lst.append(
                        Problem(cell_lst[0], int(cell_lst[1]), cell_lst[2:]))

    def __play(self, problem_lst: List[Problem]):
        print()
        if len(problem_lst) == 0:
            print('登録されている問題がありません\n')
            return
        for i, problem in enumerate(problem_lst):
            print(f'[問題{i}] {problem.sentence}')
            correct = False
            while not correct:
                for j, choice in enumerate(problem.choice_lst):
                    print(f'{j}) {choice}')
                input_ans = input_int(0, len(problem.choice_lst) - 1)
                correct = input_ans == problem.ans_idx
                if correct:
                    print('O\n')
                else:
                    print('X\n')

    def play_normal(self):
        self.play(self.problem_lst)

    def play_random(self):
        problem_lst_copy = self.problem_lst.copy()
        random.shuffle(problem_lst_copy)
        self.play(problem_lst_copy)

    def display(self):
        print()
        if len(self.problem_lst) == 0:
            print('登録されている問題がありません\n')
            return
        for i, problem in enumerate(self.problem_lst):
            print(f'{i}) {problem.sentence}')
        print()
        menu_no = 0
        while list(DisplayMenu)[menu_no] != DisplayMenu.EXIT:
            for i, menu in enumerate(DisplayMenu):
                print(f'{i}) {menu.value}')
            menu_no = input_int(0, len(DisplayMenu) - 1)
            print()
            if list(DisplayMenu)[menu_no] == DisplayMenu.DETAIL:
                print('詳細を見たい問題の番号を入力してください')
                no = input_int(0, len(self.problem_lst) - 1)
                print()
                problem = self.problem_lst[no]
                print(f'問題文) {problem.sentence}')
                print(f'正解番号) {problem.ans_idx}')
                for i, choice in enumerate(problem.choice_lst):
                    print(f'選択肢{i}) {choice}')
                print()
                for i, problem in enumerate(self.problem_lst):
                    print(f'{i}) {problem.sentence}')
                print()

    def register(self):
        print('\n問題文を入力してください')
        input_sentence = ''
        while len(input_sentence) == 0:
            print('> ', end='')
            input_sentence = input().strip()
            print()
        input_choice_lst = []
        menu_no = 0
        while list(RegisterMenu)[menu_no] != RegisterMenu.EXIT or len(input_choice_lst) == 0:
            for i, menu in enumerate(RegisterMenu):
                print(f'{i}){menu.value} ', end='')
            print()
            menu_no = input_int(0, len(RegisterMenu) - 1)
            print()
            if list(RegisterMenu)[menu_no] == RegisterMenu.REGISTER:
                input_choice = ''
                while len(input_choice) == 0:
                    print(f'選択肢{len(input_choice_lst)} > ', end='')
                    input_choice = input().strip()
                    print()
                input_choice_lst.append(input_choice)
            if len(input_choice_lst) == 0:
                print('最低1つ選択肢を登録してください\n')
        print('正解番号を入力してください')
        input_ans_idx = input_int(0, len(input_choice_lst) - 1)
        self.problem_lst.append(Problem(input_sentence, input_ans_idx, input_choice_lst))
        line_lst = []
        for problem in self.problem_lst:
            line = ','.join(problem.tolist())
            line_lst.append(line)
        with open(PROBLEM_FILEPATH, 'w') as f:
            f.write('\n'.join(line_lst))
        print()

    def delete(self):
        print()
        menu_no = 0
        while list(DeleteMenu)[menu_no] != DeleteMenu.EXIT:
            for i, menu in enumerate(DeleteMenu):
                print(f'{i}){menu.value} ', end='')
            print()
            menu_no = input_int(0, len(DeleteMenu) - 1)
            print()
            if list(DeleteMenu)[menu_no] == DeleteMenu.DELETE:
                if len(self.problem_lst) > 0:
                    for i, problem in enumerate(self.problem_lst):
                        print(f'{i}) {problem.sentence}')
                    print('消去する問題番号を入力してください')
                    no = input_int(0, len(self.problem_lst) - 1)
                    self.problem_lst.pop(no)
                    line_lst = []
                    for problem in self.problem_lst:
                        line = ','.join(problem.tolist())
                        line_lst.append(line)
                    with open(PROBLEM_FILEPATH, 'w') as f:
                        f.write('\n'.join(line_lst))
                else:
                    print('登録されている問題がありません\n')


def main():
    print('-*-' * 15 + ' Rare Candy ' + '-*-' * 15)
    game = Game()
    menu_no = 0
    while list(FrontMenu)[menu_no] != FrontMenu.EXIT:
        for i, menu in enumerate(FrontMenu):
            print(f'{i}){menu.value} ', end='')
        print()
        menu_no = input_int(0, len(FrontMenu) - 1)
        if list(FrontMenu)[menu_no] == FrontMenu.PLAY_NORMAL:
            game.play_normal()
        elif list(FrontMenu)[menu_no] == FrontMenu.PLAY_RANDOM:
            game.play_random()
        elif list(FrontMenu)[menu_no] == FrontMenu.DISPLAY:
            game.display()
        elif list(FrontMenu)[menu_no] == FrontMenu.REGISATER:
            game.register()
        elif list(FrontMenu)[menu_no] == FrontMenu.DELETE:
            game.delete()
    print('-*-' * 15 + ' See you ' + '-*-' * 15)


if __name__ == '__main__':
    main()
