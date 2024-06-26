# Basic Vim Commands
Here is a list of some basic commands in Vim. Vim has four (4) modes:
- Normal mode
- Insert mode
- Visual mode
- Command mode

## Normal mode
The following commands are used in normal mode.

- **.** - Replay last command
- **J** - Join the next line to the end of the current line
- **Ctrl+w followed by j,k,h,l,w** - Switch between windows

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
- **_** - Move to the first non-white space character in current line
- **0** - Move to the zeroth character in current line
- **$** - Move to the end of current line

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
- **p** - Paste last yanked or deleted text after cursor
- **P** - Paste last yanked or deleted text before cursor
- **Shift+v** - Enter Visual line mode and highlight the current line; This text can then be deleted (d or x)
or yanked (y)
- **Ctrl+v** - Enter visual block mode
- **I** - Insert at the beginning of selected each line in the visual block

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
- **gv** - Go to text previously selected in Visual Mode
- **:*line_number*** - Jump to line number *line_number*
- **o*char*** - Insert line below current line and enter Insert Mode
- **O*char*** - Insert line above current line and enter Insert Mode
- **[[** and **]]** - jump between sections of text
- **{** and **}** - jump between paragraphs

### Finding stuff
- **/*string*+enter** - Jump to next instance of *string* in the current file
- **?*string*+enter** - Jump to previous instance of *string* in the current file
- **//+enter** - Repeat the last search
- **\*** - Search forwards for word (bounded) under cursor
- **g*** - Search forwards for word (unbounded) under cursor
- **#** - Search backwards for word (bounded) under cursor
- **g#** - Search backwards for word (unbounded) under cursor
- **n** - cycle forwards through search results; reversed for ?
- **N** - cycle backwards through search results; reversed for ?
- **]s** - Jump to next misspelled word
- **[s** - Jump to previous misspelled word
- **zg** - Add current word to Vim's dictionary
- **zw** - Remove current word from Vim's dictionary
- **z=** - Open a list of word suggestions for the current word
- **1z=** - Replace the current word with the 1st suggestion in the list of word suggestions

## Search and replace
- **:%s/*old_string*/*next_string*/g** - replace *old_string* with *new_string* globally

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
- **:!*command*** - Run shell command
- **:set spell** - Turn spell check on
- **:set nospell** - Turn spell check off
- **:norm**+instructions listed out - do list of normal mode instructions
- **:norm ma [s 1z= &#96;a** - set mark **a** at current cursor position, jump previous spelling error, correct to the
1st suggestion and then return to the mark **a**. Use 'a instead of &#96;a to jump to the beginning of the marked line instead of the
marked cursor position

## Visual mode
- **=** - Auto-indent highlighted text
- **<** - Decrease indent for highlighted text
- **>** - Increase indent for highlighted text
- **:norm *commands*** - Run Normal mode commands on each line in the Visual Line mode
- **o** - Jump to other end of current selection

## Crazy combos
- **ddp** - swap the current line and the line below
- **viw** - select in word
- **vf<** - select to opening angled bracket
- **vt<** - select to but not including opening angled bracket
- **vaw** - select around word
- **vis** - select inside sentence
- **vas** - select around sentence
- **vip** - select inside paragraph
- **vap** - select around paragraph
- **vi{** - select the contents within { and }
- **va{** - select the contents including the { and }
- **va"** - select string within the quotation marks
- **va"** - select string including the quotation marks
- **vit** - select inside of html tags
- **vat** - select html element

Try these with **d**, **c** and **y** instead of **v**.

- **5i**+text+Esc - copy this text for 5 instances in the current line when Insert Mode is exited
- **5o**+text+Esc - go into the next line and enter Insert Mode; copy this text for 5 lines when Insert Mode is exited

- **guaw** - convert word to lowercase
- **gUaw** - convert word to uppercase - this can be done for sentences, paragraphs, and other text objects

## Registers
- **:reg** - view the registers in vim
- **"1y** - yank into register 1
- **"1p** - paste from register 1
- **"+y** - yank into system register
- **"+p** - paste from system register

### Macros
- **qa**+commands+**q** - start recording macro in register a
- **@a** - replay macro stored in a
- **@@** - replay last macro

## File browsing
- **:Ex** - open current directory
- **d** - Initiate directory creation
- **%** - Initiate file creation
