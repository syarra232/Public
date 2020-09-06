#include <stdio.h>

int my_sum_of_digits(int num)
{
    int sum = 0;
    if(num < 10)
        return num;
    else
        sum += (num%10 + my_sum_of_digits(num/10));
    
    if(sum >=10)
        my_sum_of_digits(sum);
    return sum;
}

int main(void)
{
    int n = 0;
    printf("\n Sum of the Digits of %d = %d", n, my_sum_of_digits(n));
    
    n = -4;
    printf("\n Sum of the Digits of %d = %d", n, my_sum_of_digits(n));
    
    n = 7;
    printf("\n Sum of the Digits of %d = %d", n, my_sum_of_digits(n));
    
    n = 123;
    printf("\n Sum of the Digits of %d = %d", n, my_sum_of_digits(n));

    n = 2784;
    printf("\n Sum of the Digits of %d = %d", n, my_sum_of_digits(n));
}
