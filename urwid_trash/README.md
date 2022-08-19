# Design Thoughts

## User POV
On run,
    Instructions are printed
        how to play
    Keyboard heatmap is shown, uncolored
    User is prompted for word
        How many guesses remaining is shown
    Word is drawn
        It's colored like the wordle colors
        Keyboard is shaded accordingly
    Repeat...
### Mockup

                Pyrdle - Not Yo Momma's Wordle
                (To exit: q, Q, or Ctrl+C)
    We'll assume you know Wordle and how to play. This one's harder cause the 
    dictonary wasn't filtered through Mrs. Wordle so it has more words.
    ╭───╮╭───╮╭───╮╭───╮╭───╮
    │   ││   ││   ││   ││   │
    ╰───╯╰───╯╰───╯╰───╯╰───╯
    What's your move?
    <user input>adieu
    ----------------------------------------------------------------------------
                Pyrdle - Not Yo Momma's Wordle
                (To exit: q, Q, or Ctrl+C)
    <stylized>ADIEU
    <red>5 moves remaing<red>What's your move?
    <user input>short
    ----------------------------------------------------------------------------
                Pyrdle - Not Yo Momma's Wordle
                (To exit: q, Q, or Ctrl+C)
    <stylized>ADIEU
    <stylized>SHORT
    <red>4 moves remaing<red>What's your move?
    <user input>split
    ----------------------------------------------------------------------------
                Pyrdle - Not Yo Momma's Wordle
                (To exit: q, Q, or Ctrl+C)
    <stylized>ADIEU
    <stylized>SHORT
    <stylized>SPLIT
    <green>success message<green>
    Play again (y/n)?

    ----------------------------------------------------------------------------
                Pyrdle - Not Yo Momma's Wordle
                (To exit: q, Q, or Ctrl+C)
    <stylized>ADIEU
    <stylized>SHORT
    <stylized>SPLIT
    <stylized>FORMS
    <stylized>REGAL
    <stylized>AREAS
    <red>you lose bitch<red>
    Play again (y/n)?

## Game Logic
On run,
    pick word from dictonary
    get user input
    check user word against answer word character by character
        important: letter and position
        Quality of guesses:
            - miss: Letter and position wrong
            - near hit: Letter correct, position wrong
            - hit: Letter and position correct

## Wireframe
- top_window: The main windows. Holds everything. Must be a Box Widget
    - Overlay
        - bottom: SolidFill to make background
        - top: Pile as main_pile
- main_pile: Pile with 3 items
    - Header
    - Board
    - QuestionBox
- Header:
    - Text box
- Board
    - Grid Widget
        - 6 Columns Widgets
            - 5 custom Tile Widgets
- Custom Tile Widget
    - ???
- QuestionBox
    - Text Box that doesnt change until game end
    - Edit box that takes input and clears after entry
