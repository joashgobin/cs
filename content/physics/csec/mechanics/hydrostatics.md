# 6.1 Hydrostatics
Hydrostatics is the study of fluids at rest. **Pressure** is the force exerted per unit area:
$$\begin{equation}\begin{aligned}
pressure&=\frac{force}{area}\\
P&=\frac{F}{A}
\end{aligned}\end{equation}$$
Looking at the SI unit:
$$\begin{equation}\begin{aligned}
P&=\frac{F}{A}\rightarrow \frac{N}{m^2}\rightarrow Nm^{-2}\ OR\ Pascals(Pa)
\end{aligned}\end{equation}$$
#### Example
A solid block of dimensions $2\ m\times 2\ m\times 2\ m$ is resting on a table. The block has mass $2\ kg$. Find the solid pressure exerted onto the table by the block.
$$\begin{equation}\begin{aligned}
area\ of\ the\ base&=2\ m\times 2\ m\\&=4\ m^2\\
force\ exerted&=weight\ of\ the\ block\\
&=2\ kg\times 9.81\ ms^{-2}\\
&=19.6\ N\\
pressure(P)&=\frac{force}{area}\\
&=\frac{19.6\ N}{4\ m^2}\\&=4.9\ Nm^{-2}\ OR\ 4.9\ Pa
\end{aligned}\end{equation}$$

### A note on density
Density ($\rho$) is the degree of compactness of a substance. It is the mass per unit volume:
$$\begin{equation}\begin{aligned}
density&=\frac{mass}{volume}\\
\rho&=\frac{m}{V}
\end{aligned}\end{equation}$$

## Fluid pressure
The pressure ($P$) exerted by a fluid at a point is dependent on the density of the fluid ($\rho$), acceleration due to gravity ($g$) and the depth of the point below the surface of the fluid ($h$):
$$\begin{equation}\begin{aligned}
P&=\rho gh\\
\end{aligned}\end{equation}$$
For a change in depth ($\Delta h$), the change in pressure is given by
$$\begin{equation}\begin{aligned}
\Delta P&=\rho g\Delta h\\
&OR\\
P_2-P_1&=\rho g(h_2-h_1)
\end{aligned}\end{equation}$$
Notice that pressure increases with depth:
![[image.png|460]]
Credits: [Class Notes](https://classnotes.org.in/class-8/force-and-pressure/pressure-exerted-liquids/)

### Closed versus open vessels
For a closed vessel, the above formula is used to determine the total pressure at a point ($total\ pressure(P_{total}) = fluid\ pressure(P_{fluid})$). However, for open vessels, the total pressure is the sum of the fluid pressure and atmospheric pressure:
$$\begin{equation}\begin{aligned}
P_{total}&=P_{fluid}+P_{atmosphere}\\
P_{total}&=\rho gh+P_{atmosphere}
\end{aligned}\end{equation}$$
>**Atmospheric pressure** is about $101.325\ kPa$ or $760\ mmHg\ (millimeters-mercury)$ or $1013.2\ millibars$.

### Pascal's Principle
The pressure applied to any point in **a fluid contained in a closed vessel** is ==transmitted equally to every point in the fluid==. The principle is applicable to hydraulic systems such as car braking systems and hydraulic jacks.
![[Pasted image 20221203091446.png|460]]
Credits: [Hydroline](https://hydroline.fi/blog/how-does-a-hydraulic-cylinder-work/)

The formula often used for this principle is
$$\begin{equation}\begin{aligned}
P_1&=P_2\\
\frac{F_1}{A_1}&=\frac{F_2}{A_2}
\end{aligned}\end{equation}$$
Let us say for example that the input force for a hydraulic piston is $1\ N$ and the surface area associated with this input is $1\ m^2$. 
1. If the system is ideal and the output end has an area of $100\ m^2$, what will be the output force?
$$\begin{equation}\begin{aligned}
\frac{F_{in}}{A_{in}}&=\frac{F_{out}}{A_{out}}\\
\frac{F_{in}}{A_{in}}\times A_{out}&=F_{out}\\
F_{out}&=\frac{1\ N}{1\ m^2}\times 100\ m^2\\
&=100\ N
\end{aligned}\end{equation}$$
2. If the output force moves by $4\ cm$, by how much would the input force have had to move?
For an ideal system,
$$\begin{equation}\begin{aligned}
work\ in&=work\ out\\
F_{in}\times d_{in}&=F_{out}\times d_{out}\\
d_{in}&=\frac{F_{out}\times d_{out}}{F_{in}}\\
&=\frac{100\ N\times 0.04\ m}{1\ N}\\
&=4\ m
\end{aligned}\end{equation}$$
Hence the input force (**1 Newton**) had to be moved by **4 metres** in order for the output force (*100 Newtons*) to move by only *4 centimetres*.
