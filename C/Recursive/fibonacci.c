#include <stdio.h>

int my_fibonacci(int num)
{
    if(num < 0)
        return -1;
    else if(num < 2)
        return num;
    else
        return my_fibonacci(num-1) + my_fibonacci(num-2);
}

int main(void)
{
    int n = 0;
    printf("\n%dth number in Fibonacci series: %d", n, my_fibonacci(n));

    int n = 1;
    printf("\n%dth number in Fibonacci series: %d", n, my_fibonacci(n));
    
    int n = 2;
    printf("\n%dth number in Fibonacci series: %d", n, my_fibonacci(n));
    
    int n = 17;
    printf("\n%dth number in Fibonacci series: %d", n, my_fibonacci(n));
}
