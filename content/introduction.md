# Introduction
The NibbleSprouts project is aimed at highschool, university and returning students, particularly those with *limited resources* and *strict time constraints* and especially **working students**. 
The goal is to create a scalable and easily modifiable educational content delivery system. The articles created are to be used in conjunction with more conventional course material and internet APIs in order to fill in any "learning gaps".
This project should help students to partake in **mastery learning**, *not* serving as *mere crash course content*.

## Features
This article will show you the basic features of our static site generator. Articles are written in a *modified markdown syntax* and **converted to html** when the site is generated.

You can include equations. The rendering is handled by $\KaTeX$. It supports inline mode e.g. $\sin{x}$ and a display mode:

$$T=2\pi = \sqrt{\frac{l}{g}}$$

This feature makes representing mathematical concepts easier.

You can include code snippets:

!{{./c/constructs/iterative_constructs/for_loops.c}}

This feature was added as a way to include code directly from the user's device without them having to copy and paste it manually. The little arrow can be clicked to open the code snippet in a new tab.

#### Planned features
The following features are to be implemented:
- Bible verses
- Youtube video embeds
- Embedded quizzes
