#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main()
{
    char *A = (char *)calloc(10002, sizeof(char)),
         *B = (char *)calloc(10002, sizeof(char));
    char *R = (char *)calloc(10003, sizeof(char));

    int A_LEN, B_LEN;
    int i;

    scanf(" %s %s", A, B);

    A_LEN = strlen(A);
    B_LEN = strlen(B);

    for (i = 0;; i++)
    {
        int INDEX_A = A_LEN - i - 1,
            INDEX_B = B_LEN - i - 1;

        if (INDEX_A < 0 && INDEX_B < 0)
            break;

        if (INDEX_A < 0)
        {
            R[i] = B[INDEX_B] - '0';
            continue;
        }

        if (INDEX_B < 0)
        {
            R[i] = A[INDEX_A] - '0';
            continue;
        }

        R[i] = A[INDEX_A] + B[INDEX_B] - '0' * 2;
    }

    for (int j = 0; j < i; j++)
    {
        R[j + 1] += R[j] / 10;
        R[j] = R[j] % 10;
    }

    if (R[i] > 0)
        i++;

    while (1)
    {
        printf("%d", R[--i]);
        if (i <= 0)
            break;
    }

    return 0;
}