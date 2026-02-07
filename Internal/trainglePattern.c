#include<stdio.h>
#include<stdlib.h>

int main()
{
    int n;
    printf("enter a number");
    scanf("%d",&n);
    
    system("cls");
    for (int i = 1; i>=n; i++)
    {
        for (int j = 1; j>=i; j++)
        {
            printf("*");
        }
        printf("\n");
    }
    return 0;
}