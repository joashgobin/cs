# Introduction
The NibbleSprouts project is aimed at highschool, university and returning students, particularly those with *limited resources* and *strict time constraints* and especially **working students**. 
The goal is to create a scalable and easily modifiable educational content delivery system. The articles created are to be used in conjunction with more conventional course material and internet APIs in order to fill in any "learning gaps".
This project should help students to partake in **mastery learning**. It is *not* intended to be used as *mere crash course content*.

## Features
This article will show you the basic features of the NibbleSprouts static site generator. Articles are written in a *modified markdown syntax* and **converted to html** when the site is generated.

### Typesetting
You can include equations. The MathML rendering is handled by *$\KaTeX$*. It supports inline mode e.g. $\sin{x}$ and display mode:

$$T=2\pi \sqrt{\frac{l}{g}}$$

This feature makes representing mathematical concepts easier.

### Code snippets
You can include code snippets. The syntax highlighting theme used is rose-pine (via **highlight js**):

!{{./c/constructs/iterative_constructs/for_loops.c}}

This feature was added as a way to include code directly from the user's device without them having to copy and paste it manually. The little arrow can be clicked to open the code snippet in a new tab.

### Bible verses
Bible verses are accessible thanks to the **pythonbible** package and can be added by 
specifying book chapter and verse:
!bible{{John 3:16}}

You can also insert multiple verses:
!bible{{John 1:1-3}}

This feature allows the user to quickly reference Bible verses without having to exit 
their markdown editor to copy and paste Scripture.

#### Planned features
The following features are to be implemented:
- Youtube video embeds
- Embedded quizzes
