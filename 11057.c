#include <stdio.h>

int main(void) {
    long long   arr[11] = {1,2,3,4,5,6,7,8,9,10};
    int n, m =0;

    scanf("%d", &n);
    if (n == 1) {
        printf("10");
        return 0;
    }
    for (int jdx = 1; jdx < n - 1; jdx++) {
        for (int idx = 1; idx < 10; idx++) {
            arr[0] = 1;
            arr[idx] = (arr[idx - 1] + arr[idx]) % 10007;
        }
    }
    for (int idx = 0; idx < 10; idx++)
        m += arr[idx];
    m %= 10007;
    printf("%d", m);
    return 0;
}

/**
 * 1    = 10
 * 2    = 55 (90개) 1 2 3 4 5 6 7 8 9 
 * 100 ~ 999    = 220 (900개) 0(1) 1()
 *                                              01 12 23 34 45 56  67 78 89 
 * 1000 ~ 9999  =   715                         012 123 234 345 456 567 678 789
 * 1111 ~ 1999
*/