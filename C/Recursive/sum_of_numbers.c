#include <stdio.h>

int my_sum(int num)
{
    if(num < 0)
        return -1;
    if(num == 0)
        return 0;
    else
        return num+sum(num-1);
}

int main(void)
{
    int n = 0;
    printf("\n Sum of First %d numbers = %d", n, my_sum(n));
    
    int n = 21;
    printf("\n Sum of First %d numbers = %d", n, my_sum(n));
}
