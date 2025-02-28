#include <stdio.h>
#include <string.h>

#define MAX 10005  

void bigNumberAdd(char num1[], char num2[], char result[]) {
    int len1 = strlen(num1);
    int len2 = strlen(num2);
    int carry = 0, sum, i, j, k = 0;

    char temp[MAX];
    memset(temp, 0, sizeof(temp));

    i = len1 - 1;
    j = len2 - 1;

    while (i >= 0 || j >= 0 || carry) {
        sum = carry;
        if (i >= 0) sum += num1[i--] - '0';
        if (j >= 0) sum += num2[j--] - '0';

        temp[k++] = (sum % 10) + '0'; 
        carry = sum / 10;  
    }

    int n = 0;
    for (int x = k - 1; x >= 0; x--)
        result[n++] = temp[x];
    result[n] = '\0';
}

int main() {
    char num1[MAX], num2[MAX], result[MAX];

    scanf("%s %s", num1, num2);
    bigNumberAdd(num1, num2, result);
    printf("%s\n", result);

    return 0;
}
