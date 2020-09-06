#include <stdio.h>

int my_factorial(int num)
{
    if(num < 0)
        return -1;
    else if(num == 0)
        return 1;
    else
        return num * my_factorial(num-1); 
}

int main(void)
{
    printf("-2! = ", factorial(-2));
    printf("0!  = ", factorial(0));
    printf("1!  = ", factorial(1));
    printf("10! = ", factorial(10));
}
