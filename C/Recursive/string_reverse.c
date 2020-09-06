#include <stdio.h>

void my_strrev(char *inStr, int len)
{
    int i = 0;
    for(i=0;i<len/2;i++)
    {
        inStr[i] = inStr[i]+inStr[len-i-1];
        inStr[len-i-1] = inStr[i]-inStr[len-i-1];
        inStr[i] = inStr[i]-inStr[len-i-1];
    }
}

int main(void) {
	int i = 0;
	char str[] = {'o','p','e','r','a','t','e',0};
	printf("%s--->",str);
	my_strrev(str,7);
	printf("%s",str);
	return 0;
}
