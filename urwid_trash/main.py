#!/usr/bin/env python3
import random
import sys
import signal
import urwid
from pathlib import Path


def get_answer_word():
    WORDS_FILE = Path('words.txt')

    if not WORDS_FILE.exists():
        print(f"Could not find {WORDS_FILE} file. Try running clean_words.py.")
        sys.exit(1)

    with WORDS_FILE.open() as f:
        dictonary = f.read().splitlines()

    word = random.choice(dictonary)

    return word


def compare_words(word1, word2):
    '''
    Compare word2 against word1, char by char, and compute score.

    score: List of 5 numbers.
        0: miss - Letter and position wrong
        1: near hit - Letter correct, position wrong
        2: hit - Letter and position correct
    '''
    score = []
    for char1, char2 in zip(word1, word2):
        if char2 not in word1:
            score.append(0)
        elif char2 is char1:
            score.append(2)
        else:
            score.append(1)

    return score


def main():
    # answer_word = get_answer_word()
    # print(f"answer_word: {answer_word}")

    # user_choice_word = input("Your choice? ")
    # score = compare_words(answer_word, user_choice_word)
    # print(f"score: {score}")
    pass


BLOCK = u"""
╭─────╮
│     │
╰─────╯
""".strip()
BLOCK_LETTER = u"""
╭─────╮
│  {}  │
╰─────╯
""".strip()

GRID = u"""
"""


def exit_on_q(key):
    if key in ('q', 'Q'):
        raise urwid.ExitMainLoop()


def exit_on_interrupt(signal_number, current_stack_frame):
    print("Exiting...")
    sys.exit(0)


def question():
    return urwid.Pile([urwid.Edit(u"What's your move?\n")])


def answer(name):
    return urwid.Text(('I say', u"Nice to meet you, " + name + "\n"))


class Tile(urwid.WidgetWrap):

    def __init__(self, text=' '):
        # self.tile = urwid.Text(BLOCK_LETTER.format('A '))
        self.tile = urwid.LineBox(urwid.Text(text, align='center'),
                                  tlcorner='╭',
                                  tline='─',
                                  lline='│',
                                  trcorner='╮',
                                  blcorner='╰',
                                  rline='│',
                                  bline='─',
                                  brcorner='╯')
        urwid.WidgetWrap.__init__(self, self.tile)


class Board(urwid.WidgetWrap):

    def __init__(self, tiles):
        x = [('weight', 0.2, tile) for tile in tiles]
        self.board = urwid.Columns(x)
        urwid.WidgetWrap.__init__(self, self.board)


# class PyrdleGame(urwid.WidgetWrap):

#     def __init__(self, first_screen):
#         self.board = urwid

if __name__ == "__main__":
    # Handle Ctrl+C
    signal.signal(signal.SIGINT, exit_on_interrupt)
    # main()
    palette = [('title', 'bold,underline', '')]

    title_text = urwid.Text(('title', u"Pyrdle - Not Yo Momma's Wordle"),
                            align='center')
    greeter_text = urwid.Text('''We'll assume you know Wordle and how to play.
        This one's harder cause the dictonary wasn't filtered through Mrs. Wordle so it has more words.
        ''',
                              align='center')
    instructions = urwid.Text("(To exit: q, Q, or Ctrl+C)", align='center')

    header = urwid.Pile([title_text, instructions])

    board = Board([Tile("A"), Tile(" "), Tile("C"), Tile("D"), Tile("E")])

    first_screen = urwid.Filler(urwid.Pile(
        [header, greeter_text, board, question()]),
                                valign='top')

    # game = PyrdleGame(first_screen)
    urwid.MainLoop(first_screen, palette, unhandled_input=exit_on_q).run()

    # BOLD = "\033[1m"
    # END = "\033[0m"
    # print(f"{BOLD}hello{END}")
    # print(f"hello")