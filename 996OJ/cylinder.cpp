#include <stdio.h>
#include <math.h>

int main(){
    double h = 10;
    double w = 10;

    //double x1 = ((-1 * M_PI * h) + sqrt((M_PI*h*h) + 4 * 3))/-6;
    double x1 = 2*M_PI*h/3;
//    double x2 = ((-1 * M_PI * h) - sqrt((M_PI*h*h) + 4 * 3))/-6;

    printf("%.4f\n", x1);
    if (x1>w) x1=w;
 //   if (x2>w) x2=w;
    double v1 = (x1*x1*h - x1*x1*x1)*M_PI/4; 
  //  double v2 = x2*x2*M_PI*h - x2*x2*x2/2;


    printf("%.4f\n", v1);
    //printf("%.4f\n", v2);
    return 0;

}
