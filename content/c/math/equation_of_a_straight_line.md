# Equation of a Straight Line
Any straight line can be written in the standard form:
$$y=mx+c$$

The gradient, $m$ is given by the formula:
$$m=\frac{y_2-y_1}{x_2-x_1}$$

The y-intercept, $c$ can be found by substituting the gradient and any of the points
(in this case we use $(x_1,y_1)$) into the standard form of the line equation:
$$y_1=mx_1+c$$
$$\therefore c=y_1-mx_1$$

The following code snippet shows how we can replicate this in C:
!{{./finding_the_equation_of_a_line_given_two_points.c}}
