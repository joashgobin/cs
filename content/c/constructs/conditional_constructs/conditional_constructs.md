# Conditional Constructs
In solving a problem, we sometimes want to execute a block of code if one or more conditions are met.
We use *conditional constructs* in order to specify actions and the criteria required for those actions to be executed.
In C, we have two (2) main conditional constructs:
- If-else statements
- Switch-case statements

## If-else
These are used to create multiple branching paths in our code. **Only one** branch
is executed if its condition is satisfied. All branches following it are ignored.
!{{./if_else.c}}

## Switch-case
In this statement, it is possible for all branches to run if we do not place the **break** statement
at the end of each case:
!{{./switch_case.c}}
