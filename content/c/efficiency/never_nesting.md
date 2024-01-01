# Never Nesting
This is the practice of preventing code from becoming too long horizontally. When too much
code is nested, the text we need to navigate horizontally grows to be unmanageable.

Two techniques we use to reduce nesting are:
- Extraction
- Inversion

## Extraction
Here we extract a block of code and place it within a function. We then call that function
from where the code block used to be.
!{{./extraction.c}}

## Inversion
Here we write *guard clauses* instead of nesting a bunch of conditional statements. We
place the most common behaviour and place *condition checks* before it to prevent (guard) unwanted states
from reaching that common behaviour.

We place the guard clauses **before** the common behaviour 
because the code is executed from top to bottom.

!{{./guard_clause.c}}

Notice that we cater for the exceptions (when the person is at least 65 and when the
person is at least 18). We use *return* to prevent the code from ever reaching the 
**printf("You are not an adult\n")**.
