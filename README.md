# Pyrdle
A failed attempt at making a Wordle clone.

I wanted it to be a TUI application and I first tried [`urwid`](https://urwid.org/). It seems to be more of a UI widget construction library than a plug-and-play framework. My extreme lack of UI programming meant the amount of time it would have taken me to figure out wasn't worth it. Better spent on other projects.

I found [this lovely implementation](https://github.com/frostming/wordle-tui) and it's eerily similar to what I had mind for my program, particularly the look-and-feel. Good job @frostming!

The above project used a different library called [`textual`](https://github.com/Textualize/textual). I tried using it but there wasn't enough documentation (at the time) for a noob like me. You needed to read library source code to see all the stuff it could do. See the point above about spending personal project time wisely.

## Source Details
I write these details months after I wrote the source code so I'm probably forgetting a bunch of stuff...but! I usually comment code pretty well.

- `raw_words.txt`: Raw dictionary of words to make Wordle games out of
- `clean_words.py`: Bunch of word wrangling to get 5 letter, reasonable words to play
- `words.txt`: Bunch of 5 letter words, perfect to Wordle with
- `colortrans.py`: Stolen (but credited!) script to convert RGB hex codes and xterm-256 color codes
- `urwid_trash`: The failed attempt with `urwid`
    - `plan.txt`: Trying to visual the game board
    - `README.md`: More design musings. These seem to be for a simpler, text-based approach
    - `main.py`: Wordle game logic and real attempts at drawing TUI frontend
    - `demo.py`: Trying to figure out `urwid` without Wordle logic in the way

Everything else looks related to my `textual` attempts:
- `textual_notes.md`: Scribbles from their tutorial
- `demo.py`: Took an example from vendor repo and tried modifying to a Pyrdle game.
