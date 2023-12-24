# Introduction
This article will show you the basic features of our static site generator. Articles are written in a *modified markdown syntax* and **converted to html** when the site is generated.

You can include equations. The rendering is handled by $\KaTeX$. It supports inline mode e.g. $\sin{x}$ and a display mode:

$$T=2\pi = \sqrt{\frac{l}{g}}$$

This feature makes representing mathematical concepts easier.

You can include code snippets:

!{{./c/constructs/iterative_constructs/for_loops.c}}

This feature was added as a way to include code directly from the user's device without them having to copy and paste it manually. The little arrow can be clicked to open the code snippet in a new tab.
