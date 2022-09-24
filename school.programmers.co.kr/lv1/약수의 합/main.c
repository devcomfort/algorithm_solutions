#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int n)
{
  int answer = 0;

  for (int i = 1; i * i <= n; answer += (n % i == 0 ? (
                                                          i * i == n ? i : i + n / i)
                                                    : 0),
           i++)
    ;

  return answer;
}