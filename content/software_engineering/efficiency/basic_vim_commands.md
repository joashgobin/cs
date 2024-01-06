# Basic Vim Commands
Here is a list of some basic commands in Vim. Vim has four (4) modes:
- Normal mode
- Insert mode
- Visual mode
- Command mode

## Normal mode
The following commands are used in normal mode.

### Basic movement
- **h** - Move cursor left
- **j** - Move cursor down
- **k** - Move cursor up
- **l** - Move cursor right
- **w** - Move cursor to the beginning of the next word, defined by non-white space character
- **W** - Move cursor to the beginning of the next word, defined by white space character
- **b** - Move cursor to the beginning of the previous word, defined by non-white space character
- **B** - Move cursor to the beginning of the previous word, defined by white space character
- **e** - Move cursor to the next end of word, defined by non-white space character
- **E** - Move cursor to the next end of word, defined by white space character

### Deleting, replacing and fixing changes
- **x** - Delete character under cursor
- **r*char*** - Replace character under cursor with *char*
- **dd** - Delete current line
- **D** - Delete to the end of the current line
- **cc** - Change current line
- **C** - Delete to the end of the current line and enter Insert mode
- **u** - Undo last change
- **Ctrl+r** - Redo last change
- **U** - Fix entire line

### Copying and pasting
- **yy** - Yank current line
- **p** - Paste last yanked or deleted text
- **Shift+v** - Enter Visual line mode and highlight the current line; This text can then be deleted (d or x)
or yanked (y)

### Horizontal movement and actions
- **_** - Jump to first non-white space character in current line
- **0** - Jump to beginning of current line
- **$** - Jump to end of current line
- **i** - Enter Insert mode and start inserting before current cursor position
- **I** - Enter Insert mode and start inserting at the first non-white space character in current line
- **a** - Enter Insert mode and start inserting after current cursor position
- **A** - Enter Insert mode and start inserting after the last character in current line
- **s** - Delete the character under the cursor and Enter Insert mode
- **S** - Change the current line and indent to where Vim infers that the cursor should be in the current line 
- **f*char*** - Jump to position of first instance of *char* in current line
- **F*char*** - Jump to position of previous instance of *char* in current line
- **t*char*** - Jump to position just before next instance of *char* in current line
- **T*char*** - Jump to position just before previous instance of *char* in current line
- **; and ,** - Cycle between *char* selected using **f**,**F**,**t** or **T**
- **di*char*** - Delete in between *char*
- **ci*char*** - Delete all text between instances of *char* in the current line and place the cursor in between
and enter Insert mode; The text must be enclosed by two instances of the *char*
- **yi*char*** - Yank everything in between *char*

### Vertical movement and actions
- **gg** - Go to first line of file
- **G** - Go to last line of file
- **:*line_number*** - Jump to line number *line_number*
- **o*char*** - Jump to next line and enter Insert Mode
- **O*char*** - Jump to previous line and enter Insert mode

### Finding stuff
- **/*string*+enter** - Jump to next instance of *string* in the current file
- **?*string*+enter** - Jump to previous instance of *string* in the current file
- * - Search forwards for word (bounded) under cursor
- g* - Search forwards for word (unbounded) under cursor
- **#** - Search backwards for word (bounded) under cursor
- **g#** - Search backwards for word (unbounded) under cursor
- **n** - cycle forwards through search results; reversed for ?
- **N** - cycle backwards through search results; reversed for ?
- **]s** - Jump to next misspelled word
- **[s** - Jump to previous misspelled word
- **zg** - Add current word to Vim's dictionary
- **zw** - Remove current word from Vim's dictionary

### Placing the cursor relative to the window
- **L** - Place the cursor low
- **M** - Place the cursor middle
- **H** - Place the cursor high
- **Ctrl+d** - Shift the cursor down half a screen
- **Ctrl+u** - Shift the cursor up half a screen

## Insert mode
- **Ctrl+o+Normal mode command** - Run a command as if in Normal mode but remain in Insert mode
- **Ctrl+w** - Delete previous word
- **Ctrl+u** - Delete entire line before cursor
- **Ctrl+[** - Exit out of Insert mode to the left of the cursor

## Command mode
- **:*command*** - Run *command*
- **:set spell** - Turn spell check on
- **:set nospell** - Turn spell check off

## Visual mode
- **=** - Indent highlighted text
