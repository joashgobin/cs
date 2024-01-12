#include <stdio.h>

int main(){
    // storing the points
    double x1=-2.5,x2=0,y1=0,y2=5;
    printf("Using the points (%g,%g) and (%g,%g)\n",x1,y1,x2,y2);
    
    // calculating gradient
    double gradient = (y2-y1)/(x2-x1);
    printf("The gradient of the line is %g\n",gradient);

    //calculating the y-intercept
    double y_intercept = y1-gradient*x1;
    printf("The y intercept is %g\n",y_intercept);

    // displaying the final equation of the straight line
    printf("Therefore the equation of the line is:\ny=%gx+%g",gradient,y_intercept);
    
    return 0;
}
