#!/usr/bin/env python3

from urwid import MainLoop, SolidFill, AttrMap, Padding, Filler, WidgetWrap, LineBox, Text, Pile, Overlay, Columns

BLOCK = u"""
  {}  
""".strip()
BLOCK_LETTER = u"""
╭─────╮
│  {}  │
╰─────╯
""".strip()

# class Tile(WidgetWrap):

#     def __init__(self, background, text=' ', size=4):
#         self.text = Text(text)
#         self.fill = AttrMap(SolidFill(" "), background)
#         self.background = Filler(Padding(self.fill, width=size), height=size)

#         self.letter = LineBox(self.text,
#                               tlcorner='╭',
#                               tline='─',
#                               lline='│',
#                               trcorner='╮',
#                               blcorner='╰',
#                               rline='│',
#                               bline='─',
#                               brcorner='╯')
#         self.tile = Overlay(self.letter,
#                             self.background,
#                             align='center',
#                             width=30,
#                             valign='middle',
#                             height=10)
#         WidgetWrap.__init__(self, self.tile)


def make_tile():
    text = Text(BLOCK.format('A'), align='center')
    l = LineBox(text,
                tlcorner='╭',
                tline='─',
                lline='│',
                trcorner='╮',
                blcorner='╰',
                rline='│',
                bline='─',
                brcorner='╯')

    letter = Filler(AttrMap(Pile([l]), 'basic'))

    tile = letter

    return tile


def make_header():
    title_text = Text(('title', u"Pyrdle - Not Yo Momma's Wordle"),
                      align='center')
    instructions = Text("(To exit: q, Q, or Ctrl+C)", align='center')
    greeter_text = Text('''We'll assume you know Wordle and how to play.
      This one's harder cause the dictonary wasn't filtered through Mrs. Wordle so it has more words.
      ''',
                        align='center')

    header = Pile([title_text, instructions, greeter_text])

    return header


def make_row():
    tiles = [(7, make_tile()) for i in range(0, 5)]
    row = Columns(tiles, dividechars=1)

    return row


def make_board():
    rows = [make_row() for i in range(0, 6)]
    board = Pile(rows)

    return board


def make_main_window():
    # bottom = AttrMap(SolidFill(" "), 'background')

    header = make_header()
    board = make_board()
    top = Pile([header, board])

    return top


color = [('basic', '', '', '', 'h224', 'h16'),
         ('hit_letter', '', '', '', 'h16', 'h151'),
         ('near_hit_letter', '', '', '', 'h16', 'h223'),
         ('background', '', '', '', 'h53', 'h53')]

top = make_main_window()

mainloop = MainLoop(top, color)
mainloop.screen.set_terminal_properties(colors=256)
mainloop.run()