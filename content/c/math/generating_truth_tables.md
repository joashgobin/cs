# Generating truth tables
We can use C's built-in logical operators for NOT, OR and AND in order to generate truth tables for
compound logical statements. An implication is simply logical equivalent to taking the negation
of the first proposition OR the second:

$$p\rightarrow q\equiv \neg p\lor q$$

We can thus write functions to return the result of each logical operation:
!{{./truth_tables.c}}

#### Challenge
Modify the code above to display the following compound propositions:
- $$\neg p \land \neg q$$
- $$\neg p \rightarrow \neg q$$ (inverse)
- $$q \rightarrow p$$ (converse)
- $$\neg q \rightarrow \neg p$$ (contrapositive)
