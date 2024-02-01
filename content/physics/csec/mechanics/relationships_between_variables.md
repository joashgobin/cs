# 1.11 Relationships
Now that we have studied the various types of variables, we can learn to describe the relationships between variables. There are three(3) types of relationships:
1. **Direct relationship**: If we increase one variable then the other variable increases. If we decrease one, the other decreases.
2. **Inverse relationship**: Increasing one variable decreases the other
3. **No relationship**: Increasing/decreasing one variable shows no noticeable change in the other variable

## What do they look like?
If we plot graphs of *one variable versus the other* then we can tell the relationship by looking at the **best fit line**/regression line/trend line.
- Direct relationships produce a best fit line with a **positive gradient** (resembles a forward slash, $/$)

```tikz
\usepackage{pgfplots}
\begin{document}
\begin{tikzpicture}[domain=-10:10]
\begin{axis}[axis lines=middle,clip=false,scale=1.2]
\addplot[color=black]coordinates{(1,1) (3,3)};
\addplot[color=black] coordinates{(0,0)};
\addplot[color=black] coordinates{(0,4)};
\addplot[color=black] coordinates{(4,0)};
\node [right] at (current axis.right of origin) {$variable\ 1$};
\node [above] at (current axis.above origin) {$variable\ 2$};
\end{axis}
\end{tikzpicture}
\end{document}
```

- Inverse relationships produce a best fit line with a **negative gradient** (resembles a backward slash, $\backslash$)

```tikz
\usepackage{pgfplots}
\begin{document}
\begin{tikzpicture}[domain=-10:10]
\begin{axis}[axis lines=middle,clip=false,scale=1.2]
\addplot[color=black] coordinates{(1,3) (3,1)};
\addplot[color=black] coordinates{(0,0)};
\addplot[color=black] coordinates{(0,4)};
\addplot[color=black] coordinates{(4,0)};
\node [right] at (current axis.right of origin) {$variable\ 1$};
\node [above] at (current axis.above origin) {$variable\ 2$};
\end{axis}
\end{tikzpicture}
\end{document}
```

- When there is no relationship, the best fit line can be horizontal (**gradient is zero**) or vertical (**gradient is undefined**)

```tikz
\usepackage{pgfplots}
\begin{document}
\begin{tikzpicture}[domain=0:5]
\begin{axis}[axis lines=middle,clip=false,scale=1.2]
\addplot[color=black]coordinates{(1,3) (3,3)};
\addplot[color=black] coordinates{(0,0)};
\addplot[color=black] coordinates{(0,5)};
\addplot[color=black] coordinates{(4,0)};
\node [right] at (current axis.right of origin) {$variable\ 1$};
\node [above] at (current axis.above origin) {$variable\ 2$};
\end{axis}
\end{tikzpicture}
\end{document}
```

```tikz
\usepackage{pgfplots}
\begin{document}
\begin{tikzpicture}[domain=-10:10]
\begin{axis}[axis lines=middle,clip=false,scale=1.2]
\addplot[color=black]coordinates{(2,1) (2,3)};
\addplot[color=black] coordinates{(0,4)};
\addplot[color=black] coordinates{(4,0)};
\addplot[color=black] coordinates{(0,0)};
\node [right] at (current axis.right of origin) {$variable\ 1$};
\node [above] at (current axis.above origin) {$variable\ 2$};
\end{axis}
\end{tikzpicture}
\end{document}
```

### Recap on finding gradient
The gradient is the ratio of the rise to the run. It is the rate of change of $y$ with respect to $x$:
$$\begin{equation}\begin{aligned}
gradient(m)=\frac{rise}{run}=\frac{\Delta y}{\Delta x}=\frac{y_2-y_1}{x_2-x_1}
\end{aligned}\end{equation}$$
e.g. the gradient of the line segment connecting $(1,2)$ and $(3,8)$ is
$$\begin{equation}\begin{gathered}
gradient=\frac{y_2-y_1}{x_2-x_1}=\frac{8-2}{3-1}=\frac{6}{2}=3
\end{gathered}\end{equation}$$
This means for **every unit increase** in $x$, we will see a **3 unit increase** in $y$.

#### Mission details
Find the gradient of the graphs with the points:
1. $(1,3)$ and $(2,5)$
2. $(4,2)$ and $(5,1)$
3. $(3,2)$ and $(5,2)$
4. $(2,1)$ and $(2,7)$
