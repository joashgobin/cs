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


### Deleting, replacing and fixing changes
- **x** - delete character under cursor
- **r*char*** - replace character under cursor with *char*
- **dd** - delete current line
- **cc** - change current line
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
- **o*char*** - Jump to next line and enter Insert Mode
- **O*char*** - Jump to previous line and enter Insert mode
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

### Finding stuff
- **/*string*+enter** - Jump to first instance of *string* in the current file
- **n** - cycle through search results

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

## Command mode
- **:*command*** - Run *command*
- **:set spell** - Turn spell check on
- **:set nospell** - Turn spell check off

## Visual mode
- **=** - Indent highlighted text
