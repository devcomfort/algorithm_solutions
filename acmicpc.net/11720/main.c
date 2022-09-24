#include <stdio.h>

int main()
{
  int n, r;

  scanf("%d", &n);

  for (r = 0; n--;)
  {
    char c;

    scanf(" %c", &c);

    r += c - '0';
  }

  printf("%d", r);

  return 0;
}