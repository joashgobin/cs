# Converting between Degrees and Radians

In order to convert degrees to radians, multiply the angle in degrees by $\pi$ and divide by $180\degree$:

$$45\degree = 45\degree \times \frac{\pi}{180\degree} \\
=\frac{\pi}{4}
$$

Take for example the code:

!{{./degree_to_radians.c}}

Conversely, we can convert from radians back to degrees by multiplying by $180\degree$ and dividing by $\pi$:
$$\frac{\pi}{3}=\frac{\pi}{3}\times \frac{180\degree}{\pi}=60\degree$$

#### Challenge
Convert the following angles to radians:
- $45\degree$
- $360\degree$
- $-135\degree$

Convert the following angles to degrees:
- $\frac{\pi}{4}\ rad$
- $3\pi \ rad$
- $\frac{-\pi}{5}\ rad$

Rewrite the C code above to convert an angle in radians, provided by the user, back to degrees.
